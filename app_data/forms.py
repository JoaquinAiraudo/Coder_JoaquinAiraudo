from django import forms
from app_data.models import Presidente, Ministro, Partido

class Form_Presidente(forms.ModelForm):
    class Meta:
        model = Presidente
        fields = '__all__'
        widgets = {'asume_cargo': forms.DateInput(attrs={'type':'Date'}), 'deja_cargo': forms.DateInput(attrs={'type':'Date'})}

class Form_Ministro(forms.ModelForm):
    class Meta:
        model = Ministro
        fields = '__all__'
        widgets = {'asume_cargo': forms.DateInput(attrs={'type':'Date'}), 'deja_cargo': forms.DateInput(attrs={'type':'Date'})}

class Form_Partido(forms.ModelForm):
    class Meta:
        model = Partido
        fields = '__all__'
        widgets = {'fundacion': forms.DateInput(attrs={'type':'Date'})}