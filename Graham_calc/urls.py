from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    path('Graham-valuation-Calculator', views.graham.as_view(), name='graham'),
    
]
