# core/api_urls.py
"""Called from the project root's urls.py URLConf thus:
        url(r'^api/', include('core.api_urls', namespace='api')),
"""
from django.urls import path

from userProfile_app.api.v1 import views as userprofile_views

app_name = "userProfile"

urlpatterns = [
    # {% url 'api:UserProfiles' %}
    path(
        r'user',
        view=userprofile_views.UserProfileListCreateAPIView.as_view(),
        name='user'
    ),
    # {% url 'api:login' %}
    path(
        r'login',
        view=userprofile_views.Login.as_view(),
        name='login'
    ),
    # {% url 'api:signup' %}
    path(
        r'signup',
        view=userprofile_views.SignUp.as_view(),
        name='signup'
    ),
    # {% url 'api:UserProfiles' UserProfile.uuid %}
    path(
        r'user/<uuid>/',
        view=userprofile_views.UserProfileRetrieveUpdateDestroyAPIView.as_view(),
        name='user'
    ),
    path(
        '', userprofile_views.Home, name='main'
    )
]
