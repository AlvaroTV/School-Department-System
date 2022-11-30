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
#from .views import generarCodigo, obtenerCodigo, buscarCodigo
from .adminViews import filtrar_anteproyectos, ordenar_anteproyectos, filtrar_residencias, ordenar_residencias
# Create your views here.

def plantilla(request):
    group = request.user.groups.all()[0].name
    docente = request.user.docente
    context = {'group': group}    
    return render(request, 'Teacher/materias.html', context)

def teacherProfile(request):
    group = request.user.groups.all()[0].name
    docente = request.user.docente
    try:
        perfilAcademico = docente.perfilAcademico
        materias = perfilAcademico.materias.all()        
    except:
        perfilAcademico = None
        materias = None
    
    context = {'group': group, 'docente': docente, 'materias': materias}    
    return render(request, 'Teacher/profile.html', context)

def teacherSettings(request):
    group = request.user.groups.all()[0].name
    docente = request.user.docente        
    try:
        perfilAcademico = docente.perfilAcademico
        materias = perfilAcademico.materias.all()
    except:
        perfilAcademico = None
        materias = None
        
    formD = DocenteForm(instance=docente)
    
    if request.method == 'POST':
        formD = DocenteForm(request.POST, request.FILES ,instance=docente)
        if formD.is_valid():
            formD.save()
            return redirect('teacherProfile')
        
    context = {'group': group, 'docente': docente, 'formD': formD, 'materias': materias}    
    return render(request, 'Teacher/settings.html', context)

def anteproyectosTeacher(request):
    group = request.user.groups.all()[0].name
    docente = request.user.docente
    estados = ['ACEPTADO', 'RECHAZADO']
    all_anteproyectosR1 = Anteproyecto.objects.filter(revisor1=docente).exclude(estatus__in=estados).order_by('periodoInicio')
    all_anteproyectosR2 = Anteproyecto.objects.filter(revisor2=docente).exclude(estatus__in=estados).order_by('periodoInicio')            
    
    context = {'group': group, 'all_anteproyectosR1': all_anteproyectosR1, 'all_anteproyectosR2': all_anteproyectosR2}    
    return render(request, 'Teacher/anteproyectos.html', context)

def anteproyectosH(request, page1, page2, orderB1, orderB2, filter1, filter2):
    group = request.user.groups.all()[0].name
    docente = request.user.docente
    estados = ['ACEPTADO', 'RECHAZADO']
    all_anteproyectosR1 = Anteproyecto.objects.filter(revisor1=docente, estatus__in=estados)
    all_anteproyectosR2 = Anteproyecto.objects.filter(revisor2=docente, estatus__in=estados)
    
    start1 = (page1-1)*10    
    end1 = page1*10
    
    start2 = (page2-1)*10    
    end2 = page2*10
    
    all_anteproyectosR1 = filtrar_anteproyectos(all_anteproyectosR1, filter1)
    all_anteproyectosR1 = ordenar_anteproyectos(all_anteproyectosR1, orderB1)
    all_anteproyectosR1 = all_anteproyectosR1[start1:end1]    
    if end1 != all_anteproyectosR1.count():
        end1 = end1-10+all_anteproyectosR1.count()
    totalA1 = all_anteproyectosR1.count()
    n_buttons1 = math.ceil(totalA1/10)
    buttons1 = [item for item in range(1, n_buttons1+1)]
    next_page1 = page1+1
    prev_page1 = page1-1    
    
    all_anteproyectosR2 = filtrar_anteproyectos(all_anteproyectosR2, filter2)
    all_anteproyectosR2 = ordenar_anteproyectos(all_anteproyectosR2, orderB2)
    all_anteproyectosR2 = all_anteproyectosR2[start2:end2]  
    if end2 != all_anteproyectosR2.count():
        end2 = end2-10+all_anteproyectosR2.count()  
    totalA2 = all_anteproyectosR2.count()
    n_buttons2 = math.ceil(totalA2/10)
    buttons2 = [item for item in range(1, n_buttons2+1)]
    next_page2 = page2+1
    prev_page2 = page2-1        
    
        
    context = {'group': group, 'all_anteproyectosR1': all_anteproyectosR1, 'all_anteproyectosR2': all_anteproyectosR2, 'totalA1': totalA1, 'totalA2': totalA2, 'buttons1': buttons1, 'buttons2': buttons2, 'page1': page1, 'page2': page2, 'start1': start1+1, 'start2': start2+1, 'end1': end1, 'end2': end2, 'next_page1': next_page1, 'next_page2': next_page2, 'prev_page1': prev_page1, 'prev_page2': prev_page2, 'n_buttons1': n_buttons1, 'n_buttons2': n_buttons2, 'orderB1': orderB1, 'orderB2': orderB2, 'filter1': filter1, 'filter2': filter2}    
    return render(request, 'Teacher/anteproyectosH.html', context)

