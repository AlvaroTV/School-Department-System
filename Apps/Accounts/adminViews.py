from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
#from django.db.models import Count
from datetime import date, timedelta, datetime
import math
from .models import *
from .forms import *
from .adminForms import *
from .decorators import *
from .views import generarCodigo, obtenerCodigo, buscarCodigo
# Create your views here.

@admin_only
def anteproyectos(request, page, orderB, filter):
    group = request.user.groups.all()[0].name    
    all_anteproyectos = Anteproyecto.objects.all()     
    start = (page-1)*10    
    end = page*10
    
    if request.method == 'POST':
        opc = int(request.POST['search_options'])
        text = request.POST['search'] 
                        
        if text:
            all_anteproyectos = buscar_anteproyecto(all_anteproyectos, text, opc)                        
            anteproyectos = all_anteproyectos
            start = 0
            end = anteproyectos.count()
            totalA = all_anteproyectos.count()                        
            search = '.'             
            context = {'group': group, 'anteproyectos': anteproyectos, 'totalA': totalA, 'page': page, 'start': start+1, 'end': end, 'orderB': orderB, 'search': search, 'filter': filter}
            return render(request, 'Admin/anteproyectos.html', context)    
    
    all_anteproyectos = filtrar_anteproyectos(all_anteproyectos, filter)
    all_anteproyectos = ordenar_anteproyectos(all_anteproyectos, orderB)        
    anteproyectos = all_anteproyectos[start:end]
    if end != anteproyectos.count():
        end = end-10+anteproyectos.count()
    totalA = all_anteproyectos.count()
    n_buttons = math.ceil(totalA/10)
    buttons = [item for item in range(1, n_buttons+1)]
    next_page = page+1
    prev_page = page-1    
    context = {'group': group, 'anteproyectos': anteproyectos, 'totalA': totalA, 'buttons': buttons, 'page': page, 'start': start+1, 'end': end, 'next_page': next_page, 'prev_page': prev_page, 'n_buttons': n_buttons, 'orderB': orderB, 'filter': filter}
    return render(request, 'Admin/anteproyectos.html', context)    

@admin_only
def residencias(request, page, orderB, filter):
    group = request.user.groups.all()[0].name   
    all_residencias = Residencia.objects.all()             
    start = (page-1)*10    
    end = page*10
    
    if request.method == 'POST':
        opc = int(request.POST['search_options'])
        text = request.POST['search'] 
                        
        if text:
            all_residencias = buscar_residencia(all_residencias, text, opc)
            residencias = all_residencias
            start = 0
            end = residencias.count()
            totalR = all_residencias.count()                        
            search = '.'                         
            context = {'group': group, 'residencias': residencias, 'totalR': totalR, 'page': page, 'start': start+1, 'end': end, 'orderB': orderB, 'search': search, 'filter': filter}
            return render(request, 'Admin/residencias.html', context)            
        
    all_residencias = filtrar_residencias(all_residencias, filter)
    all_residencias = ordenar_residencias(all_residencias, orderB)
    residencias = all_residencias[start:end]
    if end != residencias.count():
        end = end-10+residencias.count()
    totalR = all_residencias.count()
    n_buttons = math.ceil(totalR/10)
    buttons = [item for item in range(1, n_buttons+1)]
    next_page = page+1
    prev_page = page-1    
    
    context = {'group': group, 'residencias': residencias, 'totalR': totalR, 'buttons': buttons, 'page': page, 'start': start+1, 'end': end, 'next_page': next_page, 'prev_page': prev_page, 'n_buttons': n_buttons, 'orderB': orderB, 'filter': filter}
    return render(request, 'Admin/residencias.html', context)        

@admin_only
def expedientes(request, page, orderB, filter):
    group = request.user.groups.all()[0].name      
    all_estudiantes = Estudiante.objects.all().exclude(expediente=None)  
    start = (page-1)*10    
    end = page*10    
    
    if request.method == 'POST':
        opc = int(request.POST['search_options'])
        text = request.POST['search'] 
                        
        if text:                        
            all_estudiantes = buscar_estudiante(all_estudiantes, text, opc)            
            estudiantes = all_estudiantes
            start = 0
            end = estudiantes.count()
            totalE = all_estudiantes.count()            
            asesorI = '.'    
            search = '.'             
            context = {'group': group, 'estudiantes': estudiantes, 'totalE': totalE, 'page': page, 'start': start+1, 'end': end, 'orderB': orderB, 'search': search, 'filter': filter}
            return render(request, 'Admin/expedientes.html', context)   
            
    all_estudiantes = filtrar_expedientes(all_estudiantes, filter)
    all_estudiantes = ordenar_estudiantes(all_estudiantes, orderB)
    estudiantes = all_estudiantes[start:end]
    if end != estudiantes.count():
        end = end-10+estudiantes.count()
    totalE = all_estudiantes.count()
    n_buttons = math.ceil(totalE/10)
    buttons = [item for item in range(1, n_buttons+1)]
    next_page = page+1
    prev_page = page-1    
    context = {'group': group, 'estudiantes': estudiantes, 'totalE': totalE, 'buttons': buttons, 'page': page, 'start': start+1, 'end': end, 'next_page': next_page, 'prev_page': prev_page, 'n_buttons': n_buttons, 'orderB': orderB, 'filter': filter}
    return render(request, 'Admin/expedientes.html', context)   

