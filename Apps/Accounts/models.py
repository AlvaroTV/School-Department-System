from datetime import date
from django.db import models
from django.contrib.auth.models import User
import os

# Create your models here.

class Domicilio(models.Model):
    ESTADOS = (('Aguascalientes', 'Aguascalientes'),('Baja California', 'Baja California'),('Baja California Sur', 'Baja California Sur'),('Campeche', 'Campeche'),('Chiapas', 'Chiapas'),('Chihuahua', 'Chihuahua'),('Coahuila', 'Coahuila'),('Colima', 'Colima'),('Ciudad de México', 'Ciudad de México'),('Durango', 'Durango'),('Guanajuato', 'Guanajuato'),('Guerrero', 'Guerrero'),('Hidalgo', 'Hidalgo'),('Jalisco', 'Jalisco'),('Estado de Mexico', 'Estado de Mexico'),('Michoacan', 'Michoacan'),('Morelos', 'Michoacan'),('Nayarit', 'Nayarit'),('Nuevo Leon', 'Nuevo Leon'),('Oaxaca', 'Oaxaca'),('Puebla', 'Puebla'),('Queretaro', 'Queretaro'),('Quintana Roo', 'Quintana Roo'),('San Luis Potosi', 'San Luis Potosi'),('Sinaloa', 'Sinaloa'),('Sonora', 'Sonora'),('Tabasco', 'Tabasco'),('Tamaulipas', 'Tamaulipas'),('Tlaxcala', 'Tlaxcala'),('Veracruz', 'Veracruz'),('Yucatan', 'Yucatan'),('Zacatecas', 'Zacatecas'))
    calle = models.CharField(max_length=200, null=True, blank=True)
    colonia = models.CharField(max_length=200, null=True, blank=True)
    municipio = models.CharField(max_length=200, null=True, blank=True)
    codigoPostal = models.CharField(max_length=5, null=True, blank=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='Oaxaca')

class TitularDependencia(models.Model):
    t_nombre = models.CharField(max_length=100)
    t_apellidoP = models.CharField(max_length=70)
    t_apellidoM = models.CharField(max_length=70)
    t_puesto = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.t_nombre} {self.t_apellidoP} {self.t_apellidoM}'

class ReporteParcial1(models.Model):
    ESTADOS = (('ENVIADO', 'ENVIADO'), ('PENDIENTE', 'PENDIENTE'), ('REVISADO', 'REVISADO'), ('ACEPTADO', 'ACEPTADO'), ('RECHAZADO', 'RECHAZADO'))
    estatus = models.CharField(max_length=15, choices=ESTADOS, default='ENVIADO', blank=True)
    calificacion = models.IntegerField(null=True, blank=True)
    reporte1Doc = models.FileField(upload_to='records/reporte1/')
    
class ReporteParcial2(models.Model):
    ESTADOS = (('ENVIADO', 'ENVIADO'), ('PENDIENTE', 'PENDIENTE'), ('REVISADO', 'REVISADO'), ('ACEPTADO', 'ACEPTADO'), ('RECHAZADO', 'RECHAZADO'))
    estatus = models.CharField(max_length=15, choices=ESTADOS, default='ENVIADO', blank=True)
    calificacion = models.IntegerField(null=True, blank=True)
    reporte2Doc = models.FileField(upload_to='records/reporte2/')
    
class ReporteFinal(models.Model):
    ESTADOS = (('ENVIADO', 'ENVIADO'), ('PENDIENTE', 'PENDIENTE'), ('REVISADO', 'REVISADO'), ('ACEPTADO', 'ACEPTADO'), ('RECHAZADO', 'RECHAZADO'))
    estatus = models.CharField(max_length=15, choices=ESTADOS, default='ENVIADO', blank=True)
    calificacion = models.IntegerField(null=True, blank=True)
    reporteDocFinal = models.FileField(upload_to='records/reporteF/')            

class Expediente(models.Model):    
    reporteParcial1 = models.ForeignKey(ReporteParcial1, on_delete=models.SET_NULL, null=True, blank=True)    
    reporteParcial2 = models.ForeignKey(ReporteParcial2, on_delete=models.SET_NULL, null=True, blank=True)    
    reporteFinal = models.ForeignKey(ReporteFinal, on_delete=models.SET_NULL, null=True, blank=True)   
        
    anteproyecto = models.FileField(upload_to='records/anteproyecto/', null=True, blank=True)        
    cartaPresentacion = models.FileField(upload_to='records/cartaP/', null=True, blank=True)        
    cartaCompromiso = models.FileField(upload_to='records/cartaC/', null=True, blank=True)        
    cronograma = models.FileField(upload_to='records/crono/', null=True, blank=True)        
    residenciaDoc = models.FileField(upload_to='records/resiDoc/', null=True, blank=True)        
    manualDoc = models.FileField(upload_to='records/manual/', null=True, blank=True)              

