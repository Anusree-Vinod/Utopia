from django.shortcuts import render,redirect
from AdminApp.models import CategoryDB,ProductDb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from WebApp.models import ContactDB
from django.contrib import messages
# Create your views here.
def index_fun(request):
    Categories = CategoryDB.objects.count()
    products = ProductDb.objects.count()
    return render(request,"Index.html",{'Categories':Categories,'products':products})

def add_categories(request):
    return render(request,"add_categories.html")

def view_categories(request):
    data = CategoryDB.objects.all()
    return render(request,"view_categories.html",{'data':data})

def save_category(request):
    if request.method == "POST":
        n = request.POST.get('name')
        d =  request.POST.get('desc')
        i = request.FILES['cat_img']
        obj = CategoryDB(description=d,name=n,image=i)
        obj.save()
        messages.success(request,"Category Saved Successfully!!")
        return redirect(add_categories)

def edit_category(request,c_id):
    c = CategoryDB.objects.get(id=c_id)
    return render(request,"edit_category.html",{'c':c})

def update_category(request,c_id):
    if request.method == "POST":
        n = request.POST.get('name')
        d = request.POST.get('desc')
        try:
            g = request.FILES['cat_img']
            fs = FileSystemStorage()
            i = fs.save(g.name,g)
        except MultiValueDictKeyError:
            i = CategoryDB.objects.get(id=c_id).image
        CategoryDB.objects.filter(id=c_id).update(description=d,name=n,image=i)
        messages.success(request, "Category Updated Successfully!!")
        return redirect(view_categories)

def delete_category(request,c_id):
    data = CategoryDB.objects.get(id=c_id)
    data.delete()
    messages.success(request, "Category Deleted Successfully!!")
    return redirect(view_categories)

def add_product(request):
    categories = CategoryDB.objects.all()
    return render(request,"Add_product.html",{'categories':categories})

def save_product(request):
    if request.method == "POST":
        n = request.POST.get('name')
        d = request.POST.get('desc')
        p = request.POST.get('price')
        c = request.POST.get('category')
        img = request.FILES['prod_img']
        obj = ProductDb(name=n,price=p,description=d,category=c,image=img)
        obj.save()
        messages.success(request, "Product Saved Successfully!!")
        return redirect(add_product)

def view_products(request):
    data = ProductDb.objects.all()
    return render(request,"View_products.html",{'data':data})

def edit_product(request,p_id):
    p = ProductDb.objects.get(id=p_id)
    return  render(request,"edit_product.html",{'p':p})

def update_product(request,p_id):
    if request.method == "POST":
        n = request.POST.get('name')
        d = request.POST.get('desc')
        p = request.POST.get('price')
        c = request.POST.get('category')
        try:
            g = request.FILES['prod_img']
            fs = FileSystemStorage()
            img = fs.save(g.name,g)
        except MultiValueDictKeyError:
            img = ProductDb.objects.get(id=p_id).image
        ProductDb.objects.filter(id=p_id).update(name=n,price=p,description=d,category=c,image=img)
        messages.success(request, "Product Updated Successfully!!")
        return redirect(view_products)

def delete_product(request,p_id):
    data = ProductDb.objects.get(id=p_id)
    data.delete()
    messages.success(request, "Product Deleted Successfully!!")
    return redirect(view_products)

def admin_login_page(request):
    return render(request,"Admin_login.html")

def admin_login(request):
    if request.method == "POST":
        un = request.POST.get('username')
        pw = request.POST.get('password')
        if User.objects.filter(username__contains=un).exists():
            data = authenticate(username=un,password=pw)
            if data is not None:
                login(request,data)
                request.session['username']=un
                request.session['password']=pw
                return redirect(index_fun)
            else:
                return redirect(admin_login_page)
        else:
            return redirect(admin_login_page)

def view_messages(request):
    data = ContactDB.objects.all()
    return render(request,"view_messages.html",{'data':data})

def delete_message(request,m_id):
    data = ContactDB.objects.get(id=m_id)
    data.delete()
    return redirect(view_messages)