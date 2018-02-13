from django.urls import path

from . import views

app_name = "bridge"
urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name=''),
    path('template/<template_name>', views.template, name="template")
]
