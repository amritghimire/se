from tastypie.resources import ModelResource
from userProfile.models import UserProfile

class UserModelResource(ModelResource):
    class Meta:
        queryset = UserProfile.objects.all()
        allowed_methods = ['get']