def residenciasTeacher(request):
    group = request.user.groups.all()[0].name
    docente = request.user.docente
    estados = ['ACEPTADO', 'RECHAZADO']
    all_residenciasA = Residencia.objects.filter(r_asesorInterno=docente).exclude(estatus__in=estados)
    all_residenciasR = Residencia.objects.filter(r_revisor=docente).exclude(estatus__in=estados)            
    
    context = {'group': group, 'all_residenciasA': all_residenciasA, 'all_residenciasR': all_residenciasR}    
    return render(request, 'Teacher/residencias.html', context)    

def residenciasH(request, page1, page2, orderB1, orderB2, filter1, filter2):
    group = request.user.groups.all()[0].name
    docente = request.user.docente
    estados = ['ACEPTADO', 'RECHAZADO']
    
    all_residenciasA = Residencia.objects.filter(r_asesorInterno=docente, estatus__in=estados)
    all_residenciasR = Residencia.objects.filter(r_revisor=docente, estatus__in=estados)
    
    start1 = (page1-1)*10    
    end1 = page1*10
    
    start2 = (page2-1)*10    
    end2 = page2*10
    
    all_residenciasA = filtrar_residencias(all_residenciasA, filter1)
    all_residenciasA = ordenar_residencias(all_residenciasA, orderB1)
    all_residenciasA = all_residenciasA[start1:end1]    
    if end1 != all_residenciasA.count():
        end1 = end1-10+all_residenciasA.count()
    totalR1 = all_residenciasA.count()
    n_buttons1 = math.ceil(totalR1/10)
    buttons1 = [item for item in range(1, n_buttons1+1)]
    next_page1 = page1+1
    prev_page1 = page1-1   
    
    all_residenciasR = filtrar_residencias(all_residenciasR, filter1)
    all_residenciasR = ordenar_residencias(all_residenciasR, orderB1)
    all_residenciasR = all_residenciasR[start2:end2]    
    if end2 != all_residenciasR.count():
        end2 = end2-10+all_residenciasR.count()
    totalR2 = all_residenciasR.count()
    n_buttons2 = math.ceil(totalR2/10)
    buttons2 = [item for item in range(1, n_buttons2+1)]
    next_page2 = page2+1
    prev_page2 = page2-1   
    
    context = {'group': group, 'all_residenciasA': all_residenciasA, 'all_residenciasR': all_residenciasR, 'totalR1': totalR1, 'totalR2': totalR2, 'buttons1': buttons1, 'buttons2': buttons2, 'page1': page1, 'page2': page2, 'start1': start1+1, 'start2': start2+1, 'end1': end1, 'end2': end2, 'next_page1': next_page1, 'next_page2': next_page2, 'prev_page1': prev_page1, 'prev_page2': prev_page2, 'n_buttons1': n_buttons1, 'n_buttons2': n_buttons2, 'orderB1': orderB1, 'orderB2': orderB2, 'filter1': filter1, 'filter2': filter2}    
    return render(request, 'Teacher/residenciasH.html', context)

