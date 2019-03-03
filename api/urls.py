from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.api_welcome_page, name='api_welcome_page'),
    url(r'^register$', views.post_registration, name='post_registration'),
    url(r'^post/register$', views.post_registration, name='post_registration'),

    url(r'^get/allfarms$', views.get_all_farms, name='allfarms'),
    url(r'^get/allcrops$', views.get_all_crops, name='allcrops'),
    url(r'^get/allcropfamilies$', views.get_all_crop_families, name='allcropfamilies'),

    url(r'^locations$', views.locations, name='locations'),
]
