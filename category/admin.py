from django.contrib import admin

# Register your models here.
from .models import Category


@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'slug', 'summary', 'uuid')
