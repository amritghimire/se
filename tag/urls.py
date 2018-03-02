from django.urls import path

from . import views

app_name = "tag"


urlpatterns = [
    path('add', views.select_tag_user_view, name='add'),
]
