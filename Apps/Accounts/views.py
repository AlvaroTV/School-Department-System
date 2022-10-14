from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
#from django.db.models import Count
import string  
import random  
from .models import *
from .forms import *
from .decorators import *
# Create your views here.

# * Pagina principal para los maistros
@login_required(login_url='login')
@admin_only
def home(request):

    context = {}
    return render(request, 'Global/dashboard.html', context)


@login_required(login_url='login')
def studentPage(request):
    
    context = {}
    return render(request, 'Student/dashboard.html', context)


@login_required(login_url='login')
def teacherPage(request):
    
    context = {}
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


# * Se crea el estudiante
def createStudent(request):
    data = ['id_fotoUsuario', 'id_institutoSeguridadSocial',
            'id_numSeguridadSocial', 'id_expediente', 'id_correoElectronico', 'id_curp', 'id_anteproyecto']
    formE = EstudianteForm()
    formU = CreateUserForm()

    if request.method == 'POST':
        formE = EstudianteForm(request.POST)
        formU = CreateUserForm(request.POST)
        print(f'Estuidante: {formE.is_valid()}')
        print(formE.errors)
        print(f'User: {formU.is_valid()}')
        if formE.is_valid() & formU.is_valid():
            student = formE.save()
            user = formU.save()
            username = formU.cleaned_data.get('username')

            group = Group.objects.get(name='student')
            user.groups.add(group)
            student.correoElectronico = formU.cleaned_data.get('email')
            student.user = user
            student.save()

            messages.success(request, f'Account was created for {username}')

            return redirect('login')

    context = {'formE': formE, 'formU': formU, 'data': data}
    return render(request, 'Student/create-account.html', context)


def estudianteViewProfile(request):
    estudiante = request.user.estudiante
    domicilio = estudiante.domicilio
    form = DomicilioForm(instance=domicilio)

    context = {'form': form, 'estudiante': estudiante, 'domicilio': domicilio}
    return render(request, 'Student/viewProfile.html', context)


def estudianteSettings(request):
    estudiante = request.user.estudiante
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
            print(f'Estudiante: {formE.is_valid()}')
            print(formE.errors)
            print(formE.changed_data)
            if formE.is_valid():
                formE.save()
                if formD.is_valid():
                    formD.save()
                return redirect('studentProfile')

    context = {'formD': formD, 'formE': formE,
               'estudiante': estudiante, 'domicilio': domicilio}
    return render(request, 'Student/settings.html', context)


def expediente(request):
    estudiante = request.user.estudiante
    expediente = estudiante.expediente 
    r1 = None    
    r2 = None
    rF = None    
                                
    if expediente is None:                        
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
        r1 = expediente.reporteParcial1
        r2 = expediente.reporteParcial2
        rF = expediente.reporteFinal
                
        formE = ExpedienteForm(instance=expediente)                
        if request.method == 'POST':            
            formE = ExpedienteForm(request.POST, request.FILES, instance=expediente)                                                         
                             
            if formE.is_valid():                
                formE.save()                              
            
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found')) 
    
    context = {'form': formE, 'expediente': expediente, 'r1': r1, 'r2': r2, 'rF': rF}
    return render(request, 'Student/expediente.html', context)



