from datetime import date
from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.core.exceptions import ValidationError
import os
import uuid

# Validator
def validate_nonzero(value):
    if value == 0:
        raise ValidationError("El tiempo debe ser mayor a 0")

# Create your models here.
class Materia(models.Model):    
    SEMESTRES = ((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'))
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,unique=True)
    clave = models.CharField(max_length=10, unique=True, null=True, error_messages = {"unique":"Existe otra materia con esta clave."})
    nombre = models.CharField(max_length=150, null=True)
    semestre = models.IntegerField(choices=SEMESTRES)     
    
    def __str__(self):
        return f'{self.id}'

class Domicilio(models.Model):
    ESTADOS = (('Aguascalientes', 'Aguascalientes'),('Baja California', 'Baja California'),('Baja California Sur', 'Baja California Sur'),('Campeche', 'Campeche'),('Chiapas', 'Chiapas'),('Chihuahua', 'Chihuahua'),('Coahuila', 'Coahuila'),('Colima', 'Colima'),('Ciudad de México', 'Ciudad de México'),('Durango', 'Durango'),('Guanajuato', 'Guanajuato'),('Guerrero', 'Guerrero'),('Hidalgo', 'Hidalgo'),('Jalisco', 'Jalisco'),('Estado de Mexico', 'Estado de Mexico'),('Michoacan', 'Michoacan'),('Morelos', 'Michoacan'),('Nayarit', 'Nayarit'),('Nuevo Leon', 'Nuevo Leon'),('Oaxaca', 'Oaxaca'),('Puebla', 'Puebla'),('Queretaro', 'Queretaro'),('Quintana Roo', 'Quintana Roo'),('San Luis Potosi', 'San Luis Potosi'),('Sinaloa', 'Sinaloa'),('Sonora', 'Sonora'),('Tabasco', 'Tabasco'),('Tamaulipas', 'Tamaulipas'),('Tlaxcala', 'Tlaxcala'),('Veracruz', 'Veracruz'),('Yucatan', 'Yucatan'),('Zacatecas', 'Zacatecas'))
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,unique=True)
    calle = models.CharField(max_length=200, null=True, blank=True)
    colonia = models.CharField(max_length=200, null=True, blank=True)
    municipio = models.CharField(max_length=200, null=True, blank=True)
    codigoPostal = models.CharField(max_length=5, null=True, blank=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='Oaxaca')

class TitularDependencia(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,unique=True)
    t_nombre = models.CharField(max_length=100)
    t_apellidoP = models.CharField(max_length=70)
    t_apellidoM = models.CharField(max_length=70)
    t_puesto = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.t_nombre} {self.t_apellidoP} {self.t_apellidoM}'

class ReporteParcial1(models.Model):   
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,unique=True)
    r1_hojaRevisores = models.FileField(upload_to='records/reporte1/hojaRevisores/', null=True, blank=True, validators=[FileExtensionValidator(['pdf'])])            
    r1_formatoEvaluacion = models.FileField(upload_to='records/reporte1/formatoEvaluacion/', null=True, blank=True, validators=[FileExtensionValidator(['pdf'])])            
    r1_fechaEntrega = models.DateField(null=True, default=date.today)
    
class ReporteParcial2(models.Model):  
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,unique=True)
    r2_hojaRevisores = models.FileField(upload_to='records/reporte2/hojaRevisores/', null=True, blank=True, validators=[FileExtensionValidator(['pdf'])])            
    r2_formatoEvaluacion = models.FileField(upload_to='records/reporte2/formatoEvaluacion/', null=True, blank=True, validators=[FileExtensionValidator(['pdf'])])            
    r2_fechaEntrega = models.DateField(null=True, default=date.today)    
    
class ReporteFinal(models.Model):   
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,unique=True)
    rf_hojaRevisores = models.FileField(upload_to='records/reporteF/hojaRevisores/', null=True, blank=True, validators=[FileExtensionValidator(['pdf'])])            
    rf_formatoEvaluacion = models.FileField(upload_to='records/reporteF/formatoEvaluacion/', null=True, blank=True, validators=[FileExtensionValidator(['pdf'])])            
    rf_fechaEntrega = models.DateField(null=True, default=date.today)    
    calificacion = models.IntegerField(null=True, blank=True)    

