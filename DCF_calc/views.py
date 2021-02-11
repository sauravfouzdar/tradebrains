from __future__ import unicode_literals
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from .forms import get_input 


# Create your views here.
class DCF(TemplateView):
    template_name = 'DCF_calc.html'
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
            GrowthRateYear1_5 = form.cleaned_data['GrowthRateYear1_5']
            GrowthRateYear6_10 = form.cleaned_data['GrowthRateYear6_10']
            Debt = form.cleaned_data['Debt']
            Cash = form.cleaned_data['Cash']
            DiscountRate = form.cleaned_data['DiscountRate']
            FCF = form.cleaned_data['FCF']
            MarketCap = form.cleaned_data['MarketCap']
            SharesOutstanding = form.cleaned_data['SharesOutstanding']
            CompanyName = form.cleaned_data['CompanyName']
            TerminalGrowthRate = form.cleaned_data['TerminalGrowthRate']
            DiscountRate = form.cleaned_data['DiscountRate']
           

            if 'result' in request.POST:
                FreeCashFlowList = []
                PVofFreeCashFlowList = []
                DiscountList = []
                for i in range(0,10):

                    if(i<5):
                        x = GrowthRateYear1_5
                        DiscountList.append(round(x,2))
                        if i==0:
                          y = FCF + FCF*(GrowthRateYear1_5/100)
                          FreeCashFlowList.append(round(y,2))
                          
                          z = FreeCashFlowList[i]/(pow(1+DiscountRate/100,i+1))
                          PVofFreeCashFlowList.append(round(z,2))
                        else :
                          y = FreeCashFlowList[i-1] + FreeCashFlowList[i-1]*(GrowthRateYear1_5/100)  
                          FreeCashFlowList.append(round(y,2))
                          z = FreeCashFlowList[i]/(pow(1+DiscountRate/100,i+1))
                          PVofFreeCashFlowList.append(round(z,2))
                    else :
                      x = GrowthRateYear6_10  
                      DiscountList.append(round(x,2))
                      y = FreeCashFlowList[i-1] + FreeCashFlowList[i-1]*(GrowthRateYear6_10/100)
                      FreeCashFlowList.append(round(y,2))
                      z = FreeCashFlowList[i]/(pow(1+DiscountRate/100,i+1))
                      PVofFreeCashFlowList.append(round(z,2))       


    
            form = get_input()
            TerminalYearCF = FreeCashFlowList[9]*(TerminalGrowthRate/100) + FreeCashFlowList[9]
            sum = 0
            for i in range(0,10):
                sum += PVofFreeCashFlowList[i]

            Total_NPV_Year1_10 = round(sum,2) 
            TerminalValue = round(((TerminalYearCF)/((DiscountRate - TerminalGrowthRate)/100))/(pow(1 + DiscountRate/100,10)),2)
            TotalPVofCashflow = round(TerminalValue + Total_NPV_Year1_10,2)
            CompanyValue = round(TotalPVofCashflow + Cash - Debt,2)
            IntrinsicValue = round(CompanyValue/SharesOutstanding,2)
            #######
            print("TerminalYearCFC: ",TerminalYearCF)
            print("Total NPV: ",Total_NPV_Year1_10)
            print("Terminal value: ",TerminalValue)
            print("Total PV of Cashflow: ",TotalPVofCashflow)
            print("Value: ",CompanyValue)
            print("Intrinsic Value: ",IntrinsicValue)
            Year_list = ["1", "2", "3", "4", "5", "6", "7", "8","9", "10"]
            zipped_data = zip(Year_list, FreeCashFlowList,DiscountList, PVofFreeCashFlowList)
        args = {'form': form,'zipped_data':zipped_data,'Debt':Debt, 'Cash':Cash,'TerminalYearCF':TerminalYearCF,'Total_NPV_Year1_10':Total_NPV_Year1_10,'TerminalValue':TerminalValue,'TotalPVofCashflow':TotalPVofCashflow,'CompanyValue':CompanyValue,'IntrinsicValue':IntrinsicValue}
        return render(request, self.template_name, args)    
