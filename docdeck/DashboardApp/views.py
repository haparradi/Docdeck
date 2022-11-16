from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from PacientesApp.models import Paciente, HistoriaClinica
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from LoginApp.forms import UpdateUserForm, UpdateProfileForm, ChangePasswordForm
from PacientesApp.forms import PatientForm, HistoriaForm, DataTreinoForm

# Create your views here.
@login_required
def index(request):
    return render(request, 'index.html')

def profile(request):
    user_form = UpdateUserForm(instance=request.user)
    profile_form = UpdateProfileForm(instance=request.user.profile)
    password_form = ChangePasswordForm(request.user)
    return render(request, 'users-profile.html', {'user_form':user_form, 'profile_form':profile_form, 'password_form':password_form})

def records(request):
    return render(request, 'records.html')

class PatientsList(ListView):
    model = Paciente
    template_name = 'patients.html'
    context_object_name = 'patients'
    
    
def add_patient(request):
    if request.method == 'POST':
        patient_form = PatientForm(request.POST)
        date_form = DataTreinoForm(request.POST)
        # historia_form = HistoriaForm(request.POST)
        if patient_form.is_valid() and date_form.is_valid():
            patient_data = patient_form.cleaned_data
            date_data = date_form.cleaned_data
            paciente = Paciente(nombre=patient_data['nombre'],apellido=patient_data['apellido'],documento=patient_data['documento'], domicilio=patient_data['domicilio'],telefono=patient_data['telefono'],email=patient_data['email'],estado_civil=patient_data['estado_civil'],religion=patient_data['religion'])
            paciente.fecha_de_nacimiento= date_data['fecha_de_nacimiento']
            # historia = Paciente.historia_clinica(historia=historia_data['historia'])
            paciente.save()
            # historia.save()
            return redirect('index')
        return PatientsList.as_view()
    else:
        patient_form = PatientForm()
        date_form = DataTreinoForm()
        
        return render(request, 'add-patient.html', {'patient_form':patient_form, 'date_form':date_form})
    
    
class PatientDetail(DetailView):
    model = 'Paciente'
    template_name = 'patient-detail.html'
    context_object_name = 'patient'