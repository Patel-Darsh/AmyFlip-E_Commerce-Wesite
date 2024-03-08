from django.urls import path,include
from electronic import views

app_name = 'products'

urlpatterns = [
    #----------------------------categories url-----------------------------------
    path('categories/<int:cat_id>/', views.view_category, name='categories'),

    #----------------------------home url-----------------------------------
    path('home/', views.index, name='index'),

    #----------------------------home url-----------------------------------
    path('products/', views.products, name='products'),

    #----------------------------detail page url----------------------------
    path('detail/<int:item_id>/', views.detail, name='detail'),

    #----------------------------add item url-------------------------------
    path('add/',views.create_item, name='create_item'),

    #----------------------------delete item url----------------------------
    path('delete/<int:id>/',views.delete_item, name='delete_item'),

    #----------------------------update item url----------------------------
    path('update/<int:id>/', views.update_item, name='update_item'),

    #----------------------------cart  url----------------------------
    path('cart/', views.view_cart, name='view_cart'),

    #----------------------------add to cart url----------------------------
    path('add-to-cart/<int:id>/', views.add_to_cart, name='add_to_cart'),

    path('update-cart/<int:cart_item_id>/', views.update_cart, name='update_cart'),

    path('remove-from-cart/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),

    #-------------------------------------------------------------------------------------------

    path('checkout/', views.checkout_page, name='checkout'),

    path('order_checkout/<int:id>/', views.order_checkout, name='order_checkout'),

]
