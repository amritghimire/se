from django.urls import path

from . import views

app_name="bridge"
urlpatterns = [
    path('', views.home, name='index'),
    path('template/<template_name>',views.template,name="template")
]
