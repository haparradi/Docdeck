from django import forms 
from django.contrib.admin.widgets import AdminDateWidget   
from .models import Paciente, HistoriaClinica

class PatientForm(forms.ModelForm):
    fehca_de_nacimiento = forms.DateField(widget = forms.SelectDateWidget())
    class Meta:
        model = Paciente
        fields = ['nombre','apellido','domicilio','telefono','email','estado_civil','religion','fehca_de_nacimiento']


class HistoriaForm(forms.ModelForm):
    class Meta:
        model = HistoriaClinica
        fields = ['historia']