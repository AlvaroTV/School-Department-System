from datetime import date
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from .models import *


class EstudianteForm(ModelForm):
    class Meta:
        model = Estudiante
        fields = '__all__'
        exclude = ['domicilio', 'user', 'expediente', 'anteproyecto', 'residencia', 'numControl']
        labels = {
            'nombre': 'Nombre(s)',
            'apellidoP': 'Apellido Paterno',
            'apellidoM': 'Apellido Materno',
            'numCelular': 'Numero de celular',
            'numControl': 'Numero de control',                  
        }

    def __init__(self, *args, **kwargs):
        super(EstudianteForm, self).__init__(*args, **kwargs)
        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input'


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'username': 'Numero de control',
            'email': 'Correo institucional',
            'password1': 'Password'            
        }
        
    def clean_email(self):
        data = self.cleaned_data['email']
        domain = data.split('@')[1]
        domain_list = ["itoaxaca.edu.mx", "hotmail.com",]
        if domain not in domain_list:
            raise forms.ValidationError("Solo se acepta el correo institucional")
        return data
        
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
            
class DomicilioViewForm(ModelForm):
    class Meta:
        model = Domicilio
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(DomicilioViewForm, self).__init__(*args, **kwargs)
        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input'        
            self.fields[myField].widget.attrs['disabled'] = True

class ExpedienteForm(ModelForm):
    class Meta:
        model = Expediente
        fields = '__all__'
        exclude = ['reporteParcial1', 'reporteParcial2', 'reporteFinal']
        labels = {
            'solicitudResidencia': 'Solicitud Residencia',
            'cartaPresentacion': 'Carta Presentacion',
            'cartaCompromiso': 'Carta Compromiso',
            'cartaAceptacion': 'Carta Aceptacion',
            'constanciaTerminacion': 'Constancia Terminacion',            
            'actaCalificaciones': 'Acta Calificaciones',            
            'cartaTerminacion': 'Carta Terminacion',            
            'actaResidencia': 'Acta Residencia',            
        }

    def __init__(self, *args, **kwargs):
        super(ExpedienteForm, self).__init__(*args, **kwargs)
        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input'
            
class ExpedienteViewForm(ModelForm):
    class Meta:
        model = Expediente
        fields = '__all__'
        exclude = ['reporteParcial1', 'reporteParcial2', 'reporteFinal']
        labels = {
            'solicitudResidencia': 'Solicitud Residencia',
            'cartaPresentacion': 'Carta Presentacion',
            'cartaCompromiso': 'Carta Compromiso',
            'cartaAceptacion': 'Carta Aceptacion',
            'constanciaTerminacion': 'Constancia Terminacion',            
            'actaCalificaciones': 'Acta Calificaciones',            
            'cartaTerminacion': 'Carta Terminacion',            
            'actaResidencia': 'Acta Residencia',            
        }

    def __init__(self, *args, **kwargs):
        super(ExpedienteViewForm, self).__init__(*args, **kwargs)
        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input'            
            self.fields[myField].widget.attrs['disabled'] = True


class Reporte1Form(ModelForm):
    class Meta:
        model = ReporteParcial1
        fields = '__all__'
        exclude = ['r1_fechaEntrega']
        labels = {
            'r1_hojaRevisores': 'Hoja Revisores',
            'r1_formatoEvaluacion': 'Formato Evaluacion',
        }
        
    def __init__(self, *args, **kwargs):
        super(Reporte1Form, self).__init__(*args, **kwargs)        
        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input'        

class Reporte2Form(ModelForm):
    class Meta:
        model = ReporteParcial2
        fields = '__all__'
        exclude = ['r2_fechaEntrega']
        labels = {
            'r2_hojaRevisores': 'Hoja Revisores',
            'r2_formatoEvaluacion': 'Formato Evaluacion',
        }

    def __init__(self, *args, **kwargs):
        super(Reporte2Form, self).__init__(*args, **kwargs)
        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input'                    

class ReporteFinalForm(ModelForm):
    class Meta:
        model = ReporteFinal
        fields = '__all__'
        exclude = ['rf_fechaEntrega', 'calificacion']
        labels = {
            'rf_hojaRevisores': 'Hoja Revisores',
            'rf_formatoEvaluacion': 'Formato Evaluacion',
        }

    def __init__(self, *args, **kwargs):
        super(ReporteFinalForm, self).__init__(*args, **kwargs)
        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input'                    

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
        today = date.today()
        YEARSI= [x for x in range(today.year,today.year+1)]
        YEARSF= [x for x in range(today.year,today.year+3)]
        model = Anteproyecto
        fields = '__all__'
        exclude = ['docentes', 'dependencia', 'asesorExterno', 'anteproyectoDoc']   
        labels = {
            'a_nombre': 'Nombre del Anteproyecto',
            'tipoProyecto': 'Tipo de Proyecto',
            'fechaEntrega': 'Fecha de entrega',
            'numIntegrantes': 'Numero de integrantes',
            'periodoInicio': 'Fecha inicio',            
            'periodoFin': 'Fecha Fin',            
        }
        widgets = {
            'periodoInicio': forms.SelectDateWidget(years=YEARSI),
            #'periodoInicio': forms.DateField(widget=forms.SelectDateWidget(years=YEARS)),
            'periodoFin': forms.SelectDateWidget(years=YEARSF),
        }
                

    def __init__(self, *args, **kwargs):
        super(AnteproyectoEstForm, self).__init__(*args, **kwargs)        
        for myField in self.fields:            
            if myField == 'periodoInicio' or myField == 'periodoFin':                
                self.fields[myField].widget.attrs['class'] = 'ml-4 mt-2 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input'                
            else :
                self.fields[myField].widget.attrs['class'] = 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input'
            
