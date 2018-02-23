from django.contrib import admin

# Register your models here.
from recommendation.models import Recommended, NotRecommended

admin.site.register(Recommended)
admin.site.register(NotRecommended)
