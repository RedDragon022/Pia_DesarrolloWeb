from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Product, Event, Branch, Comment


def home(request):
    latest_products = Product.objects.all()[:3]
    success_message = ''
    if request.GET.get('ok') == '1':
        success_message = '¡Gracias por tu comentario! Será revisado pronto.'
    context = {
        'products': latest_products,
        'page_title': 'Inicio',
        'success_message': success_message,
    }
    return render(request, 'cafeteria/home.html', context)


def about(request):
    context = {'page_title': 'Acerca de Nosotros'}
    return render(request, 'cafeteria/about.html', context)


def menu(request):
    products = Product.objects.all()
    context = {
        'products': products,
        'page_title': 'Menú Completo',
        'total_products': products.count()
    }
    return render(request, 'cafeteria/menu.html', context)


def events(request):
    all_events = Event.objects.all()
    context = {
        'events': all_events,
        'page_title': 'Eventos',
        'total_events': all_events.count()
    }
    return render(request, 'cafeteria/events.html', context)


def branches(request):
    all_branches = Branch.objects.all()
    context = {
        'branches': all_branches,
        'page_title': 'Nuestras Sucursales',
        'total_branches': all_branches.count()
    }
    return render(request, 'cafeteria/branches.html', context)


def comment(request):
    error = ''
    if request.method == 'POST':
        author = request.POST.get('author', '').strip()
        email = request.POST.get('email', '').strip()
        content = request.POST.get('content', '').strip()

        if not author or not content:
            error = 'Por favor completa todos los campos obligatorios.'
        elif len(content) < 10:
            error = 'El comentario debe tener al menos 10 caracteres.'
        else:
            Comment.objects.create(author=author, email=email, content=content)
            return redirect(reverse('cafeteria:home') + '?ok=1')

    context = {'page_title': 'Enviar Comentario', 'error': error}
    return render(request, 'cafeteria/comment.html', context)
