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

def reset(request):
    reset = request.POST['reset']
    if reset == 'reset':
        request.session['monedas'] = 0
        request.session['jugadas'] = []
    return redirect('/')

def process_money(request):

    origen = request.POST['origen']
    min = int(request.POST['min'])
    max = int(request.POST['max'])

    resultado = randrange(min, max)
    request.session['monedas'] += resultado
    # jugada = "ganaste %s monedas en %s" % (resultado, origen)
    jugada = f"ganaste {resultado} monedas en {origen}"
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