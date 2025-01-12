from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from club_nautique.views import signup, home_view  # Import des vues personnalisées

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),  # Page d'accueil
    path('cours/', include('cours.urls')),
    path('locations/', include('locations.urls')),
    path('stock/', include('stock.urls')),

    # Auth URLs
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),  # Redirection après déconnexion
    path('signup/', signup, name='signup'),  # Vue pour l'inscription
]