@admin_only
def verExpediente(request, pk):
    data = ['id_dictamen', 'id_solicitudResidencia', 'id_anteproyecto', 'id_horario', 'id_cartaAceptacion', 'id_cartaCompromiso', 'id_cronograma', 'id_cartaPresentacion']    
    group = request.user.groups.all()[0].name
    estudiante = Estudiante.objects.get(id = pk)
    expediente = estudiante.expediente
    r1 = expediente.reporteParcial1
    r2 = expediente.reporteParcial2
    rF = expediente.reporteFinal                
    formE = ExpedienteForm(instance=expediente)
    form1 = Reporte1Form(instance = r1)                  
    form2 = Reporte2Form(instance = r2)                  
    formF = ReporteFinalForm(instance = rF)                      
    formEstado = ExpedienteEstadoForm(instance = expediente)        
    
    if request.method == 'POST':
        formEstado = ExpedienteEstadoForm(request.POST, instance = expediente)     
        if formEstado.is_valid():
            formEstado.save()   
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
    
    context = {'group': group, 'data': data, 'estudiante': estudiante, 'expediente': expediente, 'r1': r1, 'r2': r2, 'rF': rF, 'formE': formE, 'form1': form1, 'form2': form2, 'formF': formF, 'formEstado': formEstado}
    return render(request, 'Admin/verExpediente.html', context)             

@admin_only
def eliminarExpediente(request, pk):
    expediente = Expediente.objects.get(id = pk)
    expediente.delete()
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

@admin_only
def estudiantes(request, page, orderB):
    group = request.user.groups.all()[0].name    
    all_estudiantes = Estudiante.objects.all()  
    start = (page-1)*10    
    end = page*10
    
    if request.method == 'POST':
        opc = int(request.POST['search_options'])
        text = request.POST['search']                         
        if text:
            all_estudiantes = buscar_estudiante(all_estudiantes, text, opc)            
            estudiantes = all_estudiantes
            start = 0
            end = estudiantes.count()
            totalE = all_estudiantes.count()            
            asesorI = '.'    
            search = '.'             
            context = {'group': group, 'estudiantes': estudiantes, 'totalE': totalE, 'page': page, 'start': start+1, 'end': end, 'orderB': orderB, 'search': search}
            return render(request, 'Admin/estudiantes.html', context)   
                
    all_estudiantes = ordenar_estudiantes(all_estudiantes, orderB)
    estudiantes = all_estudiantes[start:end]
    if end != estudiantes.count():
        end = end-10+estudiantes.count()
    totalE = all_estudiantes.count()
    n_buttons = math.ceil(totalE/10)
    buttons = [item for item in range(1, n_buttons+1)]
    next_page = page+1
    prev_page = page-1    
    context = {'group': group, 'estudiantes': estudiantes, 'totalE': totalE, 'buttons': buttons, 'page': page, 'start': start+1, 'end': end, 'next_page': next_page, 'prev_page': prev_page, 'n_buttons': n_buttons, 'orderB': orderB}
    return render(request, 'Admin/estudiantes.html', context)        

@admin_only
def docentes(request, page, orderB):
    group = request.user.groups.all()[0].name    
    all_docentes = Docente.objects.all()
    start = (page-1)*10    
    end = page*10
    
    if request.method == 'POST':
        opc = int(request.POST['search_options'])
        text = request.POST['search'] 
                        
        if text:
            all_docentes = buscar_docente(all_docentes, text, opc)                                                                                            
            docentes = all_docentes
            start = 0
            end = docentes.count()
            totalD = all_docentes.count()                        
            search = '.'      
            context = {'group': group, 'docentes': docentes, 'totalD': totalD, 'page': page, 'start': start+1, 'end': end, 'orderB': orderB, 'search': search}
            return render(request, 'Admin/docentes.html', context)            
            
    all_docentes = ordenar_docentes(all_docentes, orderB)
    docentes = all_docentes[start:end]    
    if end != docentes.count():
        end = end-10+docentes.count()
    totalD = all_docentes.count()
    n_buttons = math.ceil(totalD/10)
    buttons = [item for item in range(1, n_buttons+1)]
    next_page = page+1
    prev_page = page-1    
    context = {'group': group, 'docentes': docentes, 'totalD': totalD, 'buttons': buttons, 'page': page, 'start': start+1, 'end': end, 'next_page': next_page, 'prev_page': prev_page, 'n_buttons': n_buttons, 'orderB': orderB}
    return render(request, 'Admin/docentes.html', context)     

@publicView
def verAnteproyecto(request, pk):
    group = request.user.groups.all()[0].name
    anteproyecto = Anteproyecto.objects.get(id = pk)    
    estudiantes = Estudiante.objects.filter(anteproyecto = anteproyecto)        
    revisor1 = anteproyecto.revisor1 
    revisor2 = anteproyecto.revisor2                
    dependencia = anteproyecto.dependencia 
    observacion = anteproyecto.observacion
    estadoInicial = anteproyecto.estatus
    fechaObservacion = None
    observaciones = None
    dias = 0
    fechaObservacion = None
    fechaCorte = None
    fechaActual = date.today
    fechaObservacion = None
    data = ['id_mision']        
    lista = ['ENVIADO', 'PENDIENTE', 'EN REVISION', 'REVISADO' ,'RECHAZADO']
    
    if observacion:
        fechaObservacion = observacion.fechaCreacion    
        observaciones = ObservacionDocente.objects.filter(observacion = observacion)                                
        dias = 5 + observacion.incrementarDias
        fechaObservacion = fechaObservacion + timedelta(days=dias)           
        fechaCorte = fechaObservacion + timedelta(days=1)                     
        fechaObservacion = fechaObservacion.strftime("%d/%b/%Y")                   
    
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
            estadoFinal = formEstado['estatus'].value()        
            if estadoInicial in lista and estadoFinal == 'ACEPTADO':
                residencia = Residencia(
                    dependencia = dependencia,
                    asesorExterno = anteproyecto.asesorExterno,
                    r_asesorInterno = anteproyecto.revisor1,
                    r_revisor = anteproyecto.revisor2,
                    nombre = anteproyecto.a_nombre,
                    tipoProyecto = anteproyecto.tipoProyecto,
                    numIntegrantes = anteproyecto.numIntegrantes,
                    periodoInicio = anteproyecto.periodoInicio,
                    periodoFin = anteproyecto.periodoFin
                )        
                residencia.save()                                                        

                for e in estudiantes:        
                    e.residencia = residencia
                    e.save()
                
                print('RESIDENCIA CREADA')
                
            elif estadoInicial == 'ACEPTADO' and estadoFinal in lista:
                print('Eliminar la residencia')            
                residencia = estudiantes[0].residencia
                residencia.delete()
                print('RESIDENCIA ELMINIDA')
            formEstado.save()
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
        
    context = {'group': group, 'anteproyecto': anteproyecto, 'estudiantes': estudiantes, 'dependencia': dependencia, 'revisor1': revisor1, 'revisor2': revisor2, 'formA': formA, 'formD': formD, 'formT': formT, 'formAE': formAE ,'formDom': formDom, 'formDoc': formDoc, 'fechaObservacion': fechaObservacion, 'observaciones': observaciones, 'formEstado': formEstado, 'data': data}
    return render(request, 'Admin/verAnteproyecto.html', context)           

