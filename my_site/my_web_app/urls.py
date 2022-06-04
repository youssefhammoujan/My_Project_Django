from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="home"),
    path('description.html', views.desc_pro,name="description"),
]
