from datetime import date
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from .models import *

class AnteproyectoEstadoForm(ModelForm):
    class Meta:
        model = Anteproyecto
        fields = ['estatus']
        labels = {
            'estatus': ''
        }
    
    def __init__(self, *args, **kwargs):
        super(AnteproyectoEstadoForm, self).__init__(*args, **kwargs)
        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input'
            
class ExpedienteEstadoForm(ModelForm):
    class Meta:
        model = Expediente
        fields = ['estatus']
        labels = {
            'estatus': ''
        }
    
    def __init__(self, *args, **kwargs):
        super(ExpedienteEstadoForm, self).__init__(*args, **kwargs)
        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input'        
            
class ResidenciaEstadoForm(ModelForm):
    class Meta:
        model = Residencia
        fields = ['estatus']
        labels = {
            'estatus': ''
        }
    
    def __init__(self, *args, **kwargs):
        super(ResidenciaEstadoForm, self).__init__(*args, **kwargs)
        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input'            