@admin_only
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

@admin_only
def eliminarAnteproyecto(request, pk):    
    anteproyecto = Anteproyecto.objects.get(id = pk)
    anteproyecto.delete()
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

@admin_only
def eliminarResidencia(request, pk):    
    residencia = Residencia.objects.get(id = pk)
    residencia.delete()
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

@admin_only
def editarObservaciones(request, pk):
    group = request.user.groups.all()[0].name
    docente = request.user.docente
    anteproyecto = Anteproyecto.objects.get(id = pk)
    observacion = anteproyecto.observacion
    fechaObservacion = None
    observaciones = None
    dias = 0
    fechaObservacion = None
    fechaCorte = None
    fechaActual = date.today
    fechaObservacion = None
    
    if observacion:
        fechaObservacion = observacion.fechaCreacion    
        observaciones = ObservacionDocente.objects.filter(observacion = observacion)                                
        dias = 5 + observacion.incrementarDias
        fechaObservacion = fechaObservacion + timedelta(days=dias)           
        fechaCorte = fechaObservacion + timedelta(days=1)                     
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
        
        if observacion:    
            if rDias and rDias > 0:                  
                observacion.incrementarDias += rDias            
                observacion.save()
                
            if rObservacion:            
                nuevaObservacion = ObservacionDocente(
                    docente = docente,
                    observacion = observacion,
                    observacionD = rObservacion
                )
                nuevaObservacion.save()            
        else:                            
                
            if rObservacion:            
                observacion = Observacion()
                observacion.save()
                anteproyecto.observacion = observacion
                anteproyecto.save()        
                nuevaObservacion = ObservacionDocente(
                    docente = docente,
                    observacion = observacion,
                    observacionD = rObservacion
                )
                nuevaObservacion.save()            
                                    
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))                    
    
    context = {'anteproyecto': anteproyecto, 'estudiantes': estudiantes, 'group': group, 'observaciones': observaciones, 'fechaObservacion': fechaObservacion, 'fechaCorte': fechaCorte, 'fechaActual': fechaActual}    
    return render(request, 'Admin/editObservaciones.html', context)        

@admin_only
def eliminarObservacion(request, pk):    
    observacion = ObservacionDocente.objects.get(id = pk)    
    observacion.delete()    
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))    

@publicView
def verEstudiante(request, pk):
    group = request.user.groups.all()[0].name
    estudiante = Estudiante.objects.get(id = pk)
    domicilio = estudiante.domicilio    
    anteproyecto = estudiante.anteproyecto
    residencia = estudiante.residencia
    expediente = estudiante.expediente
    
    context = {'group': group, 'estudiante': estudiante, 'domicilio': domicilio, 'anteproyecto': anteproyecto, 'residencia': residencia, 'expediente': expediente,}    
    return render(request, 'Admin/verEstudiante.html', context)        

@admin_only
def editarEstudiante(request, pk):
    group = request.user.groups.all()[0].name
    estudiante = Estudiante.objects.get(id = pk)
    anteproyecto = estudiante.anteproyecto
    domicilio = estudiante.domicilio
    
    formE = EstudianteForm(instance=estudiante)
    formD = DomicilioForm(instance=domicilio)
    
    if request.method == 'POST':
        formE = EstudianteForm(request.POST, instance=estudiante)
        formD = DomicilioForm(request.POST, instance=domicilio)
    
        if formE.is_valid():
            formE.save()
            
        if formD.is_valid():
            formD.save()
    
        return redirect('verEstudiante', estudiante.id)
    
    context = {'group': group, 'estudiante': estudiante, 'anteproyecto': anteproyecto, 'formE': formE, 'formD': formD}    
    return render(request, 'Student/settings.html', context)        

@admin_only
def removeEstudiante(request, pk):    
    estudiante = Estudiante.objects.get(id = pk)
    estudiante.anteproyecto = None
    estudiante.save()  
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

