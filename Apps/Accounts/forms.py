from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from .models import *


class EstudianteForm(ModelForm):
    class Meta:
        model = Estudiante
        fields = '__all__'
        exclude = ['domicilio', 'user']

    def __init__(self, *args, **kwargs):
        super(EstudianteForm, self).__init__(*args, **kwargs)
        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input'


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input'


class DomicilioForm(ModelForm):
    class Meta:
        model = Domicilio
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(DomicilioForm, self).__init__(*args, **kwargs)
        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input'


class ExpedienteForm(ModelForm):
    class Meta:
        model = Expediente
        fields = '__all__'
        #exclude = ['reporteParcial1', 'reporteParcial2', 'reporteFinal']

    def __init__(self, *args, **kwargs):
        super(ExpedienteForm, self).__init__(*args, **kwargs)
        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input'


class Reporte1Form(ModelForm):
    class Meta:
        model = ReporteParcial1
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super(Reporte1Form, self).__init__(*args, **kwargs)        
        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input'
        #self.fields['reporteDoc'].widget.attrs['name'] = 'reporte1Doc'
        #self.fields['reporteDoc'].label = "reporte1Doc"


class Reporte2Form(ModelForm):
    class Meta:
        model = ReporteParcial2
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(Reporte2Form, self).__init__(*args, **kwargs)
        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input'
        #self.fields['reporteDoc'].widget.attrs['name'] = 'reporte2Doc'


class ReporteFinalForm(ModelForm):
    class Meta:
        model = ReporteFinal
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ReporteFinalForm, self).__init__(*args, **kwargs)
        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input'
        #self.fields['reporteDocFinal'].widget.attrs['name'] = 'reporteFDoc'

class DocenteForm(ModelForm):
    class Meta:
        model = Docente
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(DocenteForm, self).__init__(*args, **kwargs)
        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input'
            
class AnteproyectoEstForm(ModelForm):
    class Meta:
        model = Anteproyecto
        fields = '__all__'
        exclude = ['docente']
        labels = {
            'nombre': 'Nombre del Anteproyecto',
            'tipoProyecto': 'Tipo de Proyecto',
            'fechaEntrega': 'Fecha de entrega',
            'numIntegrantes': 'Numero de integrantes',            
        }

    def __init__(self, *args, **kwargs):
        super(AnteproyectoEstForm, self).__init__(*args, **kwargs)
        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input'
            
class AnteproyectoForm(ModelForm):
    class Meta:
        model = Anteproyecto
        fields = '__all__'
        

    def __init__(self, *args, **kwargs):
        super(AnteproyectoForm, self).__init__(*args, **kwargs)
        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input'            
            
                        