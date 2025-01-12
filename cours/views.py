from django.shortcuts import render

def home_view(request):
    return render(request, 'cours/home.html')  # Assurez-vous que ce chemin est correct
