from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.contrib.auth.forms import PasswordChangeForm

from django.contrib.auth.forms import PasswordResetForm
from django.utils.http import urlsafe_base64_encode
from django.db.models.query_utils import Q
from django.utils.encoding import force_bytes
from django.core.mail import send_mail, BadHeaderError
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.contrib.auth.tokens import default_token_generator

from django.contrib.auth import update_session_auth_hash
from django.views.decorators.cache import cache_control
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Substr
from django.db.models import Count
from datetime import date, timedelta
from django.utils import timezone
import pytz
import string  
import random  
import math
from .models import *
from .forms import *
from .decorators import *
# Create your views here.

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
@dashboard
def home(request):
    group = request.user.groups.all()[0].name
    all_estudiantes = Estudiante.objects.all()
    all_anteproyectos = Anteproyecto.objects.all()
    all_residencias = Residencia.objects.all()
    docentes = Docente.objects.all().count()
    totalAlumnos = all_estudiantes.count()    
    
    anteproyectosT = all_anteproyectos.count()
    residenciasT = all_residencias.count()
    
    anteproyectosE = all_anteproyectos.filter(estatus = 'ENVIADO').count()
    anteproyectosP = all_anteproyectos.filter(estatus = 'PENDIENTE').count()
    anteproyectosER = all_anteproyectos.filter(estatus = 'EN REVISION').count()
    anteproyectosRE = all_anteproyectos.filter(estatus = 'REVISADO').count()
    anteproyectosA = all_anteproyectos.filter(estatus = 'ACEPTADO').count()
    anteproyectosR = all_anteproyectos.filter(estatus = 'RECHAZADO').count()
    
    residenciasI = all_residencias.filter(estatus = 'INICIADA').count()
    residenciasEP = all_residencias.filter(estatus = 'EN PROCESO').count()
    residenciasP = all_residencias.filter(estatus = 'PROROGA').count()
    residenciasF = all_residencias.filter(estatus = 'FINALIZADA').count()
    
    epedientesC = Expediente.objects.filter(estatus = 'COMPLETO').count()
                          
    generaciones = all_estudiantes.values(generacion = Substr('numControl', 1, 4)).distinct()    
    list_generaciones = []
    cantidad_generaciones = []
    cantidad_anteproyectos = []        
    cantidad_residencias = []    
    cantidadT_anteproyectos = []
    prueba1 = []
    prueba2 = []
    cantidadT_residencias = []   
    anteproyectos_months = []
        
    for g in generaciones:         
        list_generaciones.append(g['generacion'])        
        cantidad_generaciones.append(all_estudiantes.filter(numControl__startswith=g['generacion']).count())        
        cantidad_anteproyectos.append(all_estudiantes.filter(numControl__startswith=g['generacion']).exclude(anteproyecto=None).count())            
        cantidad_residencias.append((all_estudiantes.filter(numControl__startswith=g['generacion']).exclude(residencia=None).count())) 
        prueba1.append(all_estudiantes.filter(numControl__startswith=g['generacion']).exclude(anteproyecto=None)) 
        prueba2.append(((all_estudiantes.filter(numControl__startswith=g['generacion']).exclude(anteproyecto=None)).values('anteproyecto').annotate(dcount=Count('anteproyecto'))).count()) 
        cantidadT_anteproyectos.append(((all_estudiantes.filter(numControl__startswith=g['generacion']).exclude(anteproyecto=None)).values('anteproyecto').annotate(dcount=Count('anteproyecto'))).count()) 
        cantidadT_residencias.append(((all_estudiantes.filter(numControl__startswith=g['generacion']).exclude(residencia=None)).values('residencia').annotate(dcount=Count('residencia'))).count()) 
                    
    
    for i in range(1,13): anteproyectos_months.append(all_anteproyectos.filter(fechaEntrega__month=i).count())
    
    print(anteproyectos_months)
    
    dataPie1 = [list_generaciones, cantidad_generaciones, cantidad_anteproyectos, cantidad_residencias, cantidadT_anteproyectos, cantidadT_residencias]     
        
    
    context = {'group': group, 'totalAlumnos': totalAlumnos, 'anteproyectosE': anteproyectosE, 'anteproyectosT': anteproyectosT, 'anteproyectosP': anteproyectosP, 'anteproyectosER': anteproyectosER, 'anteproyectosRE': anteproyectosRE, 'anteproyectosA': anteproyectosA, 'anteproyectosR': anteproyectosR, 'residenciasI': residenciasI, 'residenciasEP': residenciasEP, 'residenciasP': residenciasP ,'residenciasF': residenciasF, 'docentes': docentes, 'dataPie1': dataPie1, 'anteproyectos_months': anteproyectos_months, 'title': 'Inicio', 'epedientesC': epedientesC}
    return render(request, 'Global/dashboard.html', context)

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def studentPage(request):    
    group = request.user.groups.all()[0].name
    student = request.user.estudiante
    anteproyecto = student.anteproyecto
    proyecto = student.residencia
    expediente = student.expediente  
    
    
    all_avisos = Avisos.objects.all().order_by('-fechaCreacion')  
    if all_avisos:
        for aviso in all_avisos:
            fin_aviso = aviso.fechaCreacion + timedelta(days=aviso.tiempoVida)
            fecha_actual = timezone.now()            
            print(f'Fecha de Creacion: {aviso.fechaCreacion}')
            print(f'Fecha eliminacion: {fin_aviso}')
            print(f'Fehca Actual: {fecha_actual}')
            print('Fechas con el cambio:')
            fin_aviso = convert_to_localtime(fin_aviso)
            fecha_actual = convert_to_localtime(fecha_actual)
            print('Fecha de Creacion: ', convert_to_localtime(aviso.fechaCreacion))            
            print('Fecha eliminacion: ', fin_aviso)            
            print('Fecha Actual: ', fecha_actual)            
            if fecha_actual > fin_aviso:
                print('Eliminar este aviso')
                aviso.delete()
            print('\n================================')
            
    avisosP = all_avisos.filter(estudiante = student)
    avisosT = all_avisos.filter(entidad = 'TODOS')
    avisosE = all_avisos.filter(entidad = 'ESTUDIANTES')
    avisos = avisosP | avisosT | avisosE    
    
    observacion = None
    observaciones = None
    fechaObservacion = None    
        
    try:
        observacion = anteproyecto.observacion
        observaciones = ObservacionDocente.objects.filter(observacion=observacion).order_by('-fechaElaboracion')       
        fechaObservacion = observacion.fechaCreacion            
        dias = 5 + observacion.incrementarDias
        fechaObservacion = fechaObservacion + timedelta(days=dias)                   
        fechaObservacion = fechaObservacion.strftime("%d/%b/%Y")                    
    except:
        pass
    context = {'group': group, 'anteproyecto': anteproyecto, 'proyecto': proyecto, 'expediente': expediente, 'fechaObservacion': fechaObservacion,'observaciones': observaciones, 'avisos':avisos, 'title': 'Inicio'}    
    return render(request, 'Student/dashboard.html', context)