@admin_only
def asignarRevisor1(request, page, pk):
    group = request.user.groups.all()[0].name
    anteproyecto = Anteproyecto.objects.get(id = pk)    
    all_docentes = Docente.objects.all()        
    start = (page-1)*10    
    end = page*10
    
    if request.method == 'POST':
        opc = int(request.POST['search_options'])
        text = request.POST['search'] 
                        
        if text:
            all_docentes = buscar_docente(all_docentes, text, opc)                        
            docentes = all_docentes
            start = 0
            end = docentes.count()
            totalD = all_docentes.count()            
            revisor1 = '.'                 
            context = {'group': group, 'anteproyecto': anteproyecto, 'revisor1': revisor1, 'docentes': docentes, 'totalD': totalD, 'page': page, 'start': start+1, 'end': end}    
            return render(request, 'Admin/asignarDocente.html', context)                    
    
    docentes = all_docentes[start:end]    
    if end != docentes.count():
        end = end-10+docentes.count()
    totalD = all_docentes.count()
    n_buttons = math.ceil(totalD/10)
    buttons = [item for item in range(1, n_buttons+1)]
    next_page = page+1
    prev_page = page-1            
    revisor1 = '.'
    
    context = {'group': group, 'docentes': docentes, 'anteproyecto': anteproyecto, 'revisor1': revisor1, 'totalD': totalD, 'buttons': buttons, 'page': page, 'start': start+1, 'end': end, 'next_page': next_page, 'prev_page': prev_page, 'n_buttons': n_buttons}
    return render(request, 'Admin/asignarDocente.html', context)        

@admin_only
def asignarRevisor1I(request, pkA, pkD):        
    anteproyecto = Anteproyecto.objects.get(id = pkA)
    docente = Docente.objects.get(id = pkD)
    anteproyecto.revisor1 = docente
    revisor2 = anteproyecto.revisor2
    if revisor2 and anteproyecto.estatus != 'ACEPTADO':
        anteproyecto.estatus = 'EN REVISION'
    anteproyecto.save()    
        
    return redirect('verAnteproyecto', anteproyecto.id)

@admin_only
def removeRevisor1(request, pk):
    anteproyecto = Anteproyecto.objects.get(id = pk)
    anteproyecto.revisor1 = None
    anteproyecto.save()
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

@admin_only
def asignarRevisor2(request, page, pk):
    group = request.user.groups.all()[0].name
    anteproyecto = Anteproyecto.objects.get(id = pk)
    all_docentes = Docente.objects.all()        
    start = (page-1)*10    
    end = page*10
    
    if request.method == 'POST':
        opc = int(request.POST['search_options'])
        text = request.POST['search'] 
                        
        if text:
            all_docentes = buscar_docente(all_docentes, text, opc)                                    
            docentes = all_docentes
            start = 0
            end = docentes.count()
            totalD = all_docentes.count()            
            revisor2 = '.'                 
            context = {'group': group, 'anteproyecto': anteproyecto, 'revisor2': revisor2, 'docentes': docentes, 'totalD': totalD, 'page': page, 'start': start+1, 'end': end}    
            return render(request, 'Admin/asignarDocente.html', context)                    
    
    docentes = all_docentes[start:end]    
    if end != docentes.count():
        end = end-10+docentes.count()
    totalD = all_docentes.count()
    n_buttons = math.ceil(totalD/10)
    buttons = [item for item in range(1, n_buttons+1)]
    next_page = page+1
    prev_page = page-1            
    
    revisor2 = '.'
    context = {'group': group, 'docentes': docentes, 'anteproyecto': anteproyecto, 'revisor2': revisor2, 'totalD': totalD, 'buttons': buttons, 'page': page, 'start': start+1, 'end': end, 'next_page': next_page, 'prev_page': prev_page, 'n_buttons': n_buttons}
    return render(request, 'Admin/asignarDocente.html', context)        

@admin_only
def asignarRevisor2I(request, pkA, pkD):        
    anteproyecto = Anteproyecto.objects.get(id = pkA)
    docente = Docente.objects.get(id = pkD)
    anteproyecto.revisor2 = docente
    revisor1 = anteproyecto.revisor1
    if revisor1 and anteproyecto.estatus != 'ACEPTADO':
        anteproyecto.estatus = 'EN REVISION'
    anteproyecto.save()        
    return redirect('verAnteproyecto', anteproyecto.id)

@admin_only
def removeRevisor2(request, pk):
    anteproyecto = Anteproyecto.objects.get(id = pk)
    anteproyecto.revisor2 = None
    anteproyecto.save()
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

@publicView
def verDocente(request, pk):
    group = request.user.groups.all()[0].name
    docente = Docente.objects.get(id = pk)   
    all_anteproyectos = Anteproyecto.objects.all()
    all_residencias = Residencia.objects.all()
    
    try:
        perfilAcademico = docente.perfilAcademico
        materias = perfilAcademico.materias.all()        
    except:
        perfilAcademico = None
        materias = None
    
    anteproyectos_activos_r1 = all_anteproyectos.filter(revisor1=docente).exclude(estatus__in=['ACEPTADO', 'RECHAZADO'])
    anteproyectos_activos_r2 = all_anteproyectos.filter(revisor2=docente).exclude(estatus__in=['ACEPTADO', 'RECHAZADO'])
    
    residencias_activas_a = all_residencias.filter(r_asesorInterno=docente).exclude(estatus__in=['FINALIZADA', 'RECHAZADA', 'NO FINALIZADA'])
    residencias_activas_r = all_residencias.filter(r_revisor=docente).exclude(estatus__in=['FINALIZADA', 'RECHAZADA', 'NO FINALIZADA'])
    
    anteproyectos_pasados_r1 = all_anteproyectos.filter(estatus='ACEPTADO', revisor1=docente)
    anteproyectos_pasados_r2 = all_anteproyectos.filter(estatus='ACEPTADO', revisor2=docente)
    
    residencias_pasadas_a = all_residencias.filter(estatus='FINALIZADA', r_asesorInterno=docente)
    residencias_pasadas_r = all_residencias.filter(estatus='FINALIZADA', r_revisor=docente)
        
    for i in residencias_activas_a:
        print(i.nombre)
    
    for i in residencias_activas_r:
        print(i.nombre)
         
    actividad_docente = [anteproyectos_activos_r1.count() + anteproyectos_activos_r2.count(),
                         residencias_activas_a.count() + residencias_activas_r.count(), 
                         residencias_activas_a.count(), 
                         anteproyectos_pasados_r1.count() + anteproyectos_pasados_r2.count(), 
                         residencias_pasadas_a.count() + residencias_pasadas_r.count(), 
                         residencias_activas_r.count()
                         ]
            
    context = {'group': group, 'docente': docente, 'actividad_docente': actividad_docente, 'materias': materias}        
    return render(request, 'Admin/verDocente.html', context)    

