from django.urls import path
from WebApp import views

urlpatterns = [
    path('home_fun/',views.home_fun,name="home_fun"),
    path('about_fun/',views.about_fun,name="about_fun"),
    path('contact_fun/',views.contact_fun,name="contact_fun"),
    path('checkout_fun/<int:total>',views.checkout_fun,name="checkout_fun"),
    path('products_page_fun/',views.products_page_fun,name="products_page_fun"),
    path('filtered_product_fun/<product_category>',views.filtered_product_fun,name="filtered_product_fun"),
    path('single_product_fun/<int:prod_id>',views.single_product_fun,name="single_product_fun"),
    path('user_signin_fun/',views.user_signin_fun,name="user_signin_fun"),
    path('user_signup_fun/',views.user_signup_fun,name="user_signup_fun"),
    path('user_registration/',views.user_registration,name="user_registration"),
    path('user_login/',views.user_login,name="user_login"),
    path('user_logout/',views.user_logout,name="user_logout"),
    path('save_messages/',views.save_messages,name="save_messages"),
    path('cart_fun/',views.cart_fun,name="cart_fun"),
    path('save_cart/',views.save_cart,name="save_cart"),
    path('delete_cart_item/<int:p_id>',views.delete_cart_item,name="delete_cart_item"),
    path('payment_page',views.payment_page,name="payment_page"),
    path('save_order',views.save_order,name="save_order"),
]