@login_required(login_url='login')
def teacherPage(request):
    group = request.user.groups.all()[0].name
    docente = request.user.docente
    
    all_avisos = Avisos.objects.all().order_by('-fechaCreacion')  
    if all_avisos:
        for aviso in all_avisos:
            fin_aviso = aviso.fechaCreacion + timedelta(days=aviso.tiempoVida)
            fecha_actual = timezone.now()            
            print(f'Fecha de Creacion: {aviso.fechaCreacion}')
            print(f'Fecha eliminacion: {fin_aviso}')
            print(f'Fehca Actual: {fecha_actual}')
            print('Fechas con el cambio:')
            fin_aviso = convert_to_localtime(fin_aviso)
            fecha_actual = convert_to_localtime(fecha_actual)
            print('Fecha de Creacion: ', convert_to_localtime(aviso.fechaCreacion))            
            print('Fecha eliminacion: ', fin_aviso)            
            print('Fecha Actual: ', fecha_actual)            
            if fecha_actual > fin_aviso:
                print('Eliminar este aviso')
                aviso.delete()
            print('\n================================')
            
    avisosP = all_avisos.filter(docente = docente)
    avisosT = all_avisos.filter(entidad = 'TODOS')
    avisosD = all_avisos.filter(entidad = 'DOCENTES')
    avisos = avisosP | avisosT | avisosD
    
    all_anteproyectos = Anteproyecto.objects.all()
    all_residencias = Residencia.objects.all()
    all_anteproyectos_E = all_anteproyectos.filter(estatus = 'ENVIADO')
    
    anteproyectos_activos_r1 = all_anteproyectos.filter(revisor1=docente).exclude(estatus__in=['ACEPTADO', 'RECHAZADO'])
    anteproyectos_activos_r2 = all_anteproyectos.filter(revisor2=docente).exclude(estatus__in=['ACEPTADO', 'RECHAZADO'])
    
    residencias_activas_a = all_residencias.filter(r_asesorInterno=docente).exclude(estatus__in=['FINALIZADA', 'RECHAZADA', 'NO FINALIZADA'])
    residencias_activas_r = all_residencias.filter(r_revisor=docente).exclude(estatus__in=['FINALIZADA', 'RECHAZADA', 'NO FINALIZADA'])
    
    anteproyectos_pasados_r1 = all_anteproyectos.filter(estatus='ACEPTADO', revisor1=docente)
    anteproyectos_pasados_r2 = all_anteproyectos.filter(estatus='ACEPTADO', revisor2=docente)
    
    residencias_pasadas_a = all_residencias.filter(estatus='FINALIZADA', r_asesorInterno=docente)
    residencias_pasadas_r = all_residencias.filter(estatus='FINALIZADA', r_revisor=docente)
    
    actividad_docente = [anteproyectos_activos_r1.count() + anteproyectos_activos_r2.count(),
                         residencias_activas_a.count() + residencias_activas_r.count(), 
                         residencias_activas_a.count(), 
                         anteproyectos_pasados_r1.count() + anteproyectos_pasados_r2.count(), 
                         residencias_pasadas_a.count() + residencias_pasadas_r.count(), 
                         residencias_activas_r.count()
                         ]

    all_anteproyectos_activos = anteproyectos_activos_r1 | anteproyectos_activos_r2
    actualizaciones = Actualizacion_anteproyecto.objects.filter(anteproyecto__in=all_anteproyectos_activos, tipo='ACTUALIZADO').exclude(estado='LEIDO').order_by('-fecha')
    
    context = {'group': group, 'docente': docente, 'anteproyectos': all_anteproyectos_E, 'actividad_docente': actividad_docente, 'actualizaciones': actualizaciones, 'avisos': avisos, 'title': 'Inicio'}
    return render(request, 'Teacher/dashboard.html', context)

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@unauthenticated_user
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect')

    context = {}
    return render(request, 'Global/login.html', context)

