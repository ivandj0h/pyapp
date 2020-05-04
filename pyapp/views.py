from django.shortcuts import render


def index(request):
    context = {
        'title': 'PYAPP - Home',
        'hero_title': 'Dashboard'
    }
    return render(request, 'index.html', context)


def blog(request):
    context = {
        'title': 'PYAPP - Blog',
        'hero_title': 'Blog'
    }
    return render(request, 'blog.html', context)


def about(request):
    context = {
        'title': 'PYAPP - About',
        'hero_title': 'About'
    }
    return render(request, 'about.html', context)
