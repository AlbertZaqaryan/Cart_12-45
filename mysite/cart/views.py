from django.shortcuts import render, redirect
from main.models import Shoe
from .models import Cart
# Create your views here.


def cart(request):
    summ = 0
    if request.method == 'POST':
        prod_id = request.POST.get('id')
        mymodel = Shoe.objects.get(id=prod_id)
        Cart.objects.create(prod=mymodel)
        return redirect('index')
    cart_list = Cart.objects.all()
    for i in cart_list:
        summ += i.prod.price
    return render(request, 'cart/cart.html', context={
        'cart_list':cart_list,
        'summ':summ
    })


def delete_prod(request):
    if request.method == 'POST':
        prod_id = request.POST.get('id')
        Cart.objects.filter(id=prod_id).delete()
        return redirect('cart')