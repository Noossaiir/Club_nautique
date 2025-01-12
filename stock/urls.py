from django.urls import path
from . import views

urlpatterns = [
    path('', views.stock_index, name='stock_index'),
]
