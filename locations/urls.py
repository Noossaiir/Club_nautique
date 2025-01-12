from django.urls import path
from . import views

urlpatterns = [
    path('', views.locations_index, name='locations_index'),
]
