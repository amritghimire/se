from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'title', 'uuid', 'owner')