def errorPage(request):
    return render(request, 'Global/404.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
@d_faqs
def faqs(request):
    group = request.user.groups.all()[0].name
    context = {'group': group, 'title': 'Preguntas Frecuentes'}
    return render(request, 'Global/faqs.html', context)

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def student_faqs(request):
    group = request.user.groups.all()[0].name
    context = {'group': group, 'title': 'Preguntas Frecuentes'}
    return render(request, 'Student/faqs.html', context)

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
@teacher_only
def teacher_faqs(request):
    group = request.user.groups.all()[0].name
    context = {'group': group, 'title': 'Preguntas Frecuentes'}
    return render(request, 'Teacher/faqs.html', context)

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def changePassword(request):
    user = request.user
    group = user.groups.all()[0].name
    form = ChangePasswordForm(user)
    
    if request.method == 'POST':
        form = ChangePasswordForm(user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  
            messages.success(request, 'Your password was successfully updated!')
            return render(request, 'Global/password-change-done.html', {'group': group})
        else:
            messages.error(request, 'Please correct the error below.')
            
    context = {'group': group, 'form': form, 'title': 'Cambiar Contraseña'}
    return render(request, 'Global/change-password.html', context)

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def createStudent(request):
    data = ['id_fotoUsuario', 'id_institutoSeguridadSocial', 'id_numSeguridadSocial', 'id_expediente', 'id_correoElectronico', 'id_curp', 'id_anteproyecto']
    formE = EstudianteForm()
    formU = CreateUserForm()

    if request.method == 'POST':
        formE = EstudianteForm(request.POST)
        formU = CreateUserForm(request.POST)        
        if formE.is_valid() and formU.is_valid():
            student = formE.save()
            user = formU.save()
            username = formU.cleaned_data.get('username')
            group = Group.objects.get(name='student')
            user.groups.add(group)
            student.correoElectronico = formU.cleaned_data.get('email')
            student.user = user
            student.numControl = username
            student.save()
            messages.success(request, f'Cuenta creada exitosamente!... {username}')
            return redirect('login')

    context = {'formE': formE, 'formU': formU, 'data': data}
    return render(request, 'Student/create-account.html', context)

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def estudianteViewProfile(request):
    user = request.user
    estudiante = user.estudiante    
    group = user.groups.all()[0].name
    domicilio = estudiante.domicilio
    form = DomicilioForm(instance=domicilio)
    context = {'form': form, 'estudiante': estudiante, 'domicilio': domicilio, 'group': group, 'title': 'Perfil'}
    return render(request, 'Student/viewProfile.html', context)

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def estudianteSettings(request):
    user = request.user
    group = user.groups.all()[0].name
    estudiante = user.estudiante
    domicilio = estudiante.domicilio
    formE = EstudianteForm(instance=estudiante)

    if domicilio is None:
        formD = DomicilioForm()
        if request.method == 'POST':
            formD = DomicilioForm(request.POST)
            formE = EstudianteForm(
                request.POST, request.FILES, instance=estudiante)
            if formE.is_valid():
                formE.save()
                if formD.is_valid():
                    dom = formD.save()
                    estudiante.domicilio = dom
                    estudiante.save()
                return redirect('studentProfile')

    else:
        formD = DomicilioForm(instance=domicilio)
        if request.method == 'POST':
            formD = DomicilioForm(request.POST, instance=domicilio)
            formE = EstudianteForm(
                request.POST, request.FILES, instance=estudiante)            
            if formE.is_valid():
                formE.save()
                if formD.is_valid():
                    formD.save()
                return redirect('studentProfile')

    context = {'formD': formD, 'formE': formE, 'estudiante': estudiante, 'domicilio': domicilio, 'group': group, 'title': 'Configuracion'}
    return render(request, 'Student/settings.html', context)

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def expediente(request):
    data = ['id_dictamen', 'id_solicitudResidencia', 'id_anteproyecto', 'id_horario', 'id_cartaAceptacion', 'id_cartaCompromiso', 'id_cronograma', 'id_cartaPresentacion']    
    # Documentos a los que se le agrega una fecha limite para su entrega (5 Dias)
    data2 = ['id_anteproyecto', 'id_cartaLiberacion']
    user = request.user
    group = user.groups.all()[0].name
    estudiante = user.estudiante
    semestre = estudiante.semestre
    expediente = estudiante.expediente 
    anteproyecto = estudiante.anteproyecto
    residencia = estudiante.residencia    
    r1 = None    
    r2 = None
    rF = None
    fecha20d = None            
    fecha6w = None                
    expediente_completo = True
    
    if expediente:
    
        expediente_list = Expediente.objects.filter(id = expediente.id).values()[0]    
        
        if expediente.estatus != 'FINALIZADO':
            for i in expediente_list:
                if not expediente_list[i]:
                    if i == 'dictamen':
                        if semestre > 12:                            
                            expediente_completo = False
                    else:
                        expediente_completo = False                                
                        
        if expediente_completo:            
            reporte1 = ReporteParcial1.objects.filter(id = expediente.reporteParcial1.id).values()[0]
            reporte2 = ReporteParcial2.objects.filter(id = expediente.reporteParcial2.id).values()[0]
            reporteF = ReporteFinal.objects.filter(id = expediente.reporteFinal.id).values()[0]
            all_reportes = [reporte1['r1_hojaRevisores'], reporte1['r1_formatoEvaluacion'], reporte2['r2_hojaRevisores'], reporte2['r2_formatoEvaluacion'], reporteF['rf_hojaRevisores'], reporteF['rf_formatoEvaluacion']]                        
            
            expediente_completo = not None in all_reportes
            
            if expediente_completo:
                expediente.estatus = 'COMPLETO'
                expediente.save()                                                        
        
    try:
        estatus = anteproyecto.estatus                       
    except:
        estatus = None
    
    if anteproyecto and estatus == 'ACEPTADO' and residencia.periodoInicio:              
        fecha20d = residencia.periodoInicio + timedelta(days=20)        
        fecha6w = residencia.periodoInicio + timedelta(weeks=6)         
                                
    if expediente is None:         
        if estatus == 'ACEPTADO' and residencia.periodoInicio:            
            formE = ExpedienteForm()        
            if request.method == 'POST':
                formE = ExpedienteForm(request.POST, request.FILES)                        
                if formE.is_valid():                                
                    expediente = formE.save()                
                    expediente.save() 
                    estudiante.expediente = expediente                                                    
                    estudiante.save()                                                                        
                    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
        else:            
            formE = ExpedienteViewForm()
    else:        
        r1 = expediente.reporteParcial1
        r2 = expediente.reporteParcial2
        rF = expediente.reporteFinal
                
        formE = ExpedienteForm(instance=expediente)                
        if request.method == 'POST':            
            formE = ExpedienteForm(request.POST, request.FILES, instance=expediente)                                                         
                             
            if formE.is_valid():                
                formE.save()                              
            
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found')) 
    
    context = {'form': formE, 'expediente': expediente, 'anteproyecto': anteproyecto, 'r1': r1, 'r2': r2, 'rF': rF, 'data': data, 'data2': data2, 'fecha20d': fecha20d, 'fecha6w': fecha6w, 'estatus': estatus, 'group': group, 'semestre': semestre, 'residencia': residencia, 'title': 'Expediente'}    
    return render(request, 'Student/expediente.html', context)

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def reportes(request):
    user = request.user
    group = user.groups.all()[0].name
    estudiante = user.estudiante
    expediente = estudiante.expediente
    anteproyecto = estudiante.anteproyecto   
    residencia = estudiante.residencia 
    r1 = None    
    r2 = None
    rF = None
    form1 = None
    form2 = None
    formF = None    
    r1_fechaEntrega = None            
    r2_fechaEntrega = None            
    rF_fechaEntrega = None  
    
    try:
        estatus = anteproyecto.estatus                       
    except:
        estatus = None      
        
    if anteproyecto and estatus == 'ACEPTADO' and residencia.periodoInicio:            
        fechaInicio = residencia.periodoInicio
        r1_fechaEntrega = fechaInicio + timedelta(weeks=6)        
        r2_fechaEntrega = r1_fechaEntrega + timedelta(weeks=12)
        rF_fechaEntrega = r2_fechaEntrega + timedelta(weeks=6)
        r1_fechaEntrega = r1_fechaEntrega.strftime("%d/%b/%Y")
        r2_fechaEntrega = r2_fechaEntrega.strftime("%d/%b/%Y")        
        rF_fechaEntrega = rF_fechaEntrega.strftime("%d/%b/%Y")
        
    if expediente is not None:                
        r1 = expediente.reporteParcial1
        r2 = expediente.reporteParcial2
        rF = expediente.reporteFinal                   
                               
        if r1 is None:            
            form1 = Reporte1Form()
            if request.method == 'POST':
                form1 = Reporte1Form(request.POST, request.FILES)                    
                if form1.is_valid():                    
                    r1 = form1.save()
                    expediente.reporteParcial1 = r1
                    expediente.save()
                    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))        
        else:                        
            form1 = Reporte1Form(instance = r1)                  
            if not r1.r1_formatoEvaluacion or not r1.r1_hojaRevisores:
                if request.method == 'POST':
                    form1 = Reporte1Form(request.POST, request.FILES, instance = r1)                                                                                     
                    if form1.is_valid():                                                            
                        r1 = form1.save()  
                        expediente.reporteParcial1 = r1
                        expediente.save()
                        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))                                                                        
            
        if r2 is None:            
            form2 = Reporte2Form()
            if request.method == 'POST':
                form2 = Reporte2Form(request.POST, request.FILES)                
                if form2.is_valid():                     
                    r2 = form2.save()
                    expediente.reporteParcial2 = r2
                    expediente.save()
                    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
        else:            
            form2 = Reporte2Form(instance = r2)                          
            if not r2.r2_formatoEvaluacion or not r2.r2_hojaRevisores:
                if request.method == 'POST':                
                    form2 = Reporte2Form(request.POST, request.FILES, instance = r2)                     
                    if form2.is_valid():                            
                        r2 = form2.save()  
                        expediente.reporteParcial2 = r2
                        expediente.save()
                        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
            
        if rF is None:            
            formF = ReporteFinalForm()
            if request.method == 'POST':
                formF = ReporteFinalForm(request.POST, request.FILES)                                                                
                if formF.is_valid():                      
                    rF = formF.save()
                    expediente.reporteFinal = rF
                    expediente.save()
                    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
        else:            
            formF = ReporteFinalForm(instance = rF)                        
            if not rF.rf_formatoEvaluacion or not rF.rf_hojaRevisores:        
                if request.method == 'POST':
                    formF = ReporteFinalForm(request.POST, request.FILES, instance = rF)                                                
                    if formF.is_valid():                        
                        rF = formF.save()  
                        expediente.reporteFinal = rF
                        expediente.save()
                        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))      
    else:
        form1 = Reporte1Form()                       
        form2 = Reporte2Form()                       
        formF = ReporteFinalForm()
            
    context = {'expediente': expediente, 'anteproyecto': anteproyecto, 'residencia': residencia, 'form1': form1, 'form2': form2, 'formF': formF, 'r1': r1, 'r2': r2, 'rF': rF, 'r1_fechaEntrega': r1_fechaEntrega, 'r2_fechaEntrega': r2_fechaEntrega, 'rF_fechaEntrega': rF_fechaEntrega, 'estatus': estatus, 'group': group, 'title': 'Reportes'}
    return render(request, 'Student/reportes.html', context)    

