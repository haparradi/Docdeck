from django.shortcuts import render,redirect, get_object_or_404
from django.urls import reverse_lazy
from django.db.models import Q

from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from PacientesApp.models import Paciente, HistoriaClinica, Consulta

from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, UpdateView, DeleteView


from LoginApp.forms import UpdateUserForm, UpdateProfileForm, ChangePasswordForm
from PacientesApp.forms import PatientForm, HistoriaForm, DataTreinoForm

# Create your views here.
@login_required
def index(request):
    consultas = request.user.consulta.all()
               
    return render(request, 'index.html', {'consultas':consultas})
@login_required
def profile(request):
    consultas = request.user.consulta.all()
    user_form = UpdateUserForm(instance=request.user)
    profile_form = UpdateProfileForm(instance=request.user.profile)
    password_form = ChangePasswordForm(request.user)
    return render(request, 'users-profile.html', {'user_form':user_form, 'profile_form':profile_form, 'password_form':password_form,'consultas':consultas})


class HistoryView(ListView, LoginRequiredMixin):
    model = HistoriaClinica
    template_name = 'records.html'
    context_object_name = 'records'
    def get_queryset(self):
        if self.request.user.is_superuser:
            return Paciente.objects.all()
        else:
            user = self.request.user
            return user.paciente.all()
        

class PatientsList(ListView, LoginRequiredMixin):
    model = Paciente
    template_name = 'patients.html'
    context_object_name = 'patients'
    
    def get_queryset(self):
        if self.request.user.is_superuser: 
            return Paciente.objects.all()
        else:
            user = self.request.user
            return user.paciente.all()
    
    
@login_required
def add_patient(request, id):
    if request.method == 'POST':
        patient_form = PatientForm(request.POST)
        date_form = DataTreinoForm(request.POST)
        # historia_form = HistoriaForm(request.POST)
        if patient_form.is_valid() and date_form.is_valid():
            patient_data = patient_form.cleaned_data
            date_data = date_form.cleaned_data
            paciente = Paciente(nombre=patient_data['nombre'],apellido=patient_data['apellido'],documento=patient_data['documento'], domicilio=patient_data['domicilio'],telefono=patient_data['telefono'],email=patient_data['email'],estado_civil=patient_data['estado_civil'],religion=patient_data['religion'])
            paciente.fecha_de_nacimiento= date_data['fecha_de_nacimiento']
            paciente.save()
            paciente.doctor.add(request.user)
            paciente.save()
            # historia = Paciente.historia_clinica(historia=historia_data['historia'])
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
        # try:
        #     historia = get_object_or_404(HistoriaClinica, pk=id)
        #     return render(request, 'patient-detail.html', {'historia':historia})
        # except:
        return render(request, 'patient-detail.html', {'patient':patient})
        
@login_required
def add_history(request, id):
    paciente = Paciente.objects.get(id=id)
    if request.method == 'POST':
        historia_form = HistoriaForm(request.POST)
        if historia_form.is_valid():
            data = historia_form.cleaned_data
            historia = HistoriaClinica(paciente_id = id, historia=data['historia'])
            historia.save()
            return redirect('patients')
        return render(request, 'add-history.html', {'historia_form':historia_form, 'id':id})
    else:
        historia_form = HistoriaForm()
        return render(request, 'add-history.html', {'historia_form':historia_form, 'id':id, 'paciente':paciente})
    
    
class HistoryDetail(DetailView, LoginRequiredMixin):
    model = HistoriaClinica
    template_name = 'history-detail.html'
    context_object_name = 'history'
    
    
class HistoryEdit(UpdateView, LoginRequiredMixin):
    model = HistoriaClinica
    form_class = HistoriaForm
    template_name = 'update-history.html'
    success_url = reverse_lazy('records')
    
# class DeletePatient(DeleteView):
#     model = Paciente
#     template_name = 'delete-patient.html'
#     success_url = reverse_lazy('patients')
@login_required
@require_http_methods(['DELETE'])
def delete_patient(request, pk):
    if request.user.is_superuser:
        patient = Paciente.objects.get(pk=pk)
        patient.delete()
        patients = Paciente.objects.all()
    else:
        patient = request.user.paciente.get(pk = pk)
        patient.delete()
        patients = request.user.paciente.all()
    
    return render(request, 'patients.html', {'patients':patients})

class PatientEdit(UpdateView, LoginRequiredMixin):
    model = Paciente
    form_class = PatientForm
    template_name = 'update-patient.html'
    context_object_name = 'patient_form'
    success_url = reverse_lazy('patients')
    
@login_required
def search_patient(request):
    search_text = request.POST.get('search')

    # look up all patient that contain the text in their first name
    
    if request.user.is_superuser:
        results = Paciente.objects.filter(Q(nombre__icontains=search_text) | Q(apellido__icontains=search_text))
        context = {"results": results}
    else:
        results = request.user.paciente.filter(Q(nombre__icontains=search_text) | Q(apellido__icontains=search_text))
        context = {"results": results}
    return render(request, 'partials/search-results.html', context)

class ConsultasListView(ListView, LoginRequiredMixin):
    model = Consulta
    template_name = 'consultas.html'
    context_object_name = 'consultas'
    
    def get_queryset(self):
        if self.request.user.is_superuser:
            return Consulta.objects.all()
        else:
            user = self.request.user
            return user.consulta.all()
        
@login_required
def consulta_detail(request, pk):
    consulta = Consulta.objects.get(pk=pk)
    consulta.read_constulta()
    return render(request, 'consulta-detail.html', {'consulta':consulta})
    