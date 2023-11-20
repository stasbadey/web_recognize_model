from django.urls import path
from . import views

app_name = 'home_page'

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('model/', views.model, name='model'),
    path('model/classify/', views.classify_image, name='classify_image'),
    path('model/model_view/', views.model_view, name='model_view'),
]