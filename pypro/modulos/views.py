from django.shortcuts import render

# Create your views here.
from pypro.modulos import facade


def detalhe(request, slug):
    modulo = facade.econtrar_modulo(slug)
    return render(request, 'modulos/modulo_detalhe.html', {'modulo': modulo})
