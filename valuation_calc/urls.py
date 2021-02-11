
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    path('', views.index, name ='index'),
    path('disclaimer', views.disclaimer, name='disclaimer'),
    path('Terms-and-Conditions', views.termsConditions, name='termsConditions'),
    path('Dhandho-valuation-Calculator', views.valuation_calc.as_view(), name='valuation_calc'),
    
]