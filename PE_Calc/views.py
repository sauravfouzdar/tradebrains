from __future__ import unicode_literals
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from .forms import PE_input 


# Create your views here.
class PE_valuation(TemplateView):
    template_name = 'PE_calc.html'
    #context = {'form':form}
    def get(self, request, *args, **kwargs):
        form = PE_input()
        return render(request, self.template_name,{'form':form})
    
    def post(self, request):
        form = PE_input(request.POST)
        if form.is_valid():
            EPS  = form.cleaned_data['EPS']
            MedianPE = form.cleaned_data['MedianPE']
            GrowthRate = form.cleaned_data['GrowthRate']
            SafetyMargin = form.cleaned_data['SafetyMargin']
            ConservativeGrowthRate = form.cleaned_data['ConservativeGrowthRate']
            GrowthDeclineRate = form.cleaned_data['GrowthDeclineRate']
            DiscountRate = form.cleaned_data['DiscountRate']
            print("YOYOYOY")
            if 'result' in request.POST:
                EPS_Growth_List = []
                for i in range(0,5):
                    if (i == 0):
                        x = EPS*(1+ ConservativeGrowthRate/100)
                        EPS_Growth_List.append(round(x,2))
                    else :
                        x = EPS_Growth_List[len(EPS_Growth_List)-1]*(1+(ConservativeGrowthRate/100)*(pow(1-GrowthDeclineRate/100,i-1)))
                        EPS_Growth_List.append(round(x,2))
                
            print("hello: ",EPS)
            id = len(EPS_Growth_List)-1
            print("Id: ",id)
            ValueInFiveYear = EPS_Growth_List[id]*MedianPE
            IntrinsicValue = round(ValueInFiveYear/pow((1+DiscountRate/100),5),2)
            Year_list = ["1", "2", "3", "4", "5"]
            zipped_data = zip(Year_list, EPS_Growth_List)
        args = {'form': form,'ValueInFiveYear':ValueInFiveYear,'IntrinsicValue':IntrinsicValue,'zipped_data':zipped_data}
        return render(request, self.template_name, args)    
