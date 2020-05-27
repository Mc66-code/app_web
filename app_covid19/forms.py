
from django import forms

class NouveauPassionForm(forms.Form):
    #nom = forms.CharField()
    photo = forms.ImageField()