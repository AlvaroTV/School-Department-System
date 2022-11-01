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
    
    path('verEstudiante/<int:pk>', verEstudiante, name='verEstudiante'),       
    path('editarEstudiante/<int:pk>', editarEstudiante, name='editarEstudiante'),       
    path('removeEstudiante/<int:pk>', removeEstudiante, name='removeEstudiante'),       
    
    path('asignarAsesor/<int:pk>', asignarAsesor, name='asignarAsesor'),           
    path('asignarAsesorI/<int:pkA>/<int:pkD>', asignarAsesorI, name='asignarAsesorI'),           
    path('removeAsesor/<int:pk>', removeAsesor, name='removeAsesor'),           
    
    path('asignarRevisor/<int:pk>', asignarRevisor, name='asignarRevisor'),           
    path('asignarRevisorI/<int:pkA>/<int:pkD>', asignarRevisorI, name='asignarRevisorI'),           
    path('removeRevisor/<int:pk>', removeRevisor, name='removeRevisor'),           
    
    path('verDocente/<int:pk>', verDocente, name='verDocente'),           
    path('editarDocente/<int:pk>', editarDocente, name='editarDocente'),           
    path('altaDocente/', altaDocente, name='altaDocente'),           
]
