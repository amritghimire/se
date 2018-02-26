from django.contrib import admin
from .models import UserProfile


# Register your models here.


@admin.register(UserProfile)
class UserProfileModelAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'email', 'gender', 'uuid')
