from django import forms
from .models import *

class FormaSok(forms.Form):
    all = Company.objects.all()
    mas = []
    for a in all:
        mas.append((a.id, a.title))
    print(mas)
    #firma = forms.ModelChoiceField(all.filter(title='J7'))
    firma = forms.ModelChoiceField(Company.objects.all(), required=False)
    sok = forms.ModelChoiceField(Product.objects.all(), required=False)

class FormaUser(forms.Form):
    user = forms.ModelChoiceField(User.objects.all())