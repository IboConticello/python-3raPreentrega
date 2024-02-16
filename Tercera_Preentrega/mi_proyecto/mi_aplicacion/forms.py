from django import forms
from .models import ClaseA, ClaseB, ClaseC

class ClaseAForm(forms.ModelForm):
    class Meta:
        model = ClaseA
        fields = ['campo_a']

class ClaseBForm(forms.ModelForm):
    class Meta:
        model = ClaseB
        fields = ['campo_b']

class ClaseCForm(forms.ModelForm):
    class Meta:
        model = ClaseC
        fields = ['campo_c']
