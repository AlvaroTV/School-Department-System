from django.urls import path
from .views import *
from .adminViews import *

urlpatterns = [    
    # Globales           
    path('login/', loginPage, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('404/', errorPage, name='404'),    
    path('', home, name='home'),   
    path('changePassword', changePassword, name='changePassword'), 
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
    path('anteproyectos/<int:page>/<int:orderB><int:filter>', anteproyectos, name='anteproyectos'),    
    path('residencias/<int:page>/<int:orderB><int:filter>', residencias, name='residencias'),        
    path('expedientes/<int:page>/<int:orderB><int:filter>', expedientes, name='expedientes'),        
    path('estudiantes/<int:page>/<int:orderB>', estudiantes, name='estudiantes'),        
    path('docentes/<int:page>/<int:orderB>', docentes, name='docentes'),       
    
    path('verExpediente/<int:pk>', verExpediente, name='verExpediente'),           
    path('eliminarExpediente/<int:pk>', eliminarExpediente, name='eliminarExpediente'),           
     
    path('verAnteproyecto/<int:pk>', verAnteproyecto, name='verAnteproyecto'),        
    path('editarAnteproyectoAdmin/<int:pk>', editarAnteproyectoAdmin, name='editarAnteproyectoAdmin'),        
    path('eliminarAnteproyecto/<int:pk>', eliminarAnteproyecto, name='eliminarAnteproyecto'),        
    
    path('editarObservaciones/<int:pk>', editarObservaciones, name='editarObservaciones'),        
    path('eliminarObservacion/<int:pk>', eliminarObservacion, name='eliminarObservacion'),   
    
    path('verEstudiante/<int:pk>', verEstudiante, name='verEstudiante'),       
    path('editarEstudiante/<int:pk>', editarEstudiante, name='editarEstudiante'),       
    path('removeEstudiante/<int:pk>', removeEstudiante, name='removeEstudiante'),       
    
    path('asignarRevisor1/<int:page>/<int:pk>', asignarRevisor1, name='asignarRevisor1'),           
    path('asignarRevisor1I/<int:pkA>/<int:pkD>', asignarRevisor1I, name='asignarRevisor1I'),           
    path('removeRevisor1/<int:pk>', removeRevisor1, name='removeRevisor1'),           
    
    path('asignarRevisor2/<int:page>/<int:pk>', asignarRevisor2, name='asignarRevisor2'),           
    path('asignarRevisor2I/<int:pkA>/<int:pkD>', asignarRevisor2I, name='asignarRevisor2I'),           
    path('removeRevisor2/<int:pk>', removeRevisor2, name='removeRevisor2'),           
    
    path('asignarAsesorIL/<int:page>/<int:pk>', asignarAsesorIL, name='asignarAsesorIL'),           
    path('asignarAsesorI/<int:pkR>/<int:pkD>', asignarAsesorI, name='asignarAsesorI'),           
    path('removeAsesorI/<int:pk>', removeAsesorI, name='removeAsesorI'),           
    
    path('asignarRevisorL/<int:page>/<int:pk>', asignarRevisorL, name='asignarRevisorL'),           
    path('asignarRevisor/<int:pkR>/<int:pkD>', asignarRevisor, name='asignarRevisor'),           
    path('removeRevisor/<int:pk>', removeRevisor, name='removeRevisor'),           
    
    path('verDocente/<int:pk>', verDocente, name='verDocente'),           
    path('editarDocente/<int:pk>', editarDocente, name='editarDocente'),           
    path('altaDocente/', altaDocente, name='altaDocente'), 
    
    path('verResidencia/<int:pk>', verResidencia, name='verResidencia'),        
    path('eliminarResidencia/<int:pk>', eliminarResidencia, name='eliminarResidencia'),        
    path('editarResidenciaAdmin/<int:pk>', editarResidenciaAdmin, name='editarResidenciaAdmin'),    
    
    path('eliminarEstudiante/<int:pk>', eliminarEstudiante, name='eliminarEstudiante'),       
    path('eliminarDocente/<int:pk>', eliminarDocente, name='eliminarDocente'),       
              
]
