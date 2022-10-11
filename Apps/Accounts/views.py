from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import *
# Create your views here.

# * Pagina principal para los maistros
def home(request):

    context = {}
    return render(request, 'Global/dashboard.html', context)


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


# * Pagina que regresa datos de un alumno
def student(request, pk):

    context = {}
    return render(request, 'customer.html', context)

# * Regresa datos de todos los estudiantes
def students(request):

    context = {}
    return render(request, 'products.html', context)

# * Se crea el estudiante
def createStudent(request):
    data = ['id_fotoUsuario', 'id_institutoSeguridadSocial',
            'id_numSeguridadSocial', 'id_expediente', 'id_correoElectronico', 'id_curp']
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
        if request.method == 'POST':            
            form1 = Reporte1Form(instance = r1)            
            form2 = Reporte2Form(instance = r2)           
            formF = ReporteFinalForm(instance = rF)        
                        
            if form1.is_valid():                
                f1 = form1.save()                
                expediente.reporteParcial1 = f1                
                expediente.save()
                                                    
            if form2.is_valid():
                f2 = form2.save()
                expediente.reporteParcial2 = f2
                expediente.save()
                        
            print(f'{formF.is_valid()}')                
            if formF.is_valid():
                fF = formF.save()
                expediente.reporteFinal = fF
                expediente.save()                
            
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))                     
    
    context = {'expediente': expediente, 'form1': form1, 'form2': form2, 'formF': formF, 'r1': r1, 'r2': r2, 'rF': rF}
    return render(request, 'Student/reportes.html', context)

def deleteStudent(request, pk):

    # Te redirecciona a la misma pagina
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))


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


def studentPage(request):

    context = {}
    return render(request, 'user.html', context)


def registerPage(request):

    context = {}
    return render(request, 'register.html', context)


def accountSettings(request):

    context = {}
    return render(request, 'account_settings.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')
