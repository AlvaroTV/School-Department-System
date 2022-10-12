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
     
    cartaPresentacion = models.FileField(upload_to='records/cartaP/', null=True, blank=True)        
    cartaCompromiso = models.FileField(upload_to='records/cartaC/', null=True, blank=True)        
    cronograma = models.FileField(upload_to='records/crono/', null=True, blank=True)        
    residenciaDoc = models.FileField(upload_to='records/resiDoc/', null=True, blank=True)        
    manualDoc = models.FileField(upload_to='records/manual/', null=True, blank=True)  
        

class Estudiante(models.Model):
    #user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    CARRERA = (
        ('Ingenieria Sistemas Computacionales', 'Ingenieria Sistemas Computacionales'),
        ('Ingenieria Civil', 'Ingenieria Civil'),
        ('Ingenieria Industrial', 'Ingenieria Industrial'),
    )
    SISTEMAS = 'Ingenieria Sistemas Computacionales'
    SEMESTRES = ((8, '8'), (9, '9'), (10, '10'), (11, '11'), (12, '12'), (13, '13'), (14, '14'))
    
    # Llaves Foranes
    domicilio = models.OneToOneField(Domicilio, on_delete=models.CASCADE, null=True)    
    expediente = models.OneToOneField(Expediente, on_delete=models.CASCADE, null=True, blank=True)
    
    # Atributos
    nombre = models.CharField(max_length=100)
    apellidoP = models.CharField(max_length=70)
    apellidoM = models.CharField(max_length=70)
    numCelular = models.CharField(max_length=20)
    correoElectronico = models.CharField(max_length=200, null=True, blank=True)    
    numControl = models.CharField(max_length=8, unique=True, blank=True)
    carrera = models.CharField(max_length=200, choices=CARRERA, default=SISTEMAS)
    semestre = models.IntegerField(choices=SEMESTRES) 
    curp = models.CharField(max_length=18, null=True, blank=True)
    institutoSeguridadSocial = models.CharField(max_length=200, blank=True)                    
    numSeguridadSocial = models.CharField(max_length=70, null=True, blank=True)        
    fotoUsuario = models.ImageField(default='profilepic.png', upload_to='profilesPic/',null=True, blank=True)
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    #docs = models.FileField(upload_to='docs/', null=True, blank=True)
    
    def __str__(self):
        return f'({self.id}) | {self.nombre} {self.apellidoP} {self.apellidoM}'
    
