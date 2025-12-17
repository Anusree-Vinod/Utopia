from django.shortcuts import render,redirect
from AdminApp.models import CategoryDB,ProductDb
from WebApp.models import RegistrationDB,ContactDB, cartDB,orderDB
from django.contrib import messages
import razorpay
# Create your views here.
def home_fun(request):
    categories = CategoryDB.objects.all()
    products = ProductDb.objects.all()
    cart_total = 0
    un = request.session.get('name')
    if un:
        cart_total = cartDB.objects.filter(username=un).count()
    return render(request,"home.html",{'categories':categories,'products':products,'cart_total':cart_total})

def about_fun(request):
    categories = CategoryDB.objects.all()
    cart_total = 0
    un = request.session.get('name')
    if un:
        cart_total = cartDB.objects.filter(username=un).count()
    return  render(request,"about.html",{'categories':categories,'cart_total':cart_total})

def contact_fun(request):
    categories = CategoryDB.objects.all()
    cart_total = 0
    un = request.session.get('name')
    if un:
        cart_total = cartDB.objects.filter(username=un).count()
    return render(request,"contact.html",{'categories':categories,'cart_total':cart_total})

def checkout_fun(request,total):
    categories = CategoryDB.objects.all()
    return render(request,"checkout.html",{'categories':categories,'total':total})

def products_page_fun(request):
    categories = CategoryDB.objects.all()
    products = ProductDb.objects.all()
    cart_total = 0
    un = request.session.get('name')
    if un:
        cart_total = cartDB.objects.filter(username=un).count()
    return render(request,"All_products.html",{'categories':categories,'products':products,'cart_total':cart_total})

def filtered_product_fun(request,product_category):
    categories = CategoryDB.objects.all()
    products = ProductDb.objects.filter(category=product_category)
    desc = CategoryDB.objects.get(name=product_category).description
    cart_total = 0
    un = request.session.get('name')
    if un:
        cart_total = cartDB.objects.filter(username=un).count()
    return render(request,"filtered_product.html",{'categories':categories,'products':products,'product_category':product_category,
                                                   'desc':desc,'cart_total':cart_total})

def single_product_fun(request,prod_id):
    categories = CategoryDB.objects.all()
    product = ProductDb.objects.get(id=prod_id)
    cart_total = 0
    un = request.session.get('name')
    if un:
        cart_total = cartDB.objects.filter(username=un).count()
    return render(request,"single_product.html",{'product':product,'categories':categories,'cart_total':cart_total})

def user_signin_fun(request):
    return render(request,"user_sign_in.html")

def user_signup_fun(request):
    return render(request,"user_signup.html")

def user_registration(request):
    if request.method == "POST":
        n = request.POST.get('name')
        e = request.POST.get('email')
        c = request.POST.get('contact')
        a = request.POST.get('address')
        p = request.POST.get('pwd')
        cp = request.POST.get('confirm_pwd')
        obj = RegistrationDB(name=n,email=e,contact=c,address=a,password=p,confirm_pwd=cp)
        obj.save()
        return redirect(user_signin_fun)

def user_login(request):
    if request.method == "POST":
        un = request.POST.get('username')
        p = request.POST.get('pwd')
        if RegistrationDB.objects.filter(name=un,password=p).exists():
            request.session['name']=un
            request.session['password']=p
            messages.success(request, "Login Success!")
            return redirect(home_fun)
        else:
            messages.warning(request, "Invalid Credentials")
            return redirect(user_signin_fun)
    else:
        messages.warning(request, "Invalid credentials")
        return redirect(user_signin_fun)

def user_logout(request):
    del request.session['name']
    del request.session['password']
    messages.success(request, "Logged Out!")
    return redirect(home_fun)

def save_messages(request):
    if request.method == "POST":
        n = request.POST.get('name')
        e = request.POST.get('email')
        m = request.POST.get('msg')
        obj = ContactDB(name=n,email=e,message=m)
        obj.save()
        messages.success(request, "Message Send Successfully!")
        return redirect(contact_fun)

def cart_fun(request):
    categories = CategoryDB.objects.all()
    cart = cartDB.objects.filter(username=request.session['name'])
    sub_total = 0
    del_charge = 0
    total_amt = 0
    for i in cart:
        sub_total += i.total
    if sub_total > 600:
        del_charge = 49
    else:
        del_charge = 99
    total_amt = del_charge+sub_total
    return render(request,"cart.html",{'categories':categories,'cart':cart,'sub_total':sub_total,
                                       'del_charge':del_charge,'total_amt':total_amt})

def save_cart(request):
    if request.method == "POST":
        un = request.POST.get('username')
        p = request.POST.get('product')
        price = request.POST.get('price')
        qty = request.POST.get('qty')
        t = request.POST.get('total')
        prod = ProductDb.objects.filter(name=p).first()
        img = prod.image if prod else None
        obj = cartDB(username=un,product=p,price=price,quantity=qty,total=t,image=img)
        obj.save()
        messages.success(request, "Item added to cart!!")
        return redirect(products_page_fun)

def delete_cart_item(request,p_id):
    data = cartDB.objects.filter(id=p_id)
    data.delete()
    messages.success(request, "Item Deleted!!")
    return redirect(cart_fun)

def save_order(request):
    if request.method == "POST":
        n = request.POST.get('name')
        e = request.POST.get('email')
        c = request.POST.get('contact')
        add = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pin = request.POST.get('pincode')
        tot = request.POST.get('total')
        obj = orderDB(name=n,email=e,contact=c,address=add,city=city,
                      state=state,pincode=pin,total_amt=tot)
        obj.save()
        return redirect(payment_page)

def payment_page(request):
    # Adding details for payment
    # Retrieve the data from orderdb with the specified ID
    customer = orderDB.objects.order_by('-id').first()
    # Get the amount of the specified customer
    payy = customer.total_amt
    amount = int(payy * 100)
    payy_str = str(amount)

    if request.method == "POST":
        order_currency = 'INR'
        client = razorpay.Client(auth=('rzp_test_0ib0jPwwZ7I1lT', 'VjHNO5zKeKxz8PYe7VnzwxMR'))
        payment = client.order.create({'amount':amount, 'currency':order_currency})

    return render(request,"payment.html",{'payy_str':payy_str})