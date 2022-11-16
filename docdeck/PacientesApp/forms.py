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
    class Meta:
        model = HistoriaClinica
        fields = ['historia']