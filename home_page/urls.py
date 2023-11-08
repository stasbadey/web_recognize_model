from django.urls import path, include
from . import views

app_name = 'home_page'

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('model/', views.model, name='model'),
]
