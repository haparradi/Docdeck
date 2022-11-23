"""docdeck URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('Records/', views.HistoryView.as_view(), name='records'),
    path('patients/', views.PatientsList.as_view(), name='patients'),
    path('add-patient/<int:id>/', views.add_patient, name='add-patient'),
    path('patient/<int:id>/', views.patient_detail, name='patient-detail'),
    path('add-history/<int:id>/', views.add_history, name='add-history'),
    path('history-details/<pk>/', views.HistoryDetail.as_view(), name='history-detail'),
    path('update-history/<pk>/', views.HistoryEdit.as_view(), name='update-history'),
    path('delete-patient/<pk>/', views.delete_patient, name='delete-patient'),
    path('consultas/', views.ConsultasListView.as_view(), name='consultas'),
    path('consulta-detail/<pk>/', views.consulta_detail, name='consulta-detail'),
    path('update-patient/<pk>/', views.PatientEdit.as_view(), name='update-patient')
]

htmx_urlpatterns = [
    path('search-patient', views.search_patient, name='search-patient')
]

urlpatterns+=htmx_urlpatterns