
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    path('SIP-Calculator', views.SIP_Calculator.as_view(), name='SIP_Calculator'),
]