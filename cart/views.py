from django.shortcuts import render,redirect, get_object_or_404
from products.models import product
from .models import Cart, CartItem
import razorpay
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

def _cart_id(request):
    cart=request.session.session_key
    if not cart:
        cart= request.session.create()
    return cart

def add_cart(request,product_id):
    products = product.objects.get(id=product_id)
    try :
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = _cart_id(request)
        )
        cart.save()
    try:
        cart_item = CartItem.objects.get(product=products,cart=cart)
        if cart_item.quantity < cart_item.product.stock:
            cart_item.quantity +=1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product = products,
            quantity=1,
            cart=cart
        )
        cart_item.save()
    return redirect('cart:cart_details')

def cart_details(request,total=0,counter=0,items=None):
    try:
        cart= Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart,active=True)
        for cart_item in cart_items:
            total +=(cart_item.product.product_price * cart_item.quantity)
            
            counter += cart_item.quantity
        
        
    except ObjectDoesNotExist:
        pass
    # client = razorpay.Client(auth = (settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
    # payment = client.order.create({'amount':total, 'currency':'INR','payment_capture': 1 })
    # cart.razor_pay_order_id = payment['id']
    cart.save()
    
    
    # print("***********")
    # print(payment)
    # print("***********")

    return render(request,'cart.html',dict(cart_items=cart_items,total=total,counter=counter))

def cart_remove(request,product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    products=get_object_or_404(product,id=product_id)
    cart_item = CartItem.objects.get(product=products,cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect("cart:cart_details")

def cart_fullremove(request,product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    products=get_object_or_404(product,id=product_id)
    cart_item = CartItem.objects.get(product=products,cart=cart)
    cart_item.delete()
    return redirect("cart:cart_details")