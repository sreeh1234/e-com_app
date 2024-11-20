from django .urls import path 
from . import views


urlpatterns = [
    path('',views.e_com_login),
    path('shop_home',views.shop_home),
    path('logout',views.e_com_logout),
    path('add product',views.add),
    path('edit_product/<id>',views.edit_product),
    path('delete_product/<pid>',views.delete),
    
    
# ----------------------------------------user----------------------------------------------

    path('register',views.register),
    path('user_home',views.user_home),
    path('view_product/<pid>',views.view_product),
    path('addtocart/<pid>',views.add_to_cart),
    path('viewcart',views.view_cart),
    path('increment/<cid>',views.qty_incri),
    path('decrement/<cid>',views.qty_dec),
    path('buyproduct/<pid>',views.buy_product),
    path('userbookings',views.user_bookings),
    
    
    
    
    
]
