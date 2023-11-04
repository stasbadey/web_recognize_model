from django.urls import path, include
from . import views

urlpatterns = [
    path('home_page/', views.home_page, name='home_page'),
    path('model/', views.model, name='model'),
]