@admin_only
def editarDocente(request, pk):
    group = request.user.groups.all()[0].name
    docente = Docente.objects.get(id = pk)
    formD = DocenteForm(instance=docente)
    
    if request.method == 'POST':
        formD = DocenteForm(request.POST, instance=docente)
        if formD.is_valid():
            formD.save()
            return redirect('verDocente', docente.id)
            
    
    context = {'group': group, 'docente': docente, 'formD': formD}
    return render(request, 'Admin/editarDocente.html', context)        

@admin_only
def altaDocente(request):
    group = request.user.groups.all()[0].name
    data = ['id_fotoUsuario', 'id_correoElectronico']
    formD = DocenteForm()
    formU = CreateUserForm()
    
    if request.method == 'POST':
        formD = DocenteForm(request.POST)
        formU = CreateUserForm(request.POST)
        
        if formD.is_valid() and formU.is_valid():
            teacher = formD.save()
            user = formU.save()
            group = Group.objects.get(name='teacher')
            user.groups.add(group)
            teacher.correoElectronico = formU.cleaned_data.get('email')            
            teacher.user = user
            teacher.save()
            
            return redirect('docentes', 1, 0)
    
    context = {'group': group, 'formD': formD, 'formU': formU, 'data': data}
    return render(request, 'Admin/altaDocente.html', context)        

@publicView
def verResidencia(request, pk):
    group = request.user.groups.all()[0].name
    data = ['id_mision']        
    residencia = Residencia.objects.get(id = pk)
    estudiantes = Estudiante.objects.filter(residencia = residencia)                
    asesorI = residencia.r_asesorInterno
    revisor = residencia.r_revisor
    dependencia = residencia.dependencia
    formR = ResidenciaViewForm(instance = residencia)                                
    formD = DependenciaViewForm(instance = dependencia)
    formER = ResidenciaEstadoForm(instance = residencia)
    
    if request.method == 'POST':
        formER = ResidenciaEstadoForm(request.POST, instance = residencia)        
        if formER.is_valid():  
            formER.save()      
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))    
            
    context = {'group': group, 'residencia': residencia, 'estudiantes': estudiantes, 'asesorI': asesorI, 'revisor': revisor, 'dependencia': dependencia, 'formR': formR, 'formD': formD, 'formER': formER, 'data': data,}
    return render(request, 'Admin/verResidencia.html', context)        

@admin_only
def editarResidenciaAdmin(request, pk):
    group = request.user.groups.all()[0].name
    residencia = Residencia.objects.get(id = pk)    
    estudiantes = Estudiante.objects.filter(residencia = residencia).count()        
    dependencia = residencia.dependencia
    asesorExterno = residencia.asesorExterno
    titular = dependencia.titular
    domicilio = dependencia.domicilio    
    numIntegrantes = residencia.numIntegrantes
    mensaje = ''    
    
    formR = ResidenciaForm(instance = residencia)                                
    formD = DependenciaForm(instance = dependencia)
    formT = TitularForm(instance = titular)
    formDom = DomicilioForm(instance = domicilio)
    formAE = AsesorEForm(instance = asesorExterno)    
    
    if request.method == 'POST':                        
        formR = ResidenciaForm(request.POST, instance = residencia)                                
        formD = DependenciaForm(request.POST, instance = dependencia)
        formT = TitularForm(request.POST, instance = titular)
        formDom = DomicilioForm(request.POST, instance = domicilio)
        formAE = AsesorEForm(request.POST, instance = asesorExterno)   
                  
        if formR.is_valid() and formD.is_valid() and formT.is_valid() and formAE.is_valid() and formDom.is_valid():
            numIntegrantes2 = int(formR['numIntegrantes'].value())                                    
            if numIntegrantes2 < 1:
                mensaje = 'El numero de integrantes no puede ser menor a 1'
            else:                                                                                                                                                                                  
                if numIntegrantes > numIntegrantes2 and estudiantes > numIntegrantes2:                                        
                    mensaje = 'No se puede reducir el numero de integrantes. Eliminine algun integrante del anteproyecto para poder reducir el numero de integrantes'                    
                else:                                                
                    domicilio = formDom.save()                  
                    titular = formT.save()              
                    asesorExterno = formAE.save()      
                    dependencia = formD.save()            
                    residencia = formR.save()
                    residencia.dependencia = dependencia
                    residencia.asesorExterno = asesorExterno                    
                    asesorExterno.dependencia = dependencia
                    asesorExterno.save()                                    
                    residencia.save() 
                    return redirect('verResidencia', pk = residencia.id)                                 
    
    context = {'group': group, 'formR': formR, 'formD': formD, 'formT': formT, 'formDom': formDom, 'formAE': formAE, 'residencia': residencia, 'mensaje':mensaje}    
    return render(request, 'Admin/editarResidencia.html', context)        