class Expediente(models.Model):    
    ESTATUS = (('INICIAL', 'INICIAL'), ('PROCESO', 'PROCESO'), ('COMPLETO', 'COMPLETO'), ('FINALIZADO', 'FINALIZADO'))
    # Llaves foraneas
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,unique=True)
    reporteParcial1 = models.ForeignKey(ReporteParcial1, on_delete=models.SET_NULL, null=True, blank=True)    
    reporteParcial2 = models.ForeignKey(ReporteParcial2, on_delete=models.SET_NULL, null=True, blank=True)    
    reporteFinal = models.ForeignKey(ReporteFinal, on_delete=models.SET_NULL, null=True, blank=True)   
          
    estatus = models.CharField(max_length=15, choices=ESTATUS, default='INICIAL')     
    solicitudResidencia = models.FileField(upload_to='records/solicitudResidencia/', null=True, blank=True, validators=[FileExtensionValidator(['pdf'])])     
    anteproyecto = models.FileField(upload_to='records/anteproyectoAceptado/', null=True, blank=True, validators=[FileExtensionValidator(['pdf'])])            
    dictamen = models.FileField(upload_to='records/dictamen/', null=True, blank=True, validators=[FileExtensionValidator(['pdf'])])            
    horario = models.FileField(upload_to='records/horario/', null=True, blank=True, validators=[FileExtensionValidator(['pdf'])])            
    cartaCompromiso = models.FileField(upload_to='records/cartaC/', null=True, blank=True, validators=[FileExtensionValidator(['pdf'])])                               
    cronograma = models.FileField(upload_to='records/crono/', null=True, blank=True, validators=[FileExtensionValidator(['pdf'])])     
    cartaPresentacion = models.FileField(upload_to='records/cartaP/', null=True, blank=True, validators=[FileExtensionValidator(['pdf'])])            
    cartaAceptacion = models.FileField(upload_to='records/cartaAceptacion/', null=True, blank=True, validators=[FileExtensionValidator(['pdf'])])            
    cartaLiberacion = models.FileField(upload_to='records/cartaLiberacion/', null=True, blank=True, validators=[FileExtensionValidator(['pdf'])])                
    manualUsuario = models.FileField(upload_to='records/manualUsuario/', null=True, blank=True, validators=[FileExtensionValidator(['pdf'])])            
    manualTecnico = models.FileField(upload_to='records/manualTecnico/', null=True, blank=True, validators=[FileExtensionValidator(['pdf'])])                    

class PerfilAcademico(models.Model):
    # Llaves Foraneas
    materias = models.ManyToManyField( Materia, blank=True)
    
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,unique=True)
    especialidad = models.CharField(max_length=50, null=True, blank=True)


class Docente(models.Model):
    ESTATUS = (('ACTIVO', 'ACTIVO'), ('VACACIONES', 'VACIONES'), ('INACTIVO', 'INACTIVO'))
    
    perfilAcademico = models.OneToOneField(PerfilAcademico, null=True, blank=True, on_delete=models.SET_NULL)
    
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,unique=True)
    nombre = models.CharField(max_length=100)
    apellidoP = models.CharField(max_length=70)
    apellidoM = models.CharField(max_length=70)
    numCelular = models.CharField(max_length=20, null=True, blank=True)
    correoElectronico = models.CharField(max_length=200, null=True, blank=True)        
    curp = models.CharField(max_length=18, null=True, blank=True)
    rfc = models.CharField(max_length=13, null=True, blank=True)
    estatus = models.CharField(max_length=15, choices=ESTATUS, default='ACTIVO')     
    puesto = models.CharField(max_length=70, null=True, blank=True)     
    fotoUsuario = models.ImageField(default='profilepicD.jpg', upload_to='profilesPic/teachers/',null=True, blank=True)
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)   
    
    def __str__(self):
        return f'{self.nombre} {self.apellidoP} {self.apellidoM}'     

class Observacion(models.Model):    
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,unique=True)
    fechaCreacion = models.DateField(default=date.today)
    incrementarDias = models.PositiveIntegerField(default=0)

class ObservacionDocente(models.Model):
    # Llaves foraneas
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE, null=True, blank=True)
    observacion = models.ForeignKey(Observacion, on_delete=models.CASCADE, null=True, blank=True)
    
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,unique=True)
    observacionD = RichTextField(blank=True, null=True)
    fechaElaboracion = models.DateTimeField(auto_now_add=True)
    