def reportes(request):
    expediente = request.user.estudiante.expediente    
    r1 = None    
    r2 = None
    rF = None
    form1 = None
    form2 = None
    formF = None    
                
    if not expediente is None:        
        r1 = expediente.reporteParcial1
        r2 = expediente.reporteParcial2
        rF = expediente.reporteFinal                                
        if r1 is None:            
            form1 = Reporte1Form(auto_id='id_reporte1_%s')
            if request.method == 'POST':
                form1 = Reporte1Form(request.POST, request.FILES)                   
                if form1.is_valid():
                    print('r1 is None & form1 is valid')                    
                    r1 = form1.save()
                    expediente.reporteParcial1 = r1
                    expediente.save()
                    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
        else:             
            form1 = Reporte1Form(auto_id='id_reporte1_%s', instance = r1)
        #    if request.method == 'POST':
        #        form1 = Reporte1Form(request.POST, request.FILES, instance = r1)                                                                                     
        #        if form1.is_valid():                                        
        #            print('r1 is not None & form1 is valid')                    
        #            r1 = form1.save()  
        #            expediente.reporteParcial1 = r1
        #            expediente.save()
        #            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
                                                                      
            
        if r2 is None:             
            form2 = Reporte2Form(auto_id='id_reporte2_%s')
            if request.method == 'POST':
                form2 = Reporte2Form(request.POST, request.FILES)                
                if form2.is_valid(): 
                    print('r2 is None & form2 is valid')                                              
                    r2 = form2.save()
                    expediente.reporteParcial2 = r2
                    expediente.save()
                    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
        else:             
            form2 = Reporte2Form(auto_id='id_reporte2_%s', instance = r2)
        #    if request.method == 'POST':
        #        form2 = Reporte2Form(request.POST, request.FILES, instance = r2)     
        #        if form2.is_valid():    
        #            print('r2 is not None & form2 is valid')                                    
        #            r2 = form2.save()  
        #            expediente.reporteParcial2 = r2
        #            expediente.save()
        #            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
            
            
        if rF is None:             
            formF = ReporteFinalForm(auto_id='id_reporteF_%s')
            if request.method == 'POST':
                formF = ReporteFinalForm(request.POST, request.FILES)                                                                
                if formF.is_valid():  
                    print('rF is None & formF is valid')                                
                    rF = formF.save()
                    expediente.reporteFinal = rF
                    expediente.save()
                    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
        else:             
            formF = ReporteFinalForm(auto_id='id_reporteF_%s', instance = rF)
        #    if request.method == 'POST':
        #        formF = Reporte1Form(request.POST, request.FILES, instance = rF)                                                
        #        if formF.is_valid():
        #            print('rF is not None & formF is valid')                    
        #            rF = formF.save()  
        #            expediente.reporteFinal = rF
        #            expediente.save()
        #            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))                    
    
    context = {'expediente': expediente, 'form1': form1, 'form2': form2, 'formF': formF, 'r1': r1, 'r2': r2, 'rF': rF}
    return render(request, 'Student/reportes.html', context)

def deleteStudent(request, pk):

    # Te redirecciona a la misma pagina
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))    
    
    
def anteproyecto(request):
    data = ['id_observaciones', 'id_codigoUnion', 'id_estatus', 'id_docentes']
    estudiante = request.user.estudiante         
    anteproyecto = estudiante.anteproyecto       
    anteproyectos = Anteproyecto.objects.all()    
    estudiantes = Estudiante.objects.filter(anteproyecto = anteproyecto)
    enviados = anteproyectos.exclude(codigoUnion='0000000000').filter(estatus='ENVIADO')    
    codigo = '0000000000'     
    mensaje = ''                                       
    
    if anteproyecto is None:     
        form = AnteproyectoEstForm()   
        print('No tiene anteproyecto')        
        if request.method == 'POST':                        
            form = AnteproyectoEstForm(request.POST)
            
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
                            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))                                                
                    
                mensaje = 'Codigo invalido'                                                        
                                    
            if form.is_valid():            
                anteproyecto = form.save()
                if int(request.POST['numIntegrantes']) > 1:  
                    codigo = obtenerCodigo()                                                            
                                                
                print(codigo)                
                anteproyecto.codigoUnion=codigo
                anteproyecto.save()
                estudiante.anteproyecto=anteproyecto
                estudiante.save()                                
                return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
                    
    else:
        data.clear()
        data.append('id_docentes')         
        if anteproyecto.numIntegrantes == 1:
            data.append('id_codigoUnion')
                                                
        form = AnteproyectoViewForm(instance = anteproyecto)                                
    
    context = {'form': form, 'data': data, 'mensaje':mensaje, 'anteproyecto': anteproyecto, 'estudiantes': estudiantes}
    return render(request, 'Student/anteproyecto.html', context)
    


def crearAnteproyeco(request):
    
    context = {}
    return render(request, 'Student/registroAnteproyecto.html', context)

def verAnteproyeco(request):
    
    context = {}
    return render(request, 'Student/verAnteproyecto.html', context)

def createTeacher(request):

    context = {}
    return render(request, 'Teacher/create-account.html', context)


def updateTeacher(request, pk):

    context = {}
    return render(request, 'order_form.html', context)


def deleteTeacher(request, pk):

    # Te redirecciona a la misma pagina
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
