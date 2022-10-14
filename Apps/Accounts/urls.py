from django.urls import path
from .views import *

urlpatterns = [    
    path('login/', loginPage, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('404/', errorPage, name='404'),
    
    path('', home, name='home'),    
    path('student/', studentPage, name='student'),
    path('teacher/', teacherPage, name='teacher'),
        
        
    #path('student/<int:pk>', student, name='student'),
    #path('students/', students, name='students'),
    path('profile/', estudianteViewProfile, name='studentProfile'),
    path('settings/', estudianteSettings, name='studentSettings'),
    path('expediente/', expediente, name='expediente'),
    #path('registroAnteproyecto/', crearAnteproyeco, name='registroAnteproyecto'),
    #path('verAnteproyecto/', verAnteproyeco, name='verAnteproyecto'),
    path('anteproyecto/', anteproyecto, name='anteproyecto'),
    path('reportes/', reportes, name='reportes'),
    
    path('createStudent/', createStudent, name='createStudent'),    
    path('deleteStudent/<int:pk>', deleteStudent, name='deleteStudent'),
    
    path('createTeacher/', createTeacher, name='createTeacher'),
    path('updateTeacher/<int:pk>', updateTeacher, name='updateTeacher'),
    path('deleteTeacher/<int:pk>', deleteTeacher, name='deleteTeacher'),  
  
        
    
]