class Dependencia(models.Model):
    OPCIONES = (('INDUSTRIAL', 'INDUSTRIAL'), ('SERVICIOS', 'SERVICIOS'), ('PUBLICO', 'PUBLICO'), ('PRIVADO', 'PRIVADO'), ('OTRO', 'OTRO'),)
    
    # Llaves foraneas
    domicilio = models.OneToOneField(Domicilio, on_delete=models.CASCADE, null=True)
    titular = models.OneToOneField(TitularDependencia, on_delete=models.CASCADE, null=True)
    
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,unique=True)
    d_nombre = models.CharField(max_length=100)
    rfc = models.CharField(max_length=13, null=True, unique=True, error_messages = {"unique":"Existe otra Organizacion o Empresa con este RFC."})
    giro = models.CharField(max_length=20, choices=OPCIONES, default='PUBLICO', blank=True)    
    numCelular = models.CharField(max_length=20)
    correoElectronico = models.CharField(max_length=200, null=True, blank=True)    
    mision = models.CharField(max_length=1000)
    
    def __str__(self):
        return f'{self.d_nombre}'

class AsesorExterno(models.Model):
    # Llaves foraneas
    dependencia = models.ForeignKey(Dependencia, on_delete=models.SET_NULL, null=True, blank=True)
    
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,unique=True)
    nombre = models.CharField(max_length=100)
    apellidoP = models.CharField(max_length=70)
    apellidoM = models.CharField(max_length=70)
    puesto = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.nombre} {self.apellidoP} {self.apellidoM}'

class Residencia(models.Model):
    TIPOS = (('PROPUESTA PROPIA', 'PROPUESTA PROPIA'), ('BANCO DE PROYECTOS', 'BANCO DE PROYECTOS'), ('TRABAJADOR', 'TRABAJADOR'))
    ESTADOS = (('INICIADA', 'INICIADA'), ('EN PROCESO', 'EN PROCESO'), ('PRORROGA', 'PRORROGA'), ('NO FINALIZADA', 'NO FINALIZADA'), ('RECHAZADA', 'RECHAZADA'), ('FINALIZADA', 'FINALIZADA'))
    
    # Llaves foraneas
    dependencia = models.ForeignKey(Dependencia, on_delete=models.SET_NULL, null=True, blank=True)
    asesorExterno = models.ForeignKey(AsesorExterno, on_delete=models.SET_NULL, null=True, blank=True)
    r_asesorInterno = models.ForeignKey(Docente, on_delete=models.SET_NULL, null=True, blank=True, related_name='r_asesorInterno')
    r_revisor = models.ForeignKey(Docente, on_delete=models.SET_NULL, null=True, blank=True, related_name='r_revisor')
    
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,unique=True)
    nombre = models.CharField(max_length=300)
    tipoProyecto = models.CharField(max_length=25, choices=TIPOS)         
    numIntegrantes = models.IntegerField(default=1)
    estatus = models.CharField(max_length=15, choices=ESTADOS, default='INICIADA', blank=True)    
    periodoInicio = models.DateField(null=True)
    periodoFin = models.DateField(null=True)    

class Anteproyecto(models.Model):
    TIPOS = (('PROPUESTA PROPIA', 'PROPUESTA PROPIA'), ('BANCO DE PROYECTOS', 'BANCO DE PROYECTOS'), ('TRABAJADOR', 'TRABAJADOR'))
    ESTADOS = (('ENVIADO', 'ENVIADO'), ('PENDIENTE', 'PENDIENTE'), ('EN REVISION', 'EN REVISION'), ('REVISADO', 'REVISADO'), ('ACEPTADO', 'ACEPTADO'), ('RECHAZADO', 'RECHAZADO'))
    ESTADOSR = (('PENDIENTE', 'PENDIENTE'), ('EN REVISION', 'EN REVISION'), ('ACEPTADO', 'ACEPTADO'), ('RECHAZADO', 'RECHAZADO'))
    N_INTEGRANTES = ((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'))
    
    # Llave foranea
    #docentes = models.ManyToManyField(Docente, blank=True)    
    revisor1 = models.ForeignKey(Docente, on_delete=models.SET_NULL, null=True, blank=True, related_name='revisor1')
    revisor2 = models.ForeignKey(Docente, on_delete=models.SET_NULL, null=True, blank=True, related_name='revisor2')
    dependencia = models.ForeignKey(Dependencia, on_delete=models.SET_NULL, null=True, blank=True)
    asesorExterno = models.ForeignKey(AsesorExterno, on_delete=models.SET_NULL, null=True, blank=True)
    observacion = models.OneToOneField(Observacion, on_delete=models.SET_NULL, null=True, blank=True)
    
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,unique=True)
    a_nombre = models.CharField(max_length=300)
    tipoProyecto = models.CharField(max_length=25, choices=TIPOS, default='PROPUESTA PROPIA')     
    fechaEntrega = models.DateField(default=date.today)
    numIntegrantes = models.IntegerField(choices=N_INTEGRANTES, default=1)
    estatus = models.CharField(max_length=15, choices=ESTADOS, default='ENVIADO', blank=True)
    estatusR1 = models.CharField(max_length=15, choices=ESTADOSR, default='PENDIENTE')
    estatusR2 = models.CharField(max_length=15, choices=ESTADOSR, default='PENDIENTE')    
    codigoUnion = models.CharField(max_length=10, null=True, blank=True)    
    anteproyectoDoc = models.FileField(upload_to='records/anteproyectoDoc/', validators=[FileExtensionValidator(['pdf'])], default=None)                        

class Actualizacion_anteproyecto(models.Model):
    ESTADOS = (('NO LEIDO', 'NO LEIDO'), ('LEIDO', 'LEIDO'))
    TIPOS = (('ACTUALIZADO', 'ACTUALIZADO'), ('REMOVIDO', 'REMOVIDO'))
    
    # Llaves foraneas
    anteproyecto = models.ForeignKey(Anteproyecto, on_delete=models.SET_NULL, null=True, blank=True)
    
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,unique=True)    
    fecha = models.DateTimeField(auto_now_add=True)
    descripcion = models.CharField(max_length=100)
    tipo = models.CharField(max_length=15, choices=TIPOS, default='ACTUALIZADO')
    estado = models.CharField(max_length=10, choices=ESTADOS, default='NO LEIDO')

