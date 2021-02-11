from django import forms


class get_input(forms.Form):
    CompanyName = forms.CharField(label='Company')
    Current_FCF = forms.DecimalField(label='Free Cash Flow', decimal_places=2, min_value = 0)
    MarketCap = forms.DecimalField(label='Market cap', decimal_places=2)
    GrowthRateYear1_3 = forms.DecimalField(label='Growth Rate for Year 1 to 3', decimal_places=2)
    GrowthRateYear4_6 = forms.DecimalField(label='Growth Rate for Year 4 to 6', decimal_places=2)
    GrowthRateYear7_10 = forms.DecimalField(label='Growth Rate for Year 7 to 10', decimal_places=2)
    DiscountRate = forms.DecimalField(label='Discount Rate', decimal_places=2)
    TerminalRate = forms.DecimalField(label='Terminal Rate', decimal_places=2)
    PVofFCF = forms.DecimalField(label='PV of FCF', decimal_places=2, min_value = 0)

    