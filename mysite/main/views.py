from django.shortcuts import render
from .models import Shoe
from cart.models import Cart
# Create your views here.
def index(request):
    shoes = Shoe.objects.all()
    cart_list = Cart.objects.all()
    return render(request, 'main/index.html', context={
        'shoes':shoes,
        'cart_list':cart_list
    })