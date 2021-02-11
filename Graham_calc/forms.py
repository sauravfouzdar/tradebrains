from django import forms


class graham_input(forms.Form):
    CurrentSharePrice = forms.DecimalField(label='CurrentSharePrice', decimal_places=2)
    Last4QuartersEPS = forms.DecimalField(label='Last4QuartersEPS', decimal_places=2)
    GrowthRateNext_5_yrs = forms.DecimalField(label='GrowthRateNext_5_yrs', decimal_places=2)
    TenYearIndianGovtBondYield = forms.DecimalField(label='TenYearIndianGovtBondYield', decimal_places=2,min_value = 0.1)
    RepoRate = forms.DecimalField(label='RR', decimal_places=2)

    