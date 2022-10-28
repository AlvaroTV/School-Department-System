from django.urls import path
from .views import *
from .adminViews import *

urlpatterns = [    
    # Globales           
    path('login/', loginPage, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('404/', errorPage, name='404'),    
    path('', home, name='home'),    
    path('student/', studentPage, name='student'),
    path('teacher/', teacherPage, name='teacher'),
    path('createStudent/', createStudent, name='createStudent'),                    
    
    # Estudiante                
    path('profile/', estudianteViewProfile, name='studentProfile'),
    path('settings/', estudianteSettings, name='studentSettings'),
    path('expediente/', expediente, name='expediente'),    
    path('anteproyecto/', anteproyecto, name='anteproyecto'),
    path('editAnteproyecto/', editarAnteproyecto, name='editarAnteproyecto'),
    path('reportes/', reportes, name='reportes'),    
    path('removeDoc/<int:pk>', removeDoc, name='removeDoc'),    
    path('residencia/', proyectoResidencia, name='residencia'),    
        
    # Admin
    path('anteproyectos', anteproyectos, name='anteproyectos'),    
    path('residencias', residencias, name='residencias'),        
    path('expedientes', expedientes, name='expedientes'),        
    path('estudiantes', estudiantes, name='estudiantes'),        
    path('docentes', docentes, name='docentes'),        
    path('verAnteproyecto/<int:pk>', verAnteproyecto, name='verAnteproyecto'),        
    path('editarAnteproyectoAdmin/<int:pk>', editarAnteproyectoAdmin, name='editarAnteproyectoAdmin'),        
    path('editarObservaciones/<int:pk>', editarObservaciones, name='editarObservaciones'),        
    path('eliminarObservacion/<int:pk>', eliminarObservacion, name='eliminarObservacion'),        
]
