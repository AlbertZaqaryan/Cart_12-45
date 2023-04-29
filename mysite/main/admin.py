from django.contrib import admin
from .models import Shoe
# Register your models here.


@admin.register(Shoe)
class ShoeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price']
    list_display_links = ['id', 'name']
    search_fields = ['name', 'price']