from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
#from django.db.models import Count
from datetime import date, timedelta
import string  
import random  
from .models import *
from .forms import *
from .decorators import *
# Create your views here.

@login_required(login_url='login')
@admin_only
def home(request):
    group = request.user.groups.all()[0].name
    context = {'group': group}
    return render(request, 'Global/dashboard.html', context)

@login_required(login_url='login')
def studentPage(request):
    group = request.user.groups.all()[0].name
    context = {'group': group}
    return render(request, 'Student/dashboard.html', context)

@login_required(login_url='login')
def teacherPage(request):
    group = request.user.groups.all()[0].name
    context = {'group': group}
    return render(request, 'Teacher/dashboard.html', context)

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

def estudianteViewProfile(request):
    user = request.user
    estudiante = user.estudiante    
    group = user.groups.all()[0].name
    domicilio = estudiante.domicilio
    form = DomicilioForm(instance=domicilio)
    context = {'form': form, 'estudiante': estudiante, 'domicilio': domicilio, 'group': group}
    return render(request, 'Student/viewProfile.html', context)

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

    context = {'formD': formD, 'formE': formE, 'estudiante': estudiante, 'domicilio': domicilio, 'group': group}
    return render(request, 'Student/settings.html', context)

def expediente(request):
    data = ['id_dictamen', 'id_solicitudResidencia', 'id_anteproyecto', 'id_horario', 'id_cartaAceptacion', 'id_cartaCompromiso', 'id_cronograma', 'id_cartaPresentacion']    
    user = request.user
    group = user.groups.all()[0].name
    estudiante = user.estudiante
    semestre = estudiante.semestre
    expediente = estudiante.expediente 
    anteproyecto = estudiante.anteproyecto    
    r1 = None    
    r2 = None
    rF = None
    fecha20d = None            
    fecha6w = None                
    
    try:
        estatus = anteproyecto.estatus                       
    except:
        estatus = None
    
    if anteproyecto and estatus == 'ACEPTADO':            
        fecha20d = anteproyecto.periodoInicio + timedelta(days=20)
        fecha6w = anteproyecto.periodoInicio + timedelta(weeks=6)            
                                
    if expediente is None:         
        if estatus == 'ACEPTADO':
            formE = ExpedienteForm()        
            if request.method == 'POST':
                formE = ExpedienteForm(request.POST, request.FILES)                        
                if formE.is_valid():                                
                    expediente = formE.save()                
                    estudiante.expediente = expediente                                
                    expediente.save() 
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
    
    context = {'form': formE, 'expediente': expediente, 'r1': r1, 'r2': r2, 'rF': rF, 'data': data, 'fecha20d': fecha20d, 'fecha6w': fecha6w, 'estatus': estatus, 'group': group, 'semestre': semestre}    
    return render(request, 'Student/expediente.html', context)

def reportes(request):
    user = request.user
    group = user.groups.all()[0].name
    estudiante = user.estudiante
    expediente = estudiante.expediente
    anteproyecto = estudiante.anteproyecto    
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
        
    if anteproyecto and estatus == 'ACEPTADO':            
        fechaInicio = anteproyecto.periodoInicio            
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
            
    context = {'expediente': expediente, 'form1': form1, 'form2': form2, 'formF': formF, 'r1': r1, 'r2': r2, 'rF': rF, 'r1_fechaEntrega': r1_fechaEntrega, 'r2_fechaEntrega': r2_fechaEntrega, 'rF_fechaEntrega': rF_fechaEntrega, 'estatus': estatus, 'group': group}
    return render(request, 'Student/reportes.html', context)    
    
