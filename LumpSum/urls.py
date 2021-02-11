
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    path('Lump-Sum-Calculator', views. LumpSum_Calculator.as_view(), name=' LumpSum_Calculator'),
]