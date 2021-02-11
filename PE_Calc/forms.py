from django import forms


class PE_input(forms.Form):
    EPS = forms.DecimalField(label ='EPS last 4 quarters', decimal_places=2)
    MedianPE = forms.DecimalField(label ='Median PE last 5 Years', decimal_places=2)
    GrowthRate = forms.DecimalField(label ='Expected growth rate', decimal_places=2)
    SafetyMargin  = forms.DecimalField(label ='Margin of Safety', decimal_places=2)
    ConservativeGrowthRate = forms.DecimalField(label ='Conservative Growth Rate', decimal_places=2)
    GrowthDeclineRate = forms.DecimalField(label ='Growth Decline Rate', decimal_places=2)
    DiscountRate = forms.DecimalField(label ='Discount Rate', decimal_places=2)