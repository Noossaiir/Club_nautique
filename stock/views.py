from django.shortcuts import render

def stock_index(request):
    return render(request, 'stock/index.html', {
        'message': "Bienvenue dans la gestion du stock.",
    })
