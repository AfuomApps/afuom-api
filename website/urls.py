from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.welcome_page, name='website_welcome_page'),
]
