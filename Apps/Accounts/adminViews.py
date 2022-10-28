from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
#from django.db.models import Count
from datetime import date, timedelta
from .models import *
from .forms import *
from .adminForms import *
from .decorators import *
from .views import generarCodigo, obtenerCodigo, buscarCodigo
# Create your views here.

def plantilla(request):
    group = request.user.groups.all()[0].name
    context = {'group': group}
    return render(request, 'Admin/expedientes.html', context)        

def anteproyectos(request):
    group = request.user.groups.all()[0].name
    anteproyectos = Anteproyecto.objects.all()
    context = {'group': group, 'anteproyectos': anteproyectos}
    return render(request, 'Admin/anteproyectos.html', context)    

def residencias(request):
    group = request.user.groups.all()[0].name
    residencias = Residencia.objects.all()
    context = {'group': group, 'residencias': residencias}
    return render(request, 'Admin/residencias.html', context)        

def expedientes(request):
    group = request.user.groups.all()[0].name
    expedientes = Expediente.objects.all()    
    context = {'group': group, 'expedientes': expedientes}
    return render(request, 'Admin/expedientes.html', context)        

def estudiantes(request):
    group = request.user.groups.all()[0].name
    estudiantes = Estudiante.objects.all()
    context = {'group': group, 'estudiantes': estudiantes}
    return render(request, 'Admin/estudiantes.html', context)        

def docentes(request):
    group = request.user.groups.all()[0].name
    docentes = Docente.objects.all()
    context = {'group': group, 'docentes': docentes}
    return render(request, 'Admin/docentes.html', context)     

def verAnteproyecto(request, pk):
    group = request.user.groups.all()[0].name
    anteproyecto = Anteproyecto.objects.get(id = pk)    
    estudiantes = Estudiante.objects.filter(anteproyecto = anteproyecto)        
    asesorInterno = anteproyecto.asesorInterno
    revisor = anteproyecto.revisor                
    dependencia = anteproyecto.dependencia 
    observacion = anteproyecto.observacion
    fechaObservacion = observacion.fechaCreacion    
    observaciones = ObservacionDocente.objects.filter(observacion = observacion)                                
    dias = 5 + observacion.incrementarDias
    fechaObservacion = fechaObservacion + timedelta(days=dias)           
    fechaCorte = fechaObservacion + timedelta(days=1)             
    fechaActual = date.today
    fechaObservacion = fechaObservacion.strftime("%d/%b/%Y")                   
    data = []        
    
    if anteproyecto.numIntegrantes == 1: data.append('id_codigoUnion')
                     
    formA = AnteproyectoViewForm(instance = anteproyecto)                                        
    formD = DependenciaViewForm(instance = dependencia)
    formT = TitularViewForm(instance = dependencia.titular)
    formDom = DomicilioViewForm(instance = dependencia.domicilio)
    formDoc = AnteproyectoDocForm(instance = anteproyecto)
    formAE = AsesorEViewForm(instance = anteproyecto.asesorExterno)     
    formEstado = AnteproyectoEstadoForm(instance = anteproyecto)
    
    if request.method == 'POST':
        formEstado = AnteproyectoEstadoForm(request.POST, instance = anteproyecto)
        if formEstado.is_valid():
            formEstado.save()
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
        
    context = {'group': group, 'anteproyecto': anteproyecto, 'estudiantes': estudiantes, 'dependencia': dependencia, 'revisor': revisor, 'asesorInterno': asesorInterno, 'formA': formA, 'formD': formD, 'formT': formT, 'formAE': formAE ,'formDom': formDom, 'formDoc': formDoc, 'fechaObservacion': fechaObservacion, 'observaciones': observaciones, 'formEstado': formEstado, 'data': data}
    return render(request, 'Admin/verAnteproyecto.html', context)           