def anteproyecto(request):
    data = ['id_codigoUnion', 'id_estatus', 'id_docentes', 'id_dependencia', 'id_asesorExterno']
    user = request.user
    group = user.groups.all()[0].name
    estudiante = user.estudiante                    
    anteproyectos = Anteproyecto.objects.all()                          
    anteproyecto = estudiante.anteproyecto                                                   
    estudiantes = Estudiante.objects.filter(anteproyecto = anteproyecto)        
    fechaObservacion = None
    dependencia = None
    asesorInterno = None
    revisor = None
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
                                                
            if codigoU is not None:                
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
                    fecha_inicio = formA['periodoInicio'].value()
                    fecha_fin = formA['periodoFin'].value()                    
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
                        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
                    
                    mensaje = 'Fecha de fin del Anteproyecto erronea'
                    
    else:
        data.clear()
        data.extend(['id_docentes', 'id_dependencia', 'id_asesorExterno', 'id_domicilio', 'id_titular'])         
        if anteproyecto.numIntegrantes == 1:
            data.append('id_codigoUnion')  
        
        asesorInterno = anteproyecto.asesorInterno
        revisor = anteproyecto.revisor                
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
            
    context = {'formA': formA, 'formD': formD, 'formT': formT, 'formAE': formAE ,'formDom': formDom, 'formDoc': formDoc, 'data': data, 'mensaje':mensaje, 'anteproyecto': anteproyecto, 'estudiantes': estudiantes, 'dependencia': dependencia, 'group': group, 'observaciones': observaciones, 'asesorInterno': asesorInterno, 'revisor': revisor, 'fechaObservacion': fechaObservacion, 'fechaCorte': fechaCorte, 'fechaActual': fechaActual}    
    return render(request, 'Student/anteproyecto.html', context)
    
def editarAnteproyecto(request):    
    data = ['id_docentes', 'id_dependencia', 'id_asesorExterno', 'id_estatus', 'id_codigoUnion', 'id_domicilio', 'id_titular']
    estudiante = request.user.estudiante         
    anteproyecto = estudiante.anteproyecto
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
                    mensaje = 'No se puede reducir el numero de integrantes. No se pueden eliminar integrantes'                    
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
                    return redirect('anteproyecto')                               
    
    context = {'formA': formA, 'formD': formD, 'formT': formT, 'formAE': formAE ,'formDom': formDom,'data': data, 'anteproyecto': anteproyecto, 'dependencia': dependencia, 'mensaje': mensaje}
    
    return render(request, 'Student/editarAnteproyecto.html', context)

def proyectoResidencia(request):
    data = ['id_codigoUnion']
    user = request.user
    group = user.groups.all()[0].name
    estudiante = user.estudiante             
                       
    anteproyecto = estudiante.anteproyecto   
    
    try:
        estatus = anteproyecto.estatus                                                        
    except:
        estatus = None
        
    if estatus == 'ACEPTADO':        
        dependencia = anteproyecto.dependencia   
        
        residencia = Residencia(
            dependencia = dependencia,
            asesorExterno = anteproyecto.asesorExterno,
            r_asesorInterno = anteproyecto.asesorInterno,
            r_revisor = anteproyecto.revisor,
            nombre = anteproyecto.a_nombre,
            tipoProyecto = anteproyecto.tipoProyecto,
            numIntegrantes = anteproyecto.numIntegrantes,
            periodoInicio = anteproyecto.periodoInicio,
            periodoFin = anteproyecto.periodoFin
        )        
        residencia.save()
                        
        estudiantes = Estudiante.objects.filter(anteproyecto = anteproyecto)        
        dependencia = residencia.dependencia   
        
        for e in estudiantes:        
            e.residencia = residencia
            e.save()

        estudiantes = Estudiante.objects.filter(residencia = residencia)                
        formR = ResidenciaViewForm(instance = residencia)                                
        formD = DependenciaViewForm(instance = dependencia)
        formT = TitularViewForm(instance = dependencia.titular)
        formDom = DomicilioViewForm(instance = dependencia.domicilio)
        formAE = AsesorEViewForm(instance = residencia.asesorExterno)                                
        context = {'group': group,'formR': formR, 'formD': formD, 'formT': formT, 'formAE': formAE ,'formDom': formDom,'data': data, 'anteproyecto': anteproyecto, 'estudiantes': estudiantes, 'dependencia': dependencia, 'estatus': estatus}
        return render(request, 'Student/residencia.html', context)
        
    context = {'group': group, 'estatus': estatus}
    return render(request, 'Student/residencia.html', context)
  
def removeDoc(request, pk):
    anteproyecto = Anteproyecto.objects.get(id = pk)
    anteproyecto.anteproyectoDoc.delete()    
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))        

def logoutUser(request):
    logout(request)
    return redirect('login')
    
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