class Docente(models.Model):
    ESTATUS = (('ACTIVO', 'ACTIVO'), ('VACACIONES', 'VACIONES'), ('INACTIVO', 'INACTIVO'))
    
    nombre = models.CharField(max_length=100)
    apellidoP = models.CharField(max_length=70)
    apellidoM = models.CharField(max_length=70)
    numCelular = models.CharField(max_length=20)
    correoElectronico = models.CharField(max_length=200, null=True, blank=True)        
    curp = models.CharField(max_length=18, null=True, blank=True)
    rfc = models.CharField(max_length=13, null=True, blank=True)
    estatus = models.CharField(max_length=15, choices=ESTATUS, default='ACTIVO', blank=True)     
    fotoUsuario = models.ImageField(default='profilepic.png', upload_to='profilesPic/teachers/',null=True, blank=True)
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)        

class Dependencia(models.Model):
    OPCIONES = (('INDUSTRIAL', 'INDUSTRIAL'), ('SERVICIOS', 'SERVICIOS'), ('PUBLICO', 'PUBLICO'), ('PRIVADO', 'PRIVADO'), ('OTRO', 'OTRO'),)
    
    # Llaves foraneas
    domicilio = models.OneToOneField(Domicilio, on_delete=models.CASCADE, null=True)
    titular = models.OneToOneField(TitularDependencia, on_delete=models.CASCADE, null=True)
        
    d_nombre = models.CharField(max_length=100)
    rfc = models.CharField(max_length=13, null=True, blank=True)
    giro = models.CharField(max_length=20, choices=OPCIONES, default='PUBLICO', blank=True)    
    numCelular = models.CharField(max_length=20)
    correoElectronico = models.CharField(max_length=200, null=True, blank=True)    
    mision = models.CharField(max_length=200)

class AsesorExterno(models.Model):
    # Llaves foraneas
    dependencia = models.ForeignKey(Dependencia, on_delete=models.SET_NULL, null=True, blank=True)
    
    nombre = models.CharField(max_length=100)
    apellidoP = models.CharField(max_length=70)
    apellidoM = models.CharField(max_length=70)
    puesto = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.nombre} {self.apellidoP} {self.apellidoM}'

class Anteproyecto(models.Model):
    TIPOS = (('PROPUESTA PROPIA', 'PROPUESTA PROPIA'), ('BANCO DE PROYECTOS', 'BANCO DE PROYECTOS'), ('TRABAJADOR', 'TRABAJADOR'))
    ESTADOS = (('ENVIADO', 'ENVIADO'), ('PENDIENTE', 'PENDIENTE'), ('REVISADO', 'REVISADO'), ('ACEPTADO', 'ACEPTADO'), ('RECHAZADO', 'RECHAZADO'))
    
    # Llave foranea
    docentes = models.ManyToManyField(Docente, blank=True)    
    dependencia = models.ForeignKey(Dependencia, on_delete=models.SET_NULL, null=True, blank=True)
    asesorExterno = models.ForeignKey(AsesorExterno, on_delete=models.SET_NULL, null=True, blank=True)
    
    a_nombre = models.CharField(max_length=300)
    tipoProyecto = models.CharField(max_length=25, choices=TIPOS, default='ACTIVO')     
    fechaEntrega = models.DateTimeField(auto_now_add=True)
    numIntegrantes = models.IntegerField(default=1)
    estatus = models.CharField(max_length=15, choices=ESTADOS, default='ENVIADO', blank=True)
    codigoUnion = models.CharField(max_length=10, null=True, blank=True)
    periodoInicio = models.DateField(null=True, default=date.today)
    periodoFin = models.DateField(null=True)
    observaciones = models.CharField(max_length=500, null=True, blank=True)    

class Estudiante(models.Model):
    #user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    CARRERA = (
        ('Ingenieria Sistemas Computacionales', 'Ingenieria Sistemas Computacionales'),
        ('Ingenieria Civil', 'Ingenieria Civil'),
        ('Ingenieria Industrial', 'Ingenieria Industrial'),
    )
    SISTEMAS = 'Ingenieria Sistemas Computacionales'
    SEMESTRES = ((8, '8'), (9, '9'), (10, '10'), (11, '11'), (12, '12'), (13, '13'), (14, '14'))
    
    # Llaves Foraneas
    domicilio = models.OneToOneField(Domicilio, on_delete=models.CASCADE, null=True, blank=True)    
    expediente = models.OneToOneField(Expediente, on_delete=models.CASCADE, null=True, blank=True)
    anteproyecto = models.ForeignKey(Anteproyecto, on_delete=models.CASCADE, null=True, blank=True)
    
    # Atributos
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
    #docs = models.FileField(upload_to='docs/', null=True, blank=True)
    
    def __str__(self):
        return f'({self.id}) | {self.nombre} {self.apellidoP} {self.apellidoM}'
    