def materias(request):
    group = request.user.groups.all()[0].name
    all_materias = Materia.objects.all()
    
    if group == 'teacher':        
        docente = request.user.docente    
        try:
            perfilAcademico = docente.perfilAcademico        
        except:
            perfilAcademico = None            
        
        try:
            materias = perfilAcademico.materias.all()
        except:        
            materias = None    
    elif group == 'student':
        estudiante = request.user.estudiante
        anteproyecto = estudiante.anteproyecto
        estado = anteproyecto.estatus
        if estado == 'ACEPTADO':
            return redirect('404')
        q_materias = Anteproyecto_materia.objects.filter(anteproyecto=anteproyecto)        
        materias = []
        for m in q_materias:
            materias.append(m.materia)
            print(m.materia)
    else:
        materias = None
        perfilAcademico = None
        
    semestre1 = all_materias.filter(semestre=1)
    semestre2 = all_materias.filter(semestre=2)
    semestre3 = all_materias.filter(semestre=3)
    semestre4 = all_materias.filter(semestre=4)
    semestre5 = all_materias.filter(semestre=5)
    semestre6 = all_materias.filter(semestre=6)
    semestre7 = all_materias.filter(semestre=7)
    semestre8 = all_materias.filter(semestre=8)
    semestre9 = all_materias.filter(semestre=9)    
    
    lengthS1 = semestre1.count()
    lengthS2 = semestre2.count()
    lengthS3 = semestre3.count()
    lengthS4 = semestre4.count()
    lengthS5 = semestre5.count()
    lengthS6 = semestre6.count()
    lengthS7 = semestre7.count()
    lengthS8 = semestre8.count()
    lengthS9 = semestre9.count()
    
    all_semestres = [lengthS1, lengthS2, lengthS3, lengthS4, lengthS5, lengthS6, lengthS7, lengthS8, lengthS9]
    
    rows = max(all_semestres)
    
    all_semestres.clear()
    
    for row in range(rows):
        dataRow = []
        
        try:
            dataRow.append(semestre1[row]) 
        except:
            dataRow.append(None)    
        
        try:
            dataRow.append(semestre2[row]) 
        except:
            dataRow.append(None)    
            
        try:
            dataRow.append(semestre3[row]) 
        except:
            dataRow.append(None)    
        
        try:
            dataRow.append(semestre4[row]) 
        except:
            dataRow.append(None)    
        
        try:
            dataRow.append(semestre5[row]) 
        except:
            dataRow.append(None)    
        
        try:
            dataRow.append(semestre6[row]) 
        except:
            dataRow.append(None)    
            
        try:
            dataRow.append(semestre7[row]) 
        except:
            dataRow.append(None)    
        
        try:
            dataRow.append(semestre8[row]) 
        except:
            dataRow.append(None)    
        
        try:
            dataRow.append(semestre9[row]) 
        except:
            dataRow.append(None)    
            
        all_semestres.append(dataRow)                
    
    context = {'group': group, 'all_semestres': all_semestres, 'materias': materias}    
    return render(request, 'Teacher/materias.html', context)

def tomarRevisor1(request, pk):    
    anteproyecto = Anteproyecto.objects.get(id = pk)
    docente = request.user.docente
    anteproyecto.revisor1 = docente
    revisor2 = anteproyecto.revisor2
    if revisor2:
        anteproyecto.estatus = 'EN REVISION'
    anteproyecto.save()
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))    

def tomarRevisor2(request, pk):    
    anteproyecto = Anteproyecto.objects.get(id = pk)
    docente = request.user.docente
    anteproyecto.revisor2 = docente
    revisor1 = anteproyecto.revisor1
    if revisor1:
        anteproyecto.estatus = 'EN REVISION'
    anteproyecto.save()
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))    

def seleccionarMateria(request, materiaPK):
    group = request.user.groups.all()[0].name
    materia = Materia.objects.get(id = int(materiaPK))    
    docente = request.user.docente        
    perfil_academico = docente.perfilAcademico
    if not perfil_academico:
        perfil_academico = PerfilAcademico()
        perfil_academico.save()
        docente.perfilAcademico = perfil_academico
        docente.save()
        perfil_academico = docente.perfilAcademico
        
    perfil_academico.materias.add(materia)
        
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))    
    
