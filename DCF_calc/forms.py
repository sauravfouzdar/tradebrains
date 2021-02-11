from django import forms


class get_input(forms.Form):
    CompanyName = forms.CharField(label='Company')
    FCF = forms.DecimalField(label='Free Cash Flow(3 year average)', decimal_places=2, min_value = 0)
    MarketCap = forms.DecimalField(label='Market cap', decimal_places=2)
    GrowthRateYear1_5 = forms.DecimalField(label='Growth Rate for Year 1 to 5', decimal_places=2)
    GrowthRateYear6_10 = forms.DecimalField(label='Growth Rate for Year 6 to 10', decimal_places=2)
    SharesOutstanding = forms.DecimalField(label='Total Share Outstanding', decimal_places=2,min_value = 1)
    Debt = forms.DecimalField(label='Total Debt', decimal_places=2)
    Cash = forms.DecimalField(label='Total Cash', decimal_places=2)
    DiscountRate = forms.DecimalField(label='Discount Rate', decimal_places=2)
    TerminalGrowthRate = forms.DecimalField(label='Terminal Growth Rate', decimal_places=2)
    

    