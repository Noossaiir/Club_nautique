from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='cours_index'),  # Nom de l'URL utilisé dans le template
]
