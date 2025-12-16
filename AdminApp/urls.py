from django.urls import path
from AdminApp import views

urlpatterns = [
    path('index_fun/',views.index_fun,name="index_fun"),
    path('add_categories/',views.add_categories,name="add_categories"),
    path('view_categories/',views.view_categories,name="view_categories"),
    path('save_category/',views.save_category,name="save_category"),
    path('edit_category/<int:c_id>/',views.edit_category,name="edit_category"),
    path('update_category/<int:c_id>/',views.update_category,name="update_category"),
    path('delete_category/<int:c_id>/',views.delete_category,name="delete_category"),
    path('add_product/',views.add_product,name="add_product"),
    path('save_product/',views.save_product,name="save_product"),
    path('view_products/',views.view_products,name="view_products"),
    path('edit_product/<int:p_id>/',views.edit_product,name="edit_product"),
    path('update_product/<int:p_id>/',views.update_product,name="update_product"),
    path('delete_product/<int:p_id>/',views.delete_product,name="delete_product"),
    path('admin_login_page/',views.admin_login_page,name="admin_login_page"),
    path('admin_login/',views.admin_login,name="admin_login"),
    path('view_messages/',views.view_messages,name="view_messages"),
    path('delete_message/<int:m_id>/',views.delete_message,name="delete_message")
]