def removeMateria(request, materiaPK):
    docente = request.user.docente
    materia = Materia.objects.get(id = int(materiaPK))
    perfil_academico = docente.perfilAcademico
    perfil_academico.materias.remove(materia)
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))    

def anteproyectoA(request, pk):
    group = request.user.groups.all()[0].name
    docente = request.user.docente
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
    formEstadoR1 = None
    formEstadoR2 = None
    data = ['id_mision']        
    lista = ['ENVIADO', 'PENDIENTE', 'EN REVISION', 'RECHAZADO']
    
    if observacion:
        fechaObservacion = observacion.fechaCreacion    
        observaciones = ObservacionDocente.objects.filter(observacion = observacion).order_by('-id')                                    
        dias = 5 + observacion.incrementarDias
        fechaObservacion = fechaObservacion + timedelta(days=dias)           
        fechaCorte = fechaObservacion + timedelta(days=1)                     
        fechaObservacion = fechaObservacion.strftime("%d/%b/%Y")                   
    
    if anteproyecto.numIntegrantes == 1: data.append('id_codigoUnion')
    
    if revisor1 == docente:        
        editar = True
        formEstadoR1 = AnteproyectoEstadoFormR1(instance = anteproyecto)        
    else:        
        editar = False
        formEstadoR2 = AnteproyectoEstadoFormR2(instance = anteproyecto)        
    
    formA = AnteproyectoViewForm(instance = anteproyecto)                                        
    formD = DependenciaViewForm(instance = dependencia)
    formT = TitularViewForm(instance = dependencia.titular)
    formDom = DomicilioViewForm(instance = dependencia.domicilio)
    formDoc = AnteproyectoDocForm(instance = anteproyecto)
    formAE = AsesorEViewForm(instance = anteproyecto.asesorExterno)             
    
    if request.method == 'POST':        
        if editar:
            formEstadoR1 = AnteproyectoEstadoFormR1(request.POST, instance = anteproyecto)        
            if formEstadoR1.is_valid():
                formEstadoR1.save()
                return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))    
        else:
            formEstadoR2 = AnteproyectoEstadoFormR2(request.POST, instance = anteproyecto)        
            if formEstadoR2.is_valid():
                formEstadoR2.save()
                return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))    
            
    context = {'group': group, 'docente': docente, 'anteproyecto': anteproyecto, 'estudiantes': estudiantes, 'dependencia': dependencia, 'revisor1': revisor1, 'revisor2': revisor2, 'formA': formA, 'formD': formD, 'formT': formT, 'formAE': formAE ,'formDom': formDom, 'formDoc': formDoc, 'fechaObservacion': fechaObservacion, 'observaciones': observaciones, 'formEstadoR1': formEstadoR1, 'formEstadoR2': formEstadoR2, 'data': data, 'editar': editar}    
    return render(request, 'Teacher/anteproyectoA.html', context)

def agregarComentario(request, pk):
    group = request.user.groups.all()[0].name
    docente = request.user.docente
    anteproyecto = Anteproyecto.objects.get(id = pk)
    observacion = anteproyecto.observacion    
    
    if request.method == 'POST':               
        rObservacion = request.POST['Dobservacion']
        
        if observacion:
            nuevaObservacion = ObservacionDocente(
                    docente = docente,
                    observacion = observacion,
                    observacionD = rObservacion
            )
            nuevaObservacion.save()            
        else:
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
            
        return redirect('anteproyectoA', anteproyecto.id)
    
    context = {'group': group, 'anteproyecto': anteproyecto,}    
    return render(request, 'Teacher/addComment.html', context)

def anteproyectoH(request):
    group = request.user.groups.all()[0].name
    docente = request.user.docente
    context = {'group': group}    
    return render(request, 'Teacher/anteproyectoH.html', context)

def residenciaA(request):
    group = request.user.groups.all()[0].name
    docente = request.user.docente
    context = {'group': group}    
    return render(request, 'Teacher/residenciaA.html', context)

def residenciaH(request):
    group = request.user.groups.all()[0].name
    docente = request.user.docente
    context = {'group': group}    
    return render(request, 'Teacher/residenciaH.html', context)

    