class Anteproyecto_materia(models.Model):
    # Llaves foraneas
    anteproyecto = models.ForeignKey(Anteproyecto, on_delete=models.SET_NULL, null=True, blank=True)
    materia = models.ForeignKey(Materia, on_delete=models.SET_NULL, null=True, blank=True)
    
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,unique=True)
    compatibilidad = models.IntegerField(null=True, blank=True)

class Estudiante(models.Model):    
    CARRERA = (
        ('Ingenieria Sistemas Computacionales', 'Ingenieria Sistemas Computacionales'),
        ('Ingenieria Civil', 'Ingenieria Civil'),
        ('Ingenieria Industrial', 'Ingenieria Industrial'),
    )
    SISTEMAS = 'Ingenieria Sistemas Computacionales'
    SEMESTRES = ((8, '8'), (9, '9'), (10, '10'), (11, '11'), (12, '12'), (13, '13'), (14, '14'))
    
    # Llaves Foraneas
    domicilio = models.OneToOneField(Domicilio, on_delete=models.SET_NULL, null=True, blank=True)    
    expediente = models.OneToOneField(Expediente, on_delete=models.SET_NULL, null=True, blank=True)
    anteproyecto = models.ForeignKey(Anteproyecto, on_delete=models.SET_NULL, null=True, blank=True)
    residencia = models.ForeignKey(Residencia, on_delete=models.SET_NULL, null=True, blank=True)
    
    # Atributos
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,unique=True)
    nombre = models.CharField(max_length=100)
    apellidoP = models.CharField(max_length=70)
    apellidoM = models.CharField(max_length=70)
    numCelular = models.CharField(max_length=20)
    correoElectronico = models.CharField(max_length=200, null=True, blank=True)    
    numControl = models.CharField(max_length=8, unique=True, blank=True, error_messages = {"unique":"Existe otro alumno con este numero de control."})
    carrera = models.CharField(max_length=200, choices=CARRERA, default=SISTEMAS)
    semestre = models.IntegerField(choices=SEMESTRES) 
    curp = models.CharField(max_length=18, null=True, blank=True)
    institutoSeguridadSocial = models.CharField(max_length=200, blank=True)                    
    numSeguridadSocial = models.CharField(max_length=70, null=True, blank=True)        
    fotoUsuario = models.ImageField(default='profilepic.png', upload_to='profilesPic/students/',null=True, blank=True)
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)    
    
    def __str__(self):
        return f'{self.nombre} {self.apellidoP} {self.apellidoM}'
    
class Avisos(models.Model):
    ENTIDADES = (('ESTUDIANTES', 'ESTUDIANTES'), ('DOCENTES', 'DOCENTES'), ('TODOS', 'TODOS'), ('PRIVADO', 'PRIVADO'))
    
    # Llaves foraneas
    estudiante = models.ForeignKey(Estudiante, on_delete=models.SET_NULL, null=True, blank=True)    
    docente = models.ForeignKey(Docente, on_delete=models.SET_NULL, null=True, blank=True)
    
    # Atributos
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,unique=True)
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    entidad = models.CharField(max_length=20, choices=ENTIDADES, default='TODOS')
    tiempoVida = models.PositiveIntegerField(default=1, validators =[validate_nonzero]) 
    descripcion = RichTextUploadingField(blank=True, null=True)    