@cache_control(no_cache=True, must_revalidate=True, no_store=True)    
@login_required(login_url='login')
def anteproyecto(request):
    data = ['id_codigoUnion', 'id_estatus', 'id_docentes', 'id_dependencia', 'id_asesorExterno', 'id_periodoInicio_month', 'id_periodoFin_month']
    user = request.user
    group = user.groups.all()[0].name
    estudiante = user.estudiante                    
    anteproyectos = Anteproyecto.objects.all()                          
    anteproyecto = estudiante.anteproyecto                                                   
    estudiantes = Estudiante.objects.filter(anteproyecto = anteproyecto)        
    fechaObservacion = None
    fechaCorte = None
    fechaActual = None
    dependencia = None
    revisor1 = None
    revisor2 = None
    observaciones = None  
    formDoc = None                               
    enviados = anteproyectos.exclude(codigoUnion='0000000000').filter(estatus='ENVIADO')                    
    codigo = '0000000000'     
    mensaje = ''       
    
    try:        
        observacion = anteproyecto.observacion
        fechaObservacion = observacion.fechaCreacion    
        observaciones = ObservacionDocente.objects.filter(observacion = observacion).order_by('-fechaElaboracion')                                
        dias = 5 + observacion.incrementarDias
        fechaObservacion = fechaObservacion + timedelta(days=dias)           
        fechaCorte = fechaObservacion + timedelta(days=1)             
        fechaActual = date.today
        fechaObservacion = fechaObservacion.strftime("%d/%b/%Y")                   
    except:
        pass
    
    if anteproyecto is None:             
        formA = AnteproyectoEstForm()                
                
        if request.method == 'POST':          
            try:
                codigoU = request.POST['codigoAnteproyecto']
            except:
                codigoU = None
                                                
            if codigoU:                
                for i in enviados:                    
                    if i.codigoUnion == codigoU:                        
                        numIntegrantes = Estudiante.objects.filter(anteproyecto=i).count()                                                
                        if numIntegrantes < i.numIntegrantes:
                            estudiante.anteproyecto = i
                            estudiante.save()
                            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
                        else:
                            mensaje = 'El anteproyecto esta lleno'                            
                                                        
                if not mensaje: mensaje = 'Codigo invalido'                                                        
            else:                                              
                formA = AnteproyectoEstForm(request.POST, request.FILES)                                                                                                    
                if formA.is_valid():                                                                        
                    anteproyecto = formA.save()                    
                    if int(request.POST['numIntegrantes']) > 1:  
                        codigo = obtenerCodigo()                                                                                                                                    
                    anteproyecto.codigoUnion=codigo
                    anteproyecto.save()
                    estudiante.anteproyecto=anteproyecto
                    estudiante.save()                                                    
                    return redirect('materias')                                        
                    
    else:
        data.clear()
        data.extend(['id_docentes', 'id_dependencia', 'id_asesorExterno', 'id_domicilio', 'id_titular', 'id_mision'])                 
        actualizaciones = Actualizacion_anteproyecto.objects.filter(anteproyecto = anteproyecto).order_by('-fecha')
        if anteproyecto.numIntegrantes == 1:            
            data.append('id_codigoUnion')  
        
        revisor1 = anteproyecto.revisor1
        revisor2 = anteproyecto.revisor2                 
        dependencia = anteproyecto.dependencia   
        if dependencia:
            titular = dependencia.titular
            domicilio = dependencia.domicilio
        else:
            titular = None
            domicilio = None               
        formA = AnteproyectoViewForm(instance = anteproyecto)                                        
        formD = DependenciaViewForm(instance = dependencia)
        formT = TitularViewForm(instance = titular)
        formDom = DomicilioViewForm(instance = domicilio)
        formDoc = AnteproyectoDocForm(instance = anteproyecto)
        formAE = AsesorEViewForm(instance = anteproyecto.asesorExterno)     
        
        if request.method == 'POST':        
            formDoc = AnteproyectoDocForm(request.POST, request.FILES, instance=anteproyecto)
            if formDoc.is_valid():                
                formDoc.save()
                actualizacion = Actualizacion_anteproyecto(anteproyecto = anteproyecto, descripcion = 'Se actualizó el documento del Anteproyecto')
                actualizacion.save()
                return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
        context = {'formA': formA, 'formD': formD, 'formT': formT, 'formAE': formAE ,'formDom': formDom, 'formDoc': formDoc, 'data': data, 'mensaje':mensaje, 'anteproyecto': anteproyecto, 'estudiantes': estudiantes, 'dependencia': dependencia, 'group': group, 'observaciones': observaciones, 'revisor1': revisor1, 'revisor2': revisor2, 'fechaObservacion': fechaObservacion, 'fechaCorte': fechaCorte, 'fechaActual': fechaActual, 'title': 'Anteproyecto', 'actualizaciones': actualizaciones}    
        return render(request, 'Student/anteproyecto2.html', context)
            
    context = {'formA': formA, 'formDoc': formDoc, 'data': data, 'mensaje':mensaje, 'anteproyecto': anteproyecto, 'estudiantes': estudiantes, 'dependencia': dependencia, 'group': group, 'observaciones': observaciones, 'revisor1': revisor1, 'revisor2': revisor2, 'fechaObservacion': fechaObservacion, 'fechaCorte': fechaCorte, 'fechaActual': fechaActual, 'title': 'Anteproyecto'}    
    return render(request, 'Student/anteproyecto2.html', context)

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def dependencias(request, page, orderB):
    user = request.user
    group = user.groups.all()[0].name
    estudiante = user.estudiante  
    anteproyecto = estudiante.anteproyecto   
    dependencia = anteproyecto.dependencia
    all_dependencias = Dependencia.objects.all()               
    start = (page-1)*10    
    end = page*10
    
    if request.method == 'POST':        
        text = request.POST['search'] 
                        
        if text:            
            all_dependencias = all_dependencias.filter(d_nombre__icontains=text)
            dependencias = all_dependencias
            start = 0
            end = dependencias.count()
            totalD = all_dependencias.count()                        
            search = '.'             
            context = {'group': group, 'anteproyecto': anteproyecto, 'dependencia': dependencia, 'dependencias': dependencias, 'totalD': totalD, 'page': page, 'start': start+1, 'end': end, 'orderB': orderB, 'search': search, 'filter': filter, 'title': 'Anteproyectos'}
            return render(request, 'Student/dependencia.html', context)    
    
    all_dependencias = ordenar_dependencias(all_dependencias, orderB)                
    dependencias = all_dependencias[start:end]
    if end != dependencias.count():
        end = end-10+dependencias.count()
    totalD = all_dependencias.count()
    n_buttons = math.ceil(totalD/10)
    buttons = [item for item in range(1, n_buttons+1)]
    next_page = page+1
    prev_page = page-1    
    
    context = {'anteproyecto': anteproyecto, 'dependencia': dependencia, 'group': group, 'dependencias': dependencias, 'start': start+1, 'end': end, 'totalD': totalD, 'n_buttons': n_buttons , 'buttons': buttons, 'next_page': next_page, 'prev_page': prev_page, 'page': page, 'orderB': orderB, 'title': 'Dependencia'}    
    return render(request, 'Student/dependencia.html', context)

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def asignar_dependencia(request, pk):    
    estudiante = request.user.estudiante                    
    anteproyecto = estudiante.anteproyecto
    dependencia = Dependencia.objects.get(id = pk)
    anteproyecto.dependencia = dependencia
    anteproyecto.save()    
    return redirect('anteproyecto')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def alta_dependencia(request):
    user = request.user
    group = user.groups.all()[0].name
    estudiante = user.estudiante                    
    anteproyecto = estudiante.anteproyecto
    dependencia = anteproyecto.dependencia
    dependencias = Dependencia.objects.all()
    formD = DependenciaForm()    
    
    if request.method == 'POST':
        formD = DependenciaForm(request.POST)        
        if formD.is_valid():
            dependencia = formD.save()                                    
            dependencia.save()
            anteproyecto.dependencia = dependencia
            anteproyecto.save()
            return redirect('alta_titular_d')                                                
    
    context = {'anteproyecto': anteproyecto, 'dependencia': dependencia, 'formD': formD, 'group': group, 'dependencias': dependencias,'title': 'Alta Dependencia'}    
    return render(request, 'Student/altaDependencia.html', context)

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def alta_titular_d(request):
    user = request.user
    group = user.groups.all()[0].name
    estudiante = user.estudiante                    
    anteproyecto = estudiante.anteproyecto
    dependencia = anteproyecto.dependencia
    formT = TitularForm()
    
    if request.method == 'POST':
        formT = TitularForm(request.POST)
        if formT.is_valid():
            titular = formT.save()
            titular.save()
            dependencia.titular = titular
            dependencia.save()
            if not dependencia.domicilio:
                return redirect('alta_domicilio_d')                                                            
            else:
                return redirect('anteproyecto')                                                
    
    context = {'anteproyecto': anteproyecto, 'dependencia': dependencia, 'formT': formT, 'group': group, 'dependencias': dependencias,'title': 'Alta Dependencia'}    
    return render(request, 'Student/altaTitularD.html', context)

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def alta_domicilio_d(request):
    user = request.user
    group = user.groups.all()[0].name
    estudiante = user.estudiante                    
    anteproyecto = estudiante.anteproyecto
    dependencia = anteproyecto.dependencia
    formDom = DomicilioForm()
    
    if request.method == 'POST':
        formDom = DomicilioForm(request.POST)
        if formDom.is_valid():
            domicilio = formDom.save()
            domicilio.save()
            dependencia.domicilio = domicilio
            dependencia.save()
            if not dependencia.titular:
                return redirect('alta_titular_d')                                                            
            else:
                return redirect('anteproyecto')                                                
    
    context = {'anteproyecto': anteproyecto, 'dependencia': dependencia, 'formDom': formDom, 'group': group, 'dependencias': dependencias,'title': 'Alta Dependencia'}    
    return render(request, 'Student/altaDomicilioD.html', context)

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def asesoresE(request):
    user = request.user
    group = user.groups.all()[0].name
    estudiante = user.estudiante
    anteproyecto = estudiante.anteproyecto
    asesorE = None    
    dependencia = None
    all_asesores = None
    if anteproyecto:
        print(':V')
        asesoreE = anteproyecto.asesorExterno
        dependencia = anteproyecto.dependencia
        all_asesores = AsesorExterno.objects.filter(dependencia=dependencia)
        
    context = {'group': group, 'asesorE': asesorE, 'dependencia': dependencia, 'all_asesores': all_asesores, 'title': 'Asesores Externos'}
    return render(request, 'Student/asesoresExt.html', context)

