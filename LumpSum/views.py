from __future__ import unicode_literals
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from .forms import LumpSum 



# Create your views here.
class LumpSum_Calculator(TemplateView):
    template_name = 'LumpSum.html'
    
    def get(self, request, *args, **kwargs):
        form = LumpSum()
        return render(request, self.template_name,{'form':form})
    
    def post(self, request):
        form = LumpSum(request.POST)
        if form.is_valid():
            Amount = form.cleaned_data['PrincipleAmount']
            Time = form.cleaned_data['TimePeriod']
            GrowthRate = form.cleaned_data['GrowthRate']
            
            if 'LumpSum' in request.POST:
                print("Working")
                multi = pow(1+GrowthRate/100,Time)
                MaturityAmount = round(Amount*multi,2) 
                
                
            
            
            form = LumpSum()

        args = {'form': form, 'MaturityAmount':MaturityAmount}
        return render(request, self.template_name, args)    
