from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from PacientesApp.models import Paciente, HistoriaClinica
from django.views.generic import ListView
from LoginApp.forms import UpdateUserForm, UpdateProfileForm, ChangePasswordForm
from PacientesApp.forms import PatientForm, HistoriaForm

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
        historia_form = HistoriaForm(request.POST)
        if patient_form.is_valid() and historia_form.is_valid():
            patient_data = patient_form.cleaned_data
            historia_data = historia_form.cleaned_data
            paciente = Paciente(nombre=patient_data['nombre'],apellido=patient_data['apellido'],domicilio=patient_data['domicilio'],telefono=patient_data['telefono'],email=patient_data['email'],estado_civil=patient_data['estado_civil'],religion=patient_data['religion'],fehca_de_nacimiento=patient_data['fehca_de_nacimiento'])
            historia = HistoriaClinica(historia=historia_data['historia'])
            paciente.save()
            historia.save()
            return redirect('index')
        return PatientsList.as_view()
    else:
        patient_form = PatientForm()
        historia_form = HistoriaForm()
        return render(request, 'add-patient.html', {'patient_form':patient_form, 'historia_form':historia_form})