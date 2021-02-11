from django import forms


class LumpSum(forms.Form):
    PrincipleAmount = forms.IntegerField(label='Amount')
    TimePeriod = forms.IntegerField(label=' TimePeriod', max_value=50)
    GrowthRate = forms.DecimalField(label='Growth Rate', decimal_places=2)
    

    