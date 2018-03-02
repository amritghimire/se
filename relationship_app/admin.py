from django.contrib import admin
from .models import Relationship,RelationshipWithQuestion

# Register your models here.
admin.site.register(Relationship)
admin.site.register(RelationshipWithQuestion)
