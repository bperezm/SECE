from django.shortcuts import render
from django.contrib import messages

from django.views.generic import View

from .email import *


def home(request):
    template_name = 'santillana/home.html'
    return render(request, template_name, {})


def certificacion(request):
    template_name = 'santillana/certificacion.html'
    return render(request, template_name, {})


def estandares(request):
    template_name = 'santillana/estandares.html'
    return render(request, template_name, {})


def conocer(request):
    template_name = 'santillana/conocer.html'
    return render(request, template_name, {})


def prueba(request):
    template_name = 'santillana/prueba.html'
    return render(request, template_name, {})


def informacion(request):
	template_name = 'santillana/informacion.html'
	return render(request, template_name, {})


def etica(request):
     template_name = "santillana/etica.html"
     return render(request, template_name, {})


def contacto(request):
     if request.method == 'GET':
         template_name = "santillana/contacto.html"
         return render(request, template_name, {})
     
     if request.method == 'POST':
        template_name = "santillana/contacto.html"
        if send_mail(request):
              messages.success(request, 'Tu correo se envio correctamente, pronto nos comunicaremos contigo.')
              return render(request, template_name, {})
        else:
              messages.warning(request, 'No se logro enviar tu correo correctamente, intentalo de nuevo.')
              return render(request, template_name, {'mensaje': 'No se puede enviar'})


def aviso(request):
     template_name = "santillana/aviso.html"
     return render(request, template_name, {})


def condiciones(request):
     template_name = "santillana/condiciones.html"
     return render(request, template_name, {})