@admin_only
def asignarAsesorIL(request, page, pk):
    group = request.user.groups.all()[0].name
    residencia = Residencia.objects.get(id = pk)        
    all_docentes = Docente.objects.all()        
    start = (page-1)*10    
    end = page*10
    
    if request.method == 'POST':
        opc = int(request.POST['search_options'])
        text = request.POST['search'] 
                        
        if text:
            all_docentes = buscar_docente(all_docentes, text, opc)                                    
            docentes = all_docentes
            start = 0
            end = docentes.count()
            totalD = all_docentes.count()            
            asesorI = '.'                 
            context = {'group': group, 'residencia': residencia, 'asesorI': asesorI, 'docentes': docentes, 'totalD': totalD, 'page': page, 'start': start+1, 'end': end}    
            return render(request, 'Admin/asignarDocente.html', context)                    
        
    docentes = all_docentes[start:end]    
    if end != docentes.count():
        end = end-10+docentes.count()
    totalD = all_docentes.count()
    n_buttons = math.ceil(totalD/10)
    buttons = [item for item in range(1, n_buttons+1)]
    next_page = page+1
    prev_page = page-1        
    asesorI = '.'
    context = {'group': group, 'residencia': residencia, 'asesorI':asesorI, 'docentes': docentes, 'totalD': totalD, 'buttons': buttons, 'page': page, 'start': start+1, 'end': end, 'next_page': next_page, 'prev_page': prev_page, 'n_buttons': n_buttons}
    return render(request, 'Admin/asignarDocente.html', context)            

@admin_only
def asignarAsesorI(request, pkR, pkD):
    residencia = Residencia.objects.get(id = pkR)
    docente = Docente.objects.get(id = pkD)
    residencia.r_asesorInterno = docente
    residencia.save()
    return redirect('verResidencia', residencia.id)

@admin_only
def removeAsesorI(request, pk):
    residencia = Residencia.objects.get(id = pk)
    residencia.r_asesorInterno = None
    residencia.save()
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

@admin_only
def asignarRevisorL(request, page, pk):
    group = request.user.groups.all()[0].name
    residencia = Residencia.objects.get(id = pk)    
    all_docentes = Docente.objects.all()        
    start = (page-1)*10    
    end = page*10                        
    
    if request.method == 'POST':
        opc = int(request.POST['search_options'])
        text = request.POST['search'] 
                        
        if text:
            all_docentes = buscar_docente(all_docentes, text, opc)                                    
            docentes = all_docentes
            start = 0
            end = docentes.count()
            totalD = all_docentes.count()            
            revisor = '.'                 
            context = {'group': group, 'residencia': residencia, 'revisor': revisor, 'docentes': docentes, 'totalD': totalD, 'page': page, 'start': start+1, 'end': end}    
            return render(request, 'Admin/asignarDocente.html', context)                    
    
    docentes = all_docentes[start:end]        
    if end != docentes.count():
        end = end-10+docentes.count()
    totalD = all_docentes.count()
    n_buttons = math.ceil(totalD/10)
    buttons = [item for item in range(1, n_buttons+1)]
    next_page = page+1
    prev_page = page-1        
    revisor = '.'        
    
    context = {'group': group, 'residencia': residencia, 'revisor': revisor, 'docentes': docentes, 'totalD': totalD, 'buttons': buttons, 'page': page, 'start': start+1, 'end': end, 'next_page': next_page, 'prev_page': prev_page, 'n_buttons': n_buttons}    
    return render(request, 'Admin/asignarDocente.html', context)            

@admin_only
def asignarRevisor(request, pkR, pkD):
    residencia = Residencia.objects.get(id = pkR)
    docente = Docente.objects.get(id = pkD)
    residencia.r_revisor = docente
    residencia.save()
    return redirect('verResidencia', residencia.id)

@admin_only
def removeRevisor(request, pk):
    residencia = Residencia.objects.get(id = pk)
    residencia.r_revisor = None
    residencia.save()
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

@admin_only
def eliminarEstudiante(request, pk):
    estudiante = Estudiante.objects.get(id = pk)
    estudiante.delete()
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

@admin_only
def eliminarDocente(request, pk):
    docente = Docente.objects.get(id = pk)
    docente.delete()
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

@admin_only
def eliminarDocExpediente(request, pk, file_name):    
    expediente = Expediente.objects.get(id = pk)        
    file_name = file_name.replace('id_', '')    
    archivo = getattr(expediente,file_name)
    archivo.delete()    
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

@admin_only
def eliminarDocR1(request, pk, file_name):
    reporte = ReporteParcial1.objects.get(pk=pk)
    file_name = file_name.replace(' ', '')    
    letter = file_name[0]
    letter = letter.lower()
    file_name = file_name.replace(file_name[0], letter, 1)
    str = 'r1_'
    file_name = str + file_name
    archivo = getattr(reporte,file_name)
    archivo.delete()    
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

@admin_only
def eliminarDocR2(request, pk, file_name):
    reporte = ReporteParcial2.objects.get(pk=pk)
    file_name = file_name.replace(' ', '')    
    letter = file_name[0]
    letter = letter.lower()
    file_name = file_name.replace(file_name[0], letter, 1)
    str = 'r2_'
    file_name = str + file_name
    archivo = getattr(reporte,file_name)
    archivo.delete()    
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

@admin_only
def eliminarDocRF(request, pk, file_name):
    reporte = ReporteFinal.objects.get(pk=pk)
    file_name = file_name.replace(' ', '')    
    letter = file_name[0]
    letter = letter.lower()
    file_name = file_name.replace(file_name[0], letter, 1)
    str = 'rf_'
    file_name = str + file_name
    archivo = getattr(reporte,file_name)
    archivo.delete()    
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

