from django.shortcuts import render
from django.http import JsonResponse


def api_welcome_page(request):
    return JsonResponse({'team': 'Afuom', 'message': 'We are the coolest team!!!'})
