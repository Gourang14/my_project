# forms.py
from django import forms

class PredictionForm(forms.Form):
    B_Req = forms.FloatField(label='B_Req')
    Weights = forms.FloatField(label='Weights')
    Complexity = forms.FloatField(label='Complexity')
    Cost = forms.FloatField(label='Cost')
