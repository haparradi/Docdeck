from django import forms

from django.contrib.admin.widgets import AdminDateWidget   
from .models import Paciente, HistoriaClinica

class PatientForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nombre','apellido', 'documento','domicilio','telefono','email','estado_civil','religion']

class DateInput(forms.DateInput):
    input_type = 'date'
        
class DataTreinoForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['fecha_de_nacimiento']
        widgets = {
            'dateField': DateInput
        }


class HistoriaForm(forms.ModelForm):
    historia = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    class Meta:
        model = HistoriaClinica
        fields = ['historia']
        labels = {'historia':'Historia Clinica'}
        