class AnteproyectoViewForm(ModelForm):
    class Meta:
        model = Anteproyecto
        fields = '__all__'     
        exclude = ['docentes', 'dependencia', 'asesorExterno', 'anteproyectoDoc']   
        labels = {
            'a_nombre': 'Nombre del Anteproyecto',
            'tipoProyecto': 'Tipo de Proyecto',
            'fechaEntrega': 'Fecha de entrega',
            'numIntegrantes': 'Numero de integrantes',
            'codigoUnion': 'Codigo de union',
            'periodoInicio': 'Fecha inicio',            
            'periodoFin': 'Fecha Fin',            
        }        

    def __init__(self, *args, **kwargs):
        super(AnteproyectoViewForm, self).__init__(*args, **kwargs)
        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input'            
            self.fields[myField].widget.attrs['disabled'] = True

class AnteproyectoForm(ModelForm):
    class Meta:
        model = Anteproyecto
        fields = '__all__'
        exclude = ['docentes', 'dependencia', 'asesorExterno', 'anteproyectoDoc']   
        labels = {
            'a_nombre': 'Nombre del anteproyecto',
        }        

    def __init__(self, *args, **kwargs):
        super(AnteproyectoForm, self).__init__(*args, **kwargs)
        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input'                        
            
class AnteproyectoDocForm(ModelForm):
    class Meta:
        model = Anteproyecto
        fields = ['anteproyectoDoc']        
        labels = {
            'anteproyectoDoc': 'Anteproyecto',
        }        

    def __init__(self, *args, **kwargs):
        super(AnteproyectoDocForm, self).__init__(*args, **kwargs)
        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input'                                    

class ResidenciaViewForm(ModelForm):
    class Meta:
        model = Residencia
        fields = '__all__'
        exclude = ['dependencia', 'asesorExterno']
        labels = {
            'nombre': 'Nombre del proyecto de Residencia',
            'tipoProyecto': 'Tipo de Proyecto',
            'fechaEntrega': 'Fecha de entrega',
            'numIntegrantes': 'Numero de integrantes',            
            'periodoInicio': 'Fecha inicio',            
            'periodoFin': 'Fecha Fin',            
        }   
    
    def __init__(self, *args, **kwargs):
        super(ResidenciaViewForm, self).__init__(*args, **kwargs)
        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input'                             
            self.fields[myField].widget.attrs['disabled'] = True
        
            
class DependenciaForm(ModelForm):
    class Meta:
        model = Dependencia
        fields = '__all__'
        exclude = ['domicilio', 'titular']
        labels = {
            'd_nombre': 'Nombre',
            'rfc': 'RFC (Elimina espacios y guiones)',
            'numCelular': 'Numero de Celular',
            'correoElectronico': 'Correo Electronico',            
        }

    def __init__(self, *args, **kwargs):
        super(DependenciaForm, self).__init__(*args, **kwargs)
        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input'
    
class DependenciaViewForm(ModelForm):
    class Meta:
        model = Dependencia
        fields = '__all__'
        exclude = ['domicilio', 'titular']
        labels = {
            'd_nombre': 'Nombre',
            'rfc': 'RFC',
            'numCelular': 'Numero de Celular',
            'correoElectronico': 'Correo Electronico',            
        }

    def __init__(self, *args, **kwargs):
        super(DependenciaViewForm, self).__init__(*args, **kwargs)
        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input'
            self.fields[myField].widget.attrs['disabled'] = True
        
class TitularForm(ModelForm):
    class Meta:
        model = TitularDependencia
        fields = '__all__'
        labels = {
            't_nombre': 'Nombre(s)',
            't_apellidoP': 'Apellido Paterno',
            't_apellidoM': 'Apellido Materno',
            't_puesto': 'Puesto'
        }
    
    def __init__(self, *args, **kwargs):
        super(TitularForm, self).__init__(*args, **kwargs)
        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input'

class TitularViewForm(ModelForm):
    class Meta:
        model = TitularDependencia
        fields = '__all__'
        labels = {
            't_nombre': 'Nombre(s)',
            't_apellidoP': 'Apellido Paterno',
            't_apellidoM': 'Apellido Materno',
            't_puesto': 'Puesto'
        }
    
    def __init__(self, *args, **kwargs):
        super(TitularViewForm, self).__init__(*args, **kwargs)
        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input'
            self.fields[myField].widget.attrs['disabled'] = True
            
class AsesorEForm(ModelForm):
    class Meta:
        model = AsesorExterno
        fields = '__all__'   
        labels = {
            'nombre': 'Nombre(s)',
            'apellidoP': 'Apellido Paterno',
            'apellidoM': 'Apellido Materno',
        }
    
    def __init__(self, *args, **kwargs):
        super(AsesorEForm, self).__init__(*args, **kwargs)
        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input'
            
class AsesorEViewForm(ModelForm):
    class Meta:
        model = AsesorExterno
        fields = '__all__'   
        labels = {
            'nombre': 'Nombre(s)',
            'apellidoP': 'Apellido Paterno',
            'apellidoM': 'Apellido Materno',
        }
    
    def __init__(self, *args, **kwargs):
        super(AsesorEViewForm, self).__init__(*args, **kwargs)
        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input'            
            self.fields[myField].widget.attrs['disabled'] = True