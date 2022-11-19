from .models import Consulta
from .forms import ConsultaForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView
# Create your views here.
# class EnviarConsulta(FormView):
#     form_class = ConsultaForm
#     template_name = 'contact.html'
#     success_url = reverse_lazy('contact')

def enviar_consulta(request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        print(form['doctor'])
        if form.is_valid():
            data = form.cleaned_data
            consulta = Consulta.objects.create(nombre_apellido=data['nombre_apellido'], email=data['email'],consulta=data['consulta'], doctor_id=data['doctor'].id)
            consulta.save
            response = 'Consulta Enviada!'
            return render(request,'contact.html', {'response':response})
        return render(request,'contact.html', {'form':form, 'response':'Formulario Invalido'})
    else:
        form = ConsultaForm()
        return render(request, 'contact.html', {'form':form})