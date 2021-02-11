
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    path('DCF-valuation-Calculator', views.DCF.as_view(), name='DCF'),
   
]