from __future__ import unicode_literals
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from .forms import graham_input 



# Create your views here.
class graham(TemplateView):
    template_name = 'graham_calc.html'
    
    def get(self, request, *args, **kwargs):
        form = graham_input()
        return render(request, self.template_name,{'form':form})
    
    def post(self, request):
        form = graham_input(request.POST)
        if form.is_valid():
            CurrentSharePrice = form.cleaned_data['CurrentSharePrice']
            Last4QuartersEPS = form.cleaned_data['Last4QuartersEPS']
            GrowthRateNext_5_yrs = form.cleaned_data['GrowthRateNext_5_yrs']
            TenYearIndianGovtBondYield = form.cleaned_data['TenYearIndianGovtBondYield']
            RepoRate = form.cleaned_data['RepoRate']
            if 'grahamresult' in request.POST:
                print("Working Graham")
                x = round((Last4QuartersEPS*(7 + GrowthRateNext_5_yrs)*RepoRate)/TenYearIndianGovtBondYield,2)
                
            
            
            form = graham_input()

        args = {'form': form, 'x':x}
        return render(request, self.template_name, args)    
