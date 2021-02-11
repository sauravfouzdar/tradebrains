from __future__ import unicode_literals
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from .forms import SIP 



# Create your views here.
class SIP_Calculator(TemplateView):
    template_name = 'SIP.html'
    
    def get(self, request, *args, **kwargs):
        form = SIP()
        return render(request, self.template_name,{'form':form})
    
    def post(self, request):
        form = SIP(request.POST)
        if form.is_valid():
            Amount = form.cleaned_data['PrincipleAmount']
            Time = form.cleaned_data['TimePeriod']
            GrowthRate = form.cleaned_data['GrowthRate']
            
            if 'SIP' in request.POST:
                print("Working")
                CompoundedRate = GrowthRate/1200
                multi = pow(1+CompoundedRate,Time*12)
                MaturityAmount = (Amount*(multi-1)*(1+CompoundedRate))/CompoundedRate
                x = round(MaturityAmount,2) 
                
                
            
            
            form = SIP()

        args = {'form': form, 'x':x}
        return render(request, self.template_name, args)    
