from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from database.models import *
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json


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

    new_farm.save()
    # create firebase hook

    serialized_data = json.loads(
        serializers.serialize('json', [new_farm]))[0]["fields"]
    serialized_area_info = [j["fields"] for j in json.loads(serializers.serialize(
        'json', Farm.objects.exclude(name=new_farm.name)))]

    response = {
        "profile": serialized_data,
        "area_info": serialized_area_info
    }

    return JsonResponse(response)


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
    new_alert = Alert(
        farm_name=request.POST.get('name'),
        threat_level=request.POST.get('bio', ''),
        catalog_category=request.POST.get('area', ''),
        specific_threat=request.POST.get('category_id', ''),
    )

    threat_info = [j["fields"] for j in json.loads(serializers.serialize(
        'json', Disease.objects.filter(name=new_alert.specific_threat)))]
    response = {
        "my_alert_info": new_alert.threat_level,
        "alert_response": threat_info
    }
    return JsonResponse({"data": response})


# get disease catalog
@require_http_methods(["GET"])
def get_all_farms(request):
    all_farms = [j["fields"] for j in json.loads(serializers.serialize(
        'json', Farm.objects.all()))]

    return JsonResponse({"data": all_farms})


@require_http_methods(["GET"])
def get_all_crops(request):
    all_crops = [j["fields"] for j in json.loads(serializers.serialize(
        'json', Crop.objects.all()))]

    return JsonResponse({"data": all_crops})


@require_http_methods(["GET"])
def get_all_crop_families(request):
    all_crop_families = [j["fields"] for j in json.loads(serializers.serialize(
        'json', Crop.objects.all()))]

    return JsonResponse({"data": all_crop_families})


def send_alerts():
    pass


# get threats
# get alerts
