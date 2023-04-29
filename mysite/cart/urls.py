from django.urls import path
from . import views

urlpatterns=[
    path('', views.cart, name='cart'),
    path('delete_prod/', views.delete_prod, name='delete_prod'),
]