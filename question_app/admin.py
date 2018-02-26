from django.contrib import admin

# Register your models here.
from question_app.models import Question


@admin.register(Question)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'title', 'slug', 'uuid')
