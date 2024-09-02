from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

def plantillaPadre (request):
    inicio = get_template('plantillaPadre.html')
    documento = inicio.render({})
    return HttpResponse(documento)

def inicio(request):
    return render(request,'inicio.html')
    
        