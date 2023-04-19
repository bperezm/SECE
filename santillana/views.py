from django.shortcuts import render


def home(request):
    template_name = 'santillana/home.html'
    return render(request, template_name, {})


def certificacion(request):
    template_name = 'santillana/certificacion.html'
    return render(request, template_name, {})


def estandares(request):
    template_name = 'santillana/estandares.html'
    return render(request, template_name, {})
