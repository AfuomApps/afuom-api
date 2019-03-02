from django.shortcuts import render
from django.http import JsonResponse


def api_welcome_page(request):
    return JsonResponse({'team': 'Afuom', 'message': 'We are the coolest team!!!'})


def locations(request):
    return JsonResponse({"locations": [
        {
            "alert": "yellow",
            "threat": "rodents",
            "longitude": -46.818894,
            "latitude": -23.007798,
        },
        {
            "alert": "green",
            "threat": "rodents",
            "longitude": -46.821657,
            "latitude": -23.007268
        },
        {
            "alert": "red",
            "threat": "red spots disease",
            "longitude": -46.815429,
            "latitude": -23.007696,
        },
    ]})
