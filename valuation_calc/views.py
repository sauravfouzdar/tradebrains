from __future__ import unicode_literals
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from .forms import get_input 


# Create your views here.
def index(request):
    context = {}
    template_name = 'index.html'

    return render(request,template_name,context)
    
def disclaimer(request):
    context = {}
    template_name = 'disclaimer.html'

    return render(request,template_name,context)

def termsConditions(request):
    context = {}
    template_name = 'Terms-conditions.html'

    return render(request,template_name,context)
    
class valuation_calc(TemplateView):
    template_name = 'valuation_calc.html'
    #context = {'form':form}
    def get(self, request, *args, **kwargs):
        form = get_input()
        return render(request, self.template_name,{'form':form})
    
    def post(self, request):
        form = get_input(request.POST or None)
        if form.is_valid():
             # lookup 
            # ij i StockDetail
            #if i=="input":
                #######:
            GrowthRateYear1_3 = form.cleaned_data['GrowthRateYear1_3']
            GrowthRateYear4_6 = form.cleaned_data['GrowthRateYear4_6']
            GrowthRateYear7_10 = form.cleaned_data['GrowthRateYear7_10']
            DiscountRate = form.cleaned_data['DiscountRate']
            FCF = form.cleaned_data['Current_FCF']
            MarketCap = form.cleaned_data['MarketCap']
            CompanyName = form.cleaned_data['CompanyName']
            TerminalMultiple = form.cleaned_data['TerminalRate']
            PVofFCF = form.cleaned_data['PVofFCF']
           

            if 'result' in request.POST:
                FreeCashFlowList = []
                PVofFreeCashFlowList = []
                for i in range(0,10):
                    if (i <=2) :
                        x = (FCF*pow(1+ GrowthRateYear1_3/100,i+1))
                        FreeCashFlowList.append(round(x, 2))
                        y =  x/pow(1+DiscountRate/100,i+1)
                        PVofFreeCashFlowList.append(round(y,2))
                    elif (i>2 and i<=5) :
                        
                            temp = FreeCashFlowList[i-1] 
                            #print("temp: ",temp)
                            x = temp*(1+ GrowthRateYear4_6/100)
                            #print("x: ", x)
                            FreeCashFlowList.append(round(x,2))
                            y = x/pow(1+DiscountRate/100,i+1)
                            PVofFreeCashFlowList.append(round(y,2))
                            #temp = (FCF*pow(1+ GrowthRateYear1_3/100,3)
                    else :
                        temp = FreeCashFlowList[i-1]
                        x = temp*(1+ GrowthRateYear7_10/100)
                        FreeCashFlowList.append(round(x, 2))
                        y = (x/pow(1+DiscountRate/100,i+1))
                        PVofFreeCashFlowList.append(round(y,2))     
    
            form = get_input()
            IV = 0
            for i in range(0,10):
                IV += PVofFreeCashFlowList[i]
 
            IV += 15*PVofFreeCashFlowList[9] + PVofFCF
            print("Intrinsic Value: ", IV)    
            Diff = IV - MarketCap
            Difference = round(MarketCap/IV -1,2)
            Difference*=100
            print("Diff : ",Difference)
            Year_list = ["1", "2", "3", "4", "5", "6", "7", "8","9", "10"]
            zipped_data = zip(Year_list, FreeCashFlowList, PVofFreeCashFlowList)
        args = {'form': form,'zipped_data':zipped_data,'IV':IV,'Difference':Difference,'PVofFCF':PVofFCF,'FCF':FCF}
        return render(request, self.template_name, args)    