def editarAnteproyectoAdmin(request, pk):
    group = request.user.groups.all()[0].name
    data = ['id_codigoUnion']
    anteproyecto = Anteproyecto.objects.get(id = pk)    
    estudiantes = Estudiante.objects.filter(anteproyecto = anteproyecto).count()        
    dependencia = anteproyecto.dependencia
    asesorExterno = anteproyecto.asesorExterno
    titular = dependencia.titular
    domicilio = dependencia.domicilio
    codigo = anteproyecto.codigoUnion
    numIntegrantes = anteproyecto.numIntegrantes
    mensaje = ''    
    
    formA = AnteproyectoEstForm(instance = anteproyecto)                                
    formD = DependenciaForm(instance = dependencia)
    formT = TitularForm(instance = titular)
    formDom = DomicilioForm(instance = domicilio)
    formAE = AsesorEForm(instance = asesorExterno)                 
    
    if request.method == 'POST':                        
        formA = AnteproyectoEstForm(request.POST, instance = anteproyecto)                                
        formD = DependenciaForm(request.POST, instance = dependencia)
        formT = TitularForm(request.POST, instance = titular)
        formDom = DomicilioForm(request.POST, instance = domicilio)
        formAE = AsesorEForm(request.POST, instance = asesorExterno)   
                  
        if formA.is_valid() and formD.is_valid() and formT.is_valid() and formAE.is_valid() and formDom.is_valid():
            numIntegrantes2 = int(formA['numIntegrantes'].value())                                    
            if numIntegrantes2 < 1:
                mensaje = 'El numero de integrantes no puede ser menor a 1'
            else:                
                if numIntegrantes == 1 and numIntegrantes2 >= 2:                    
                    codigo = obtenerCodigo()                    
                elif numIntegrantes >= 2 and numIntegrantes2 == 1 and estudiantes == 1:                    
                    codigo = '0000000000'                                                                                                                                                                                             
                if numIntegrantes > numIntegrantes2 and estudiantes > numIntegrantes2:                                        
                    mensaje = 'No se puede reducir el numero de integrantes. Eliminine algun integrante del anteproyecto para poder reducir el numero de integrantes'                    
                else:                                                
                    domicilio = formDom.save()                  
                    titular = formT.save()              
                    asesorExterno = formAE.save()      
                    dependencia = formD.save()            
                    anteproyecto = formA.save()
                    anteproyecto.dependencia = dependencia
                    anteproyecto.asesorExterno = asesorExterno
                    anteproyecto.codigoUnion = codigo
                    asesorExterno.dependencia = dependencia
                    asesorExterno.save()                                    
                    anteproyecto.save() 
                    return redirect('verAnteproyecto', pk = anteproyecto.id)                               
    
    context = {'group': group, 'formA': formA, 'formD': formD, 'formT': formT, 'formAE': formAE ,'formDom': formDom, 'anteproyecto': anteproyecto, 'dependencia': dependencia, 'mensaje': mensaje, 'group': group, 'data': data}                
    return render(request, 'Admin/editarAnteproyecto.html', context)        

def editarObservaciones(request, pk):
    group = request.user.groups.all()[0].name
    docente = request.user.docente
    anteproyecto = Anteproyecto.objects.get(id = pk)
    observacion = anteproyecto.observacion
    fechaObservacion = observacion.fechaCreacion    
    observaciones = ObservacionDocente.objects.filter(observacion = observacion)                                
    dias = 5 + observacion.incrementarDias
    fechaObservacion = fechaObservacion + timedelta(days=dias)           
    fechaCorte = fechaObservacion + timedelta(days=1)             
    fechaActual = date.today
    fechaObservacion = fechaObservacion.strftime("%d/%b/%Y")                           
    
    if request.method == 'POST':                
        
        try:
            rDias = int(request.POST['agregarDias'])
        except: 
            rDias = None
            
        try:
            rObservacion = request.POST['Dobservacion']
        except: 
            rObservacion = None
            
        if rDias is not None and rDias > 0:            
            observacion.incrementarDias += rDias            
            observacion.save()
            
        if rObservacion:            
            nuevaObservacion = ObservacionDocente(
                docente = docente,
                observacion = observacion,
                observacionD = rObservacion
            )
            nuevaObservacion.save()            
            
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))                    
    
    context = {'anteproyecto': anteproyecto, 'estudiantes': estudiantes, 'group': group, 'observaciones': observaciones, 'fechaObservacion': fechaObservacion, 'fechaCorte': fechaCorte, 'fechaActual': fechaActual}    
    return render(request, 'Admin/editObservaciones.html', context)        

def eliminarObservacion(request, pk):    
    observacion = ObservacionDocente.objects.get(id = pk)    
    observacion.delete()    
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

