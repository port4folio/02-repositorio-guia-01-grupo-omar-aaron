from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return HttpResponse("Hola, esta es la vista de inicio")

def perfil(request):
    return HttpResponse("Esta es la vista de perfil")