from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Vue pour la page d'accueil
def home_view(request):
    return render(request, 'home.html')

# Vue pour gérer l'inscription
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Compte créé avec succès. Veuillez vous connecter.')
            return redirect('login')  # Rediriger vers la page de connexion
        else:
            messages.error(request, 'Veuillez corriger les erreurs.')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

# Vue pour gérer la connexion
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Rediriger vers la page d'accueil après connexion
        else:
            messages.error(request, 'Nom d’utilisateur ou mot de passe invalide.')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

# Vue pour gérer la déconnexion
def logout_view(request):
    logout(request)
    messages.info(request, 'Vous êtes déconnecté.')
    return redirect('home')
