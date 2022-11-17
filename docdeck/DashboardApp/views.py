from django.shortcuts import render,redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from PacientesApp.models import Paciente, HistoriaClinica
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from LoginApp.forms import UpdateUserForm, UpdateProfileForm, ChangePasswordForm
from PacientesApp.forms import PatientForm, HistoriaForm, DataTreinoForm

# Create your views here.
@login_required
def index(request):
    return render(request, 'index.html')
@login_required
def profile(request):
    user_form = UpdateUserForm(instance=request.user)
    profile_form = UpdateProfileForm(instance=request.user.profile)
    password_form = ChangePasswordForm(request.user)
    return render(request, 'users-profile.html', {'user_form':user_form, 'profile_form':profile_form, 'password_form':password_form})
@login_required
def records(request):
    return render(request, 'records.html')

class PatientsList(ListView, LoginRequiredMixin):
    model = Paciente
    template_name = 'patients.html'
    context_object_name = 'patients'
    
@login_required    
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
    
    
# class PatientDetail(DetailView):
#     model = 'Paciente'
#     template_name = 'patient-detail.html'
#     context_object_name = 'patient'
@login_required
def patient_detail(request, id): 
    if request.method == 'GET':
        patient = Paciente.objects.get(id=id)
        try:
            historia = get_object_or_404(HistoriaClinica, pk=id)
            return render(request, 'patient-detail.html', {'historia':historia})
        except:
            return render(request, 'patient-detail.html', {'patient':patient})
@login_required
def add_history(request, id):
    if request.method == 'POST':
        historia_form = HistoriaForm(request.POST)
        if historia_form.is_valid():
            data = historia_form.cleaned_data
            historia = HistoriaClinica(paciente_id = id, historia=data['historia'])
            historia.save()
            return redirect('patients')
        return render(request, 'add-history.html', {'historia_form':historia, 'id':id})
    else:
        historia_form = HistoriaForm()
        return render(request, 'add-history.html', {'historia_form':historia_form, 'id':id})
    
    
class HistoryDetail(DetailView, LoginRequiredMixin):
    model = HistoriaClinica
    template_name = 'history-detail.html'
    context_object_name = 'history'