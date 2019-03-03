from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from database.models import *
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers


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


@require_http_methods(["POST"])
@csrf_exempt
def post_registration(request):
    """
    request:
    {
        "name": "Sam's Farm",
        "bio": "Sams bio",
        "area": "Ithaca",
        "location": "Tompkins"
        "crops_grown": [{"cocoa": }],
        "interested_in_selling":""
        "contact": {
            "phone": ""
        }
    }

    response:
    their profile:
    area map : what others are growing around them

    """
    new_farm = Farm(
        name=request.POST.get('name'),
        bio=request.POST.get('bio'),
        area=int(request.POST.get('area', 10)),
        location={
            "latitude": request.POST.get('longitude', '0.000'),
            "longitude": request.POST.get('latitude', '0.000')
        },
        crops_grown=request.POST.get('crops_grown'),
        interested_in_selling=bool(
            request.POST.get('interested_in_selling', True)),
        contact={"phone": request.POST.get('phone')}
    )
    p = new_farm.save()
    print(p)

    v = serializers.serialize('json', [new_farm])
    print(v)
    response = {
        "profile": v,
        "area_info": []
    }
    # print(request.POST)
    return JsonResponse({"status": "success"})


@require_http_methods(["POST"])
def post_alert(request):
    """
    req-----
    picture
    crop info
    threat: whch one? weed, insect, disease?
    specific_threat: from disease catalog


    respo -----
    threat_deatials: level, symptoms, treatments, preventions
    threat_level
    """
    pass


# get disease catalog
