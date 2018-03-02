from django.urls import path

from . import views

app_name = "category_app"


urlpatterns = [
    path('add', views.select_category_user_view, name='add'),
]
