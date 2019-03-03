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
@csrf_exempt
def post_alert(request):
    """
    req-----
    picture
    crop info
    threat_group: whch one? weed, insect, disease?
    catalog_category: from disease catalog


    respo -----
    threat_deatials: level, symptoms, treatments, preventions
    threat_level
    """
    print(request.POST)

    new_alert = Alert(
        farm_name=Farm.objects.get(
            name__icontains=request.POST.get('farm_name', '')),
        threat_level=ThreatType.objects.get(
            severity=request.POST.get('threat_level', 'HIGH')),
        catalog_category=Disease.objects.filter(
            name=request.POST.get('catalog_category', '')),
        threat_group=request.POST.get('specific_threat', 'disease'),
        description=request.POST.get('description', '')
    )

    # print(new_alert)
    # new_file = Image(name="reportedImageFrom" +
    #                  new_alert.farm_associated.name, file=request.POST["picture"])

    threat_info = [j["fields"] for j in json.loads(serializers.serialize(
        'json', Disease.objects.filter(name=new_alert.specific_threat)))]
    response = {
        "my_alert_info": new_alert.threat_level,
        "alert_response": threat_info
    }
    return JsonResponse({"data": response})


@require_http_methods(["GET"])
def get_all_farms(request):
    all_farms = [j["fields"] for j in json.loads(serializers.serialize(
        'json', Farm.objects.all()))]

    return JsonResponse({"data": all_farms})


@require_http_methods(["GET"])
def get_all_farms_2(request):
    json_data = json.loads(serializers.serialize(
        'json', Farm.objects.all()))

    for p in json_data:
        print(p)

    all_farms = [
        {
            "name": j["fields"]["name"],
            "bio": j["fields"]["bio"],
            "area": j["fields"]["area"],
            "longitude": j["fields"]["location"]["longitude"],
            "latitude": j["fields"]["location"]["latitude"],
            "crops": j["fields"]["crops_grown"]["crops"],
            "interested_in_selling": j["fields"]["interested_in_selling"],
            "contact": j["fields"]["contact"]["phone"]
        } for j in json_data
    ]

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
