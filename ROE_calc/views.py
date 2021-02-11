from __future__ import unicode_literals
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from .forms import ROE_input 


# Create your views here.
class ROE_valuation(TemplateView):
    template_name = 'ROE_calc.html'
    #context = {'form':form}
    def get(self, request, *args, **kwargs):
        form = ROE_input()
        return render(request, self.template_name,{'form':form})
    
    def post(self, request):
        form = ROE_input(request.POST)
        if form.is_valid():
            ShareholdersEquity  = form.cleaned_data['ShareholdersEquity']
            Price = form.cleaned_data['Price']
            ROE = form.cleaned_data['ReturnOnEquity']
            SafetyMargin = form.cleaned_data['SafetyMargin']
            ConservativeGrowthRate = form.cleaned_data['ConservativeGrowthRate']
            DividendYield = form.cleaned_data['DividendYield']
            DiscountRate = form.cleaned_data['DiscountRate']
            SharesOutstanding = form.cleaned_data['SharesOutstanding']
            DividendPayoutRatio = form.cleaned_data['DividendPayoutRatio']
            if 'result' in request.POST:
                #print("works ROE")
                ShareHolders_Equity_List = []
                Dividend_List = []
                NPV_dividend_List = []
                for i in range(0,10):
                    if (i == 0):
                        x = (ShareholdersEquity*(1+ ConservativeGrowthRate/100))/SharesOutstanding
                        ShareHolders_Equity_List.append(round(x,2))
                        y = (Price*DividendYield/100)*(1+ ConservativeGrowthRate/100)
                        Dividend_List.append(round(y,2))
                        NPV_dividend_List.append(round(y,2))
                    else :
                        x = x*(1+ ConservativeGrowthRate/100)
                        ShareHolders_Equity_List.append(round(x,2))
                        y  = Dividend_List[i-1]*(1+ ConservativeGrowthRate/100)
                        Dividend_List.append(round(y,2))
                        z = y/(pow((1 + DiscountRate/100),i))
                        NPV_dividend_List.append(round(z,2))
            
            id = len(ShareHolders_Equity_List)-1
            #print("Id : ",id)
            Year_10_Net_Income = round((ShareHolders_Equity_List[id]*ROE)/100,2)
            Required_Value = round((Year_10_Net_Income*100)/DiscountRate,2)
            NPV_RequiredValue = round(Required_Value/(pow((1+ DiscountRate/100),10)),2)
            sum = 0
            for i in range(0,10):
                sum += NPV_dividend_List[i]
      
            NPV_Dividend = round(sum,2)
            Intrinsic_Value = NPV_RequiredValue + NPV_Dividend
            # print("Required_Value:  ",Required_Value)
            # print("Year_10_Net_Income: ",Year_10_Net_Income)
            # print("NPV_RequiredValue: ",NPV_RequiredValue)
            #print("NPV_Dividend: ",NPV_Dividend)
            #print("Intrinsic Value: ",Intrinsic_Value)
            Year_list = ["1", "2", "3", "4", "5", "6", "7", "8","9", "10"]
            zipped_data = zip(Year_list, ShareHolders_Equity_List, Dividend_List, NPV_dividend_List)
        args = {'form': form,'ShareHolders_Equity_List':ShareHolders_Equity_List,
        'Dividend_List':Dividend_List,'NPV_dividend_List':NPV_dividend_List,
        'NPV_dividend_List':NPV_dividend_List,'Required_Value':Required_Value,
        'NPV_RequiredValue':NPV_RequiredValue,'Year_10_Net_Income':Year_10_Net_Income,
        'Intrinsic_Value':Intrinsic_Value,'zipped_data':zipped_data}
        return render(request, self.template_name, args)    
