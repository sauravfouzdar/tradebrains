
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    path('ROE-valuation-Calculator', views.ROE_valuation.as_view(), name='ROE_valuation'),
]