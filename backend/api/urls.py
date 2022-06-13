from django.urls import path
 
from . import views
 
urlpatterns = [
    path('login',views.login,name='login'),
    path('get_all_product',views.get_all_product,name='get_all_product'),
    path('get_all_product_url',views.get_all_product_url,name='get_all_product_url'),
    path('add_product_url',views.add_product_url,name='add_product_url'),
    path('get_all_user',views.get_all_user,name='get_all_user'),
    path('operator_user',views.operator_user,name='operator_user'),
    path('operator_product',views.operator_product,name='operator_product'),
    path('set_user_money',views.set_user_money,name='set_user_money'),
    path('add_user_prize',views.add_user_prize,name='add_user_prize'),
    path('del_user_prize',views.del_user_prize,name='del_user_prize'),
    path('get_user_prize',views.get_user_prize,name='get_user_prize'),
]