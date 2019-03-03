from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.api_welcome_page, name='api_welcome_page'),
    url(r'^register$', views.post_registration, name='post_registration'),
    url(r'^locations$', views.locations, name='locations'),
]
