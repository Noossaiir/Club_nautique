from django.shortcuts import render

def locations_index(request):
    return render(request, 'locations/index.html', {
        'message': "Bienvenue dans la section des locations.",
    })