def filtrar_anteproyectos(anteproyectos, filter):
    all_anteproyectos = anteproyectos
    if filter == 1:
        all_anteproyectos = anteproyectos.filter(estatus = 'ACEPTADO')
    elif filter == 2:
        all_anteproyectos = anteproyectos.filter(estatus = 'ENVIADO')
    elif filter == 3:
        all_anteproyectos = anteproyectos.filter(estatus = 'PENDIENTE')
    elif filter == 4:
        all_anteproyectos = anteproyectos.filter(estatus = 'EN REVISION')
    elif filter == 5:
        all_anteproyectos = anteproyectos.filter(estatus = 'REVISADO')
    elif filter == 6:
        all_anteproyectos = anteproyectos.filter(estatus = 'RECHAZADO')
    return all_anteproyectos

def ordenar_anteproyectos(anteproyectos, orderB):
    all_anteproyectos = anteproyectos           
    if orderB == 1:
        all_anteproyectos = all_anteproyectos.order_by('a_nombre')    
    elif orderB == 2:
        all_anteproyectos = all_anteproyectos.order_by('-a_nombre')        
    elif orderB == 3:
        all_anteproyectos = all_anteproyectos.order_by('periodoInicio')    
    elif orderB == 4:
        all_anteproyectos = all_anteproyectos.order_by('-periodoInicio')    
    elif orderB == 5:
        all_anteproyectos = all_anteproyectos.order_by('periodoFin')    
    elif orderB == 6:
        all_anteproyectos = all_anteproyectos.order_by('-periodoFin')        
    return all_anteproyectos

def buscar_anteproyecto(anteproyectos, text, opc):
    all_anteproyectos = anteproyectos
    if opc == 1:                
        all_anteproyectos = all_anteproyectos.filter(a_nombre__icontains=text)
    elif opc == 2:                
        dependencias = Dependencia.objects.filter(d_nombre__icontains=text)
        all_anteproyectos = all_anteproyectos.filter(dependencia__in=dependencias)
    elif opc == 3:                
        try:
            month_number = int(text)
            if month_number > 0 and month_number <= 12:                        
                all_anteproyectos = all_anteproyectos.filter(periodoInicio__month=month_number)                                                   
            else:
                month_number = None
                all_anteproyectos = all_anteproyectos.filter(periodoInicio__month=month_number)                                                   
        except:                    
            MONTHS = {'ENERO':1, 'FEBRERO':2, 'MARZO':3, 'ABRIL':4, 'MAYO':5, 'JUNIO':6, 'JULIO':7, 'AGOSTO':8, 'SEPTIEMBRE':9, 'OCTUBRE':10, 'NOVIEMBRE':11, 'DICIEMBRE':12}                                                
            try:
                text = text.upper()
                month_number = MONTHS[text]
                all_anteproyectos = all_anteproyectos.filter(periodoInicio__month=month_number)                                                   
            except:
                month_number = None
                all_anteproyectos = all_anteproyectos.filter(periodoInicio__month=month_number)                                                                                       
    elif opc == 4:
        try:
            month_number = int(text)
            if month_number > 0 and month_number <= 12:                        
                all_anteproyectos = all_anteproyectos.filter(periodoFin__month=month_number)                                                   
            else:
                month_number = None
                all_anteproyectos = all_anteproyectos.filter(periodoFin__month=month_number)                                                   
        except:                    
            MONTHS = {'ENERO':1, 'FEBRERO':2, 'MARZO':3, 'ABRIL':4, 'MAYO':5, 'JUNIO':6, 'JULIO':7, 'AGOSTO':8, 'SEPTIEMBRE':9, 'OCTUBRE':10, 'NOVIEMBRE':11, 'DICIEMBRE':12}                                                
            try:
                text = text.upper()
                month_number = MONTHS[text]
                all_anteproyectos = all_anteproyectos.filter(periodoFin__month=month_number)                                                   
            except:
                month_number = None
                all_anteproyectos = all_anteproyectos.filter(periodoFin__month=month_number)                                                                                       
    elif opc == 5:                
        try:
            year = int(text) 
            all_anteproyectos = all_anteproyectos.filter(periodoInicio__year=year)                               
        except:
            text = None                
    elif opc == 6:       
        try:
            year = int(text) 
            all_anteproyectos = all_anteproyectos.filter(periodoFin__year=year)                               
        except:
            text = None         
    
    return all_anteproyectos 

def filtrar_residencias(residencias, filter):
    all_residencias = residencias
    if filter == 1:
        all_residencias = all_residencias.filter(estatus = 'INICIADA')
    elif filter == 2:
        all_residencias = all_residencias.filter(estatus = 'FINALIZADA')
    elif filter == 3:
        all_residencias = all_residencias.filter(estatus = 'EN PROCESO')
    elif filter == 4:
        all_residencias = all_residencias.filter(estatus = 'RECHAZADA')
    elif filter == 5:
        all_residencias = all_residencias.filter(estatus = 'PROROGA')    
    return all_residencias

def ordenar_residencias(residencias, orderB):
    all_residencias = residencias
    if orderB == 1:
        all_residencias = all_residencias.order_by('nombre')    
    elif orderB == 2:
        all_residencias = all_residencias.order_by('-nombre')        
    elif orderB == 3:
        all_residencias = all_residencias.order_by('periodoInicio')    
    elif orderB == 4:
        all_residencias = all_residencias.order_by('-periodoInicio')    
    elif orderB == 5:
        all_residencias = all_residencias.order_by('periodoFin')    
    elif orderB == 6:
        all_residencias = all_residencias.order_by('-periodoFin')        
    return all_residencias

