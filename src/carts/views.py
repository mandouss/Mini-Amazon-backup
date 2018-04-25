from django.shortcuts import render, redirect

from goods.models import Good
# Create your views here.

from .models import Cart


def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    #e = GoodQuantity.objects.filter(cart=cart_obj)
    print(e)
    return render(request, "carts/home.html", {"cart": cart_obj })


def cart_update(request):
    good_id = request.POST.get('good_id')
    if good_id is not None:
        try:
            good_obj = Good.objects.get(id=good_id)
        except Good.DoesNotExist:
            print("Show message touser, product is gone?")
            return redirect("cart:home")
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        if good_obj in cart_obj.goods.all(): 
            #GoodQuantity.objects.get(good=good_obj, cart=cart_obj).delete()
            cart_obj.goods.remove(good_obj)
        else:      
            #e = GoodQuantity.objects.create(good=good_obj, cart=cart_obj)
            #e.save()
            cart_obj.goods.add(good_obj) #ManyToManyField
            #print(e)
        request.session['cart_items'] = cart_obj.goods.count()
        #cart_obj.goods.remove(obj)
    return redirect("cart:home")
