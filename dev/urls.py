from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^dev$', views.dev_list, name='dev_list'),
]