def buscar_residencia(residencias, text, opc):
    all_residencias = residencias
    if opc == 1:                
        all_residencias = all_residencias.filter(nombre__icontains=text)
    elif opc == 2:                
        dependencias = Dependencia.objects.filter(d_nombre__icontains=text)
        all_residencias = all_residencias.filter(dependencia__in=dependencias)
    elif opc == 3:                
        try:
            month_number = int(text)
            if month_number > 0 and month_number <= 12:                        
                all_residencias = all_residencias.filter(periodoInicio__month=month_number)                                                   
            else:
                month_number = None
                all_residencias = all_residencias.filter(periodoInicio__month=month_number)                                                   
        except:                    
            MONTHS = {'ENERO':1, 'FEBRERO':2, 'MARZO':3, 'ABRIL':4, 'MAYO':5, 'JUNIO':6, 'JULIO':7, 'AGOSTO':8, 'SEPTIEMBRE':9, 'OCTUBRE':10, 'NOVIEMBRE':11, 'DICIEMBRE':12}                                                
            try:
                text = text.upper()
                month_number = MONTHS[text]
                all_residencias = all_residencias.filter(periodoInicio__month=month_number)                                                   
            except:
                month_number = None
                all_residencias = all_residencias.filter(periodoInicio__month=month_number)                                                   

    elif opc == 4:
        try:
            month_number = int(text)
            if month_number > 0 and month_number <= 12:                        
                all_residencias = all_residencias.filter(periodoFin__month=month_number)                                                   
            else:
                month_number = None
                all_residencias = all_residencias.filter(periodoFin__month=month_number)                                                   
        except:                    
            MONTHS = {'ENERO':1, 'FEBRERO':2, 'MARZO':3, 'ABRIL':4, 'MAYO':5, 'JUNIO':6, 'JULIO':7, 'AGOSTO':8, 'SEPTIEMBRE':9, 'OCTUBRE':10, 'NOVIEMBRE':11, 'DICIEMBRE':12}                                                
            try:
                text = text.upper()
                month_number = MONTHS[text]
                all_residencias = all_residencias.filter(periodoFin__month=month_number)                                                   
            except:
                month_number = None
                all_residencias = all_residencias.filter(periodoFin__month=month_number)                                                   

    elif opc == 5:                
        try:
            year = int(text) 
            all_residencias = all_residencias.filter(periodoInicio__year=year)                               
        except:
            year = None     
            all_residencias = all_residencias.filter(periodoInicio__year=year)                                          
    elif opc == 6:       
        try:
            year = int(text) 
            all_residencias = all_residencias.filter(periodoFin__year=year)                               
        except:
            year = None         
            all_residencias = all_residencias.filter(periodoFin__year=year)                                                                  
    return all_residencias

def filtrar_expedientes(estudiantes, filter):
    all_expedientes = Expediente.objects.all()
    all_estudiantes = estudiantes        
    if filter == 1:
        all_expedientes = all_expedientes.filter(estatus = 'INICIAL')
    elif filter == 2:
        all_expedientes = all_expedientes.filter(estatus = 'PROCESO')
    elif filter == 3:
        all_expedientes = all_expedientes.filter(estatus = 'COMPLETO')        
    all_estudiantes = all_estudiantes.filter(expediente__in = all_expedientes)    
    return all_estudiantes

def ordenar_estudiantes(estudiantes, orderB):
    all_estudiantes = estudiantes                
    if orderB == 1:
        all_estudiantes = all_estudiantes.order_by('semestre')    
    elif orderB == 2:
        all_estudiantes = all_estudiantes.order_by('-semestre')    
    elif orderB == 3:
        all_estudiantes = all_estudiantes.order_by('numControl')        
    elif orderB == 4:
        all_estudiantes = all_estudiantes.order_by('-numControl')    
    elif orderB == 5:
        all_estudiantes = all_estudiantes.order_by('apellidoP')    
    elif orderB == 6:
        all_estudiantes = all_estudiantes.order_by('-apellidoP')    
    else:
        all_estudiantes = all_estudiantes          
    return all_estudiantes
    
def buscar_estudiante(estudiantes ,text, opc):
    all_estudiantes = estudiantes    
    if text:
        if opc == 1:                
            all_estudiantes = all_estudiantes.filter(numControl__icontains=text)
        elif opc == 2:                
            all_estudiantes = all_estudiantes.filter(nombre__icontains=text)
        elif opc == 3:                
            all_estudiantes = all_estudiantes.filter(apellidoP__icontains=text)
        elif opc == 4:
            all_estudiantes = all_estudiantes.filter(apellidoM__icontains=text)
        elif opc == 5: 
            try:               
                all_estudiantes = all_estudiantes.filter(semestre=text)
            except: 
                all_estudiantes = all_estudiantes.filter(semestre=None)
    
    return all_estudiantes

def ordenar_docentes(docentes, orderB):
    all_docentes = docentes
    if orderB == 1:
        all_docentes = all_docentes.order_by('nombre')    
    elif orderB == 2:
        all_docentes = all_docentes.order_by('-nombre')    
    elif orderB == 3:
        all_docentes = all_docentes.order_by('apellidoP')        
    elif orderB == 4:
        all_docentes = all_docentes.order_by('-apellidoP')    
    elif orderB == 5:
        all_docentes = all_docentes.order_by('rfc')    
    elif orderB == 6:
        all_docentes = all_docentes.order_by('-rfc')        
    return all_docentes

def buscar_docente(docentes, text, opc):    
    all_docentes = docentes
    if opc == 1:                
        all_docentes = all_docentes.filter(nombre__icontains=text)            
    elif opc == 2:                
        all_docentes = all_docentes.filter(apellidoP__icontains=text)
    elif opc == 3:
        all_docentes = all_docentes.filter(apellidoM__icontains=text)            
    elif opc == 4:
        all_docentes = all_docentes.filter(rfc__icontains=text)            
        
    return all_docentes
