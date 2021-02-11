
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    path('PE-valuation-Calculator', views.PE_valuation.as_view(), name='PE_valuation'),
]