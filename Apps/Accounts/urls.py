from django.urls import path
from .views import *

urlpatterns = [    
    path('login/', loginPage, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('404/', errorPage, name='404'),
    
    path('', home, name='home'),    
    path('student/', studentPage, name='student'),
    path('teacher/', teacherPage, name='teacher'),
                    
    path('profile/', estudianteViewProfile, name='studentProfile'),
    path('settings/', estudianteSettings, name='studentSettings'),
    path('expediente/', expediente, name='expediente'),    
    path('anteproyecto/', anteproyecto, name='anteproyecto'),
    path('editAnteproyecto/', editarAnteproyecto, name='editarAnteproyecto'),
    path('reportes/', reportes, name='reportes'),    
    path('removeDoc/<int:pk>', removeDoc, name='removeDoc'),    
    path('residencia', proyectoResidencia, name='residencia'),    
    path('createStudent/', createStudent, name='createStudent'),                    
    
]
