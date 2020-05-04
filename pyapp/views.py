from django.shortcuts import render


def index(request):
    context = {
        'title': 'PYAPP - Home',
        'hero_title': 'PYAPP Dashboard'
    }
    return render(request, 'index.html', context)
