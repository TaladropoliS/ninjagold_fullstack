from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
# import random
from random import randrange
# Create your views here.

def inicio(request):
    if 'monedas' not in request.session.keys():
        request.session['monedas'] = 0
    if 'jugadas' not in request.session.keys():
        request.session['jugadas'] = []
    return render(request, 'index.html')

def process_money(request):
    origen = request.POST['origen']
    min = int(request.POST['min'])
    max = int(request.POST['max'])

    resultado = randrange(min, max)
    request.session['monedas'] += resultado
    jugada = "ganaste %s monedas en %s" % (resultado, origen)
    request.session['jugadas'].append(jugada)
    context = {
        'resultado': resultado,
        'juego': origen
    }
    return redirect('/')

    # return JsonResponse({
    #     'origen': origen,
    #     'min': min,
    #     'max': max
    # })

def granja(request):
    juego = request.POST['juego']
    # if juego == 'granja':
    resultado = randrange(10, 20)
    request.session['monedas'] += resultado
    context = {
        'resultado':resultado,
        'juego': granja
    }
    return render(request, 'index.html', context)

def cueva(request):
    resultado = randrange(5, 10)
    request.session['monedas'] += resultado
    context = {
        'resultado': resultado,
    }
    return render(request, 'index.html', context)

def casa(request):
    resultado = randrange(2, 5)
    request.session['monedas'] += resultado
    context = {
        'resultado': resultado
    }
    return render(request, 'index.html', context)

def casino(request):
    resultado = randrange(-50, 50)
    request.session['monedas'] += resultado
    context = {
        'resultado': resultado
    }
    return render(request, 'index.html', context)
