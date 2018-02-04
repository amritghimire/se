# core/api_urls.py
"""Called from the project root's urls.py URLConf thus:
        url(r'^api/', include('core.api_urls', namespace='api')),
"""
from django.urls import path

from userProfile.api.v1 import views as userprofile_views

app_name = "userProfile"

urlpatterns = [
    # {% url 'api:UserProfiles' %}
    path(
        r'user/',
        view=userprofile_views.UserProfileListCreateAPIView.as_view(),
        name='user'
    ),
    # {% url 'api:UserProfiles' UserProfile.uuid %}
    path(
        r'^user/(?P<uuid>[-\w]+)/$',
        view=userprofile_views.UserProfileRetrieveUpdateDestroyAPIView.as_view(),
        name='user'
    ),
    path(
        '/', userprofile_views.home, name='main'
    )
]
