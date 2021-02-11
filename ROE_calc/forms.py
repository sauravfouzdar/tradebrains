from django import forms

class ROE_input(forms.Form):
    ShareholdersEquity = forms.DecimalField(label='Shareholder Equity', decimal_places=2)
    Price = forms.DecimalField(label='Price of Stock', decimal_places=2)
    ReturnOnEquity = forms.DecimalField(label='Return on Equity 3 Years Average', decimal_places=2)
    SharesOutstanding = forms.DecimalField(label='Total Shares Outstanding', decimal_places=2)
    DividendYield = forms.DecimalField(label='Dividend Yield', decimal_places=2)
    DividendPayoutRatio = forms.DecimalField(label='Dividend Payout Ratio', decimal_places=2)
    SafetyMargin = forms.DecimalField(label='Margin of Safety', decimal_places=2)
    ConservativeGrowthRate = forms.DecimalField(label='Conservative Growth Rate', decimal_places=2)
    DiscountRate = forms.DecimalField(label='Discount Rate', decimal_places=2)


    