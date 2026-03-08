from django.urls import path
from . import views

urlpatterns=[
    path("",views.product_list,name='product_list'),
    path("add/<int:product_id>",views.add_to_cart,name="add_to_cart"),
    path("cart/",views.cart_details,name="cart_details"),
    path("remove/<int:product_id>",views.remove_from_cart,name="remove_from_cart"),
    path("checkout/",views.checkout,name="checkout"),
    path("checkout_success/<int:order_id>",views.checkout_success,name="checkout_success")
]