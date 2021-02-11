from django import forms


class SIP(forms.Form):
    PrincipleAmount = forms.IntegerField(label='Amount', max_value=50000,min_value=1)
    TimePeriod = forms.IntegerField(label=' TimePeriod', max_value=35,min_value=1)
    GrowthRate = forms.DecimalField(label='Growth Rate', decimal_places=2,min_value=1)
    

    