def asignar_asesorE(request, pk):
    user = request.user
    group = user.groups.all()[0].name
    estudiante = user.estudiante
    anteproyecto = estudiante.anteproyecto
    asesorE = AsesorExterno.objects.get(id = pk)
    anteproyecto.asesorExterno = asesorE
    anteproyecto.save()
    return redirect('anteproyecto')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def alta_asesorE(request):
    user = request.user
    group = user.groups.all()[0].name
    estudiante = user.estudiante
    anteproyecto = estudiante.anteproyecto
    asesorE = None
    dependencia = None
    form = AsesorEForm()
    if anteproyecto:
        asesorE = anteproyecto.asesorExterno
        dependencia = anteproyecto.dependencia
    
    if request.method == 'POST':
        form = AsesorEForm(request.POST)
        if form.is_valid():
            asesorE = form.save()
            asesorE.dependencia = dependencia
            asesorE.save()            
            anteproyecto.asesorExterno = asesorE
            anteproyecto.save()
            return redirect('anteproyecto')
    context = {'group': group, 'asesorE': asesorE, 'dependencia':dependencia, 'form': form, 'title': 'Alta Asesor Externo'}
    return render(request, 'Student/altaAsesorE.html', context)            

def anteproyecto2(request):
    data = ['id_codigoUnion', 'id_estatus', 'id_docentes', 'id_dependencia', 'id_asesorExterno', 'id_periodoInicio_month', 'id_periodoFin_month']
    user = request.user
    group = user.groups.all()[0].name
    estudiante = user.estudiante                    
    anteproyectos = Anteproyecto.objects.all()                          
    anteproyecto = estudiante.anteproyecto                                                   
    estudiantes = Estudiante.objects.filter(anteproyecto = anteproyecto)        
    fechaObservacion = None
    fechaCorte = None
    fechaActual = None
    dependencia = None
    revisor1 = None
    revisor2 = None
    observaciones = None                                 
    enviados = anteproyectos.exclude(codigoUnion='0000000000').filter(estatus='ENVIADO')                    
    codigo = '0000000000'     
    mensaje = ''       
    
    try:        
        observacion = anteproyecto.observacion
        fechaObservacion = observacion.fechaCreacion    
        observaciones = ObservacionDocente.objects.filter(observacion = observacion)                                
        dias = 5 + observacion.incrementarDias
        fechaObservacion = fechaObservacion + timedelta(days=dias)           
        fechaCorte = fechaObservacion + timedelta(days=1)             
        fechaActual = date.today
        fechaObservacion = fechaObservacion.strftime("%d/%b/%Y")                   
    except:
        pass
    
    if anteproyecto is None:             
        formA = AnteproyectoEstForm()
        formD = DependenciaForm()  
        formT = TitularForm()
        formDom = DomicilioForm()
        formDoc = AnteproyectoDocForm()
        formAE = AsesorEForm()         
                
        if request.method == 'POST':          
            try:
                codigoU = request.POST['codigoAnteproyecto']
            except:
                codigoU = None
                                                
            if codigoU:                
                for i in enviados:                    
                    if i.codigoUnion == codigoU:                        
                        numIntegrantes = Estudiante.objects.filter(anteproyecto=i).count()                                                
                        if numIntegrantes < i.numIntegrantes:
                            estudiante.anteproyecto = i
                            estudiante.save()
                            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
                        else:
                            mensaje = 'El anteproyecto esta lleno'                            
                                                        
                if not mensaje: mensaje = 'Codigo invalido'                                                        
            else:                
                              
                formA = AnteproyectoEstForm(request.POST)
                formD = DependenciaForm(request.POST)
                formT = TitularForm(request.POST)
                formDom = DomicilioForm(request.POST)
                formAE = AsesorEForm(request.POST)                        
                                        
                if formA.is_valid() and formD.is_valid() and formT.is_valid() and formAE.is_valid() and formDom.is_valid():                                
                    fecha_inicio = formA.cleaned_data.get('periodoInicio')
                    fecha_fin = formA.cleaned_data.get('periodoFin')
                    if fecha_inicio < fecha_fin:                                            
                        anteproyecto = formA.save()
                        dependencia = formD.save()
                        titular = formT.save()
                        domicilio = formDom.save()
                        asesorE = formAE.save()                        
                        dependencia.domicilio = domicilio
                        dependencia.titular = titular
                        dependencia.save()                        
                        asesorE.dependencia = dependencia
                        asesorE.save()
                        anteproyecto.dependencia = dependencia
                        anteproyecto.asesorExterno = asesorE
                        if int(request.POST['numIntegrantes']) > 1:  
                            codigo = obtenerCodigo()                                                                                                                                    
                        anteproyecto.codigoUnion=codigo
                        anteproyecto.save()
                        estudiante.anteproyecto=anteproyecto
                        estudiante.save()                                
                        #return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
                        return redirect('materias')
                    
                    mensaje = 'Fecha de fin del Anteproyecto erronea'
                    
    else:
        data.clear()
        data.extend(['id_docentes', 'id_dependencia', 'id_asesorExterno', 'id_domicilio', 'id_titular'])         
        if anteproyecto.numIntegrantes == 1:
            data.append('id_codigoUnion')  
        
        revisor1 = anteproyecto.revisor1
        revisor2 = anteproyecto.revisor2         
        print(revisor1)       
        print(revisor2)       
        dependencia = anteproyecto.dependencia                  
        formA = AnteproyectoViewForm(instance = anteproyecto)                                        
        formD = DependenciaViewForm(instance = dependencia)
        formT = TitularViewForm(instance = dependencia.titular)
        formDom = DomicilioViewForm(instance = dependencia.domicilio)
        formDoc = AnteproyectoDocForm(instance = anteproyecto)
        formAE = AsesorEViewForm(instance = anteproyecto.asesorExterno)     
        
        if request.method == 'POST':        
            formDoc = AnteproyectoDocForm(request.POST, request.FILES, instance=anteproyecto)
            if formDoc.is_valid():                
                formDoc.save()
                return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
            
    context = {'formA': formA, 'formD': formD, 'formT': formT, 'formAE': formAE ,'formDom': formDom, 'formDoc': formDoc, 'data': data, 'mensaje':mensaje, 'anteproyecto': anteproyecto, 'estudiantes': estudiantes, 'dependencia': dependencia, 'group': group, 'observaciones': observaciones, 'revisor1': revisor1, 'revisor2': revisor2, 'fechaObservacion': fechaObservacion, 'fechaCorte': fechaCorte, 'fechaActual': fechaActual, 'title': 'Anteproyecto'}    
    return render(request, 'Student/anteproyecto2.html', context)
    
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')    
def editarAnteproyecto(request):    
    data = ['id_docentes', 'id_dependencia', 'id_asesorExterno', 'id_estatus', 'id_codigoUnion', 'id_domicilio', 'id_titular']
    group = request.user.groups.all()[0].name
    estudiante = request.user.estudiante         
    anteproyecto = estudiante.anteproyecto
    estudiantes = Estudiante.objects.filter(anteproyecto = anteproyecto).count()                    
    
    codigo = anteproyecto.codigoUnion
    numIntegrantes = anteproyecto.numIntegrantes
    mensaje = ''
    
    formA = AnteproyectoEstForm(instance = anteproyecto)                                                    
    
    if request.method == 'POST':                        
        formA = AnteproyectoEstForm(request.POST, instance = anteproyecto)                                          
                  
        if formA.is_valid():
            numIntegrantes2 = int(formA['numIntegrantes'].value())                        
            
            if numIntegrantes2 < 1:
                mensaje = 'El numero de integrantes no puede ser menor a 1'
            else:                
                if numIntegrantes == 1 and numIntegrantes2 >= 2:                    
                    codigo = obtenerCodigo()                    
                elif numIntegrantes >= 2 and numIntegrantes2 == 1 and estudiantes == 1:                    
                    codigo = '0000000000'                     
                                                                                                                                                                        
                if numIntegrantes > numIntegrantes2 and estudiantes > numIntegrantes2:                                        
                    mensaje = 'No se puede reducir el numero de integrantes. No se pueden eliminar integrantes'                    
                else:                                                                    
                    anteproyecto = formA.save()                                      
                    anteproyecto.save() 
                    return redirect('anteproyecto')                               
    
    context = {'formA': formA, 'data': data, 'anteproyecto': anteproyecto, 'mensaje': mensaje, 'group': group, 'title': 'Editar Anteproyecto'}    
    return render(request, 'Student/editarAnteproyecto.html', context)

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def proyectoResidencia(request):
    data = ['id_codigoUnion']
    user = request.user
    group = user.groups.all()[0].name
    estudiante = user.estudiante                                    
    anteproyecto = estudiante.anteproyecto   
    residencia = estudiante.residencia        
    mensaje = ''
        
    if residencia:                                                
        dependencia = residencia.dependencia                   
        asesorI = residencia.r_asesorInterno
        revisor = residencia.r_revisor
        estudiantes = Estudiante.objects.filter(residencia = residencia)                
        formR = ResidenciaViewForm(instance = residencia)   
        formRDate = ResidenciaDateForm(instance = residencia)                                
        formD = DependenciaViewForm(instance = dependencia)
        formT = TitularViewForm(instance = dependencia.titular)
        formDom = DomicilioViewForm(instance = dependencia.domicilio)
        formAE = AsesorEViewForm(instance = residencia.asesorExterno)     
        
        if request.method == 'POST':            
            formRDate = ResidenciaDateForm(request.POST, instance=residencia) 
            if formRDate.is_valid():
                formRDate.save()
                return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))                                                                        
            else:
                mensaje = 'Por favor, ingrese una fecha valida'            
                                                   
        context = {'group': group, 'mensaje': mensaje ,'formR': formR, 'formRDate': formRDate, 'formD': formD, 'formT': formT, 'formAE': formAE ,'formDom': formDom,'data': data, 'anteproyecto': anteproyecto, 'estudiantes': estudiantes, 'dependencia': dependencia, 'residencia': residencia, 'asesorI': asesorI, 'revisor': revisor, 'title': 'Residencia'}
        return render(request, 'Student/residencia.html', context)
        
    context = {'group': group, 'residencia': residencia, 'title': 'Residencia'}
    return render(request, 'Student/residencia.html', context)

@login_required(login_url='login')  
def removeDoc(request, pk):
    anteproyecto = Anteproyecto.objects.get(id = pk)
    anteproyecto.anteproyectoDoc.delete()        
    actualizacion = Actualizacion_anteproyecto(anteproyecto = anteproyecto, tipo='REMOVIDO', descripcion = 'Se removió el documento del Anteproyecto')
    actualizacion.save()
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))        

def logoutUser(request):
    logout(request)
    return redirect('login')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def compatibilidadA(request, materiaPK):
    group = request.user.groups.all()[0].name
    estudiante = request.user.estudiante
    anteproyecto = estudiante.anteproyecto    
    materia = Materia.objects.get(id = materiaPK)
      
    if request.method == 'POST':        
        compatibilidad = int(request.POST['Compatibilidad'])
        anteproyecto_materia = Anteproyecto_materia(anteproyecto=anteproyecto, materia=materia, compatibilidad=compatibilidad)
        anteproyecto_materia.save()
        return redirect('materias')
        
    context = {'group': group, 'materia': materia, 'title': 'Comptabilidad'}    
    return render(request, 'Student/compatibilidadA.html', context)

def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = ResetPasswordForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "Global/password_reset/password_reset_email.txt"
                    c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect ("/password_reset/done/")
    password_reset_form = ResetPasswordForm()
    return render(request=request, template_name="Global/password_reset/forgot-password.html", context={"password_reset_form":password_reset_form})
    
def generarCodigo():            
    length = 10
    letters = string.ascii_uppercase
    code = ''.join(random.choice(letters + string.digits) for i in range(length))                        
    return code   

def obtenerCodigo():
    while True:        
        codigo = generarCodigo()
        if not buscarCodigo(codigo):
            return codigo        
     
def buscarCodigo(codigo):
    proyectos = Anteproyecto.objects.exclude(codigoUnion='0000000000').filter(estatus='Enviado')     
    for p in proyectos:
        if p.codigoUnion == codigo:
            return True
    return False

def ordenar_dependencias(dependencias, orderB):
    all_dependencias = dependencias
    if orderB == 1:
        all_dependencias = all_dependencias.order_by('d_nombre')    
    elif orderB == 2:
        all_dependencias = all_dependencias.order_by('-d_nombre')    
    return all_dependencias
    
def convert_to_localtime(utctime):
    fmt = '%d-%m-%Y %H:%M'
    utc = utctime.replace(tzinfo=pytz.UTC)
    localtz = utc.astimezone(timezone.get_current_timezone())
    return localtz.strftime(fmt)