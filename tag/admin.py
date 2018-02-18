from django.contrib import admin

# Register your models here.
from tag.models import Tag


@admin.register(Tag)
class TagModelAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'name', 'uuid', 'slug')
