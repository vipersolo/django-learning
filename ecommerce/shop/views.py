from django.shortcuts import render,redirect,get_object_or_404
from .models import Product,Order,OrderItem
from django.contrib.auth.decorators import login_required

# Create your views here.

#-------------------------
#important point when ever using session,cookies,JSON storage,Redis cache,  ALWAYS KEEP DICTONARY KEYS AS STRINGS
#-------------------------



def product_list(request):
    products = Product.objects.all()
    return render(request,'shop/product_list.html',{'products':products})

def add_to_cart(request,product_id):
    cart = request.session.get("cart",{})
    cart[str(product_id)]=cart.get(str(product_id),0) + 1
    # cart[product_id] = cart.get("product_id",0)+1 product_id is taken as literal not value there for no match never changes.
    request.session["cart"] = cart
    print(request.session.get("cart",{}))
    return redirect("cart_details")

def cart_details(request):
    cart = request.session.get("cart",{})
    products=[]
    total = 0
    for product_id,quantity in cart.items():
        product  = get_object_or_404(Product,pk=int(product_id))
        subtotal = product.price * quantity
        products.append({'product':product,'quantity':quantity,'subtotal':subtotal})
        total+=subtotal
    return render(request,'shop/cart_details.html',{'products':products,'total':total})



def remove_from_cart(request,product_id):
    cart = request.session.get('cart',{})
    if str(product_id) in cart:
        del cart[str(product_id)]
    request.session['cart'] = cart
    return redirect('cart_details')

@login_required
def checkout(request):
    cart = request.session.get("cart",{})
    if not cart:
        return redirect("product_list")
    order = Order.objects.create(customer = request.user)
    for product_id,quantity in cart.items():
        product = get_object_or_404(Product,pk=int(product_id))
        OrderItem.objects.create(order=order,product=product,quantity=quantity)
    request.session["cart"] = {}
    return redirect("checkout_success",order_id=order.id)

@login_required
def checkout_success(request,order_id):
    order = Order.objects.get(pk=order_id)
    return render(request,"shop/checkout_success.html",{"order":order})