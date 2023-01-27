from django.shortcuts import render, redirect
from django.core.mail import EmailMessage, BadHeaderError, send_mail

def enviar_email(asunto, mensaje, lista_destinos, tipo=None, estado=None):            

    # Anteproyecto - Para el Estudiante
    if tipo == 1:
        mensajes = {
            'ENVIADO': 'Felicidades, su anteproyecto se ha dado de alta. Le pedimos que este pendiente para las observcaciones que este pueda tener',            
            'PENDIENTE': 'Su proyecto se encuentra en el estado de PENDIENTE. Esto significa que esta bajo revision por posibles inconvenientes. Si todo esta bien, el estado del anteproyecto cambiara pronto.',            
            'EN REVISION': 'Feliciades, ya le han sido asignado ambos revisores a su anteproyecto. Le recomendamos ponerse en contacto con ellos lo mas pronto posible',            
            'REVISADO': 'Felicidades, su anteproyecto ha sido ACEPTADO por ambos revisores. Solo falta que sea revisado por la jefa del departamento de vinculacion para su autorizacion.',            
            'ACEPTADO': 'Felicidades, su anteproyecto ha sido ACEPTADO por la jefa del departamento de vinculacion. Ahora su anteproyecto ha pasado a ser un proyecto de residencia.',            
            'RECHAZADO': 'Lamentamos informarle que su anteproyecto ha sido RECHAZADO. Si tiene mas dudas puede acudir con la jefa del departamento de vinculacion',            
            'CANCELADO': 'Lamentamos informarle que su anteproyecto ha sido CANCELDADO. Si tiene mas dudas puede acudir con la jefa del departamento de vinculacion',                        
        }
        mensaje = mensajes.get(estado)    
            
    # Residencia - Para el Estudiante
    elif tipo == 2:
        mensajes = {
            'INICIADA': 'Su residencia ha comenzado. Recuerda que debes registrar el periodo de tu residencia y tambien debe subir los documentos de su expediente.',
            'EN PROCESO': 'Se la ha asignado un asesor interno y un revisor a su proyecto de residencias. Le recomendamos ponerse en contacto con ellos lo mas pronto posible.',
            'PRORROGA': 'Su proyecto de residencia ha entrado en periodo de prorroga.',
            'NO FINALIZADA': 'Lamentamos informarle que su proyecto de residencia no ha finalizado.',
            'RECHAZADA': 'Lamentamos informarle que su proyecto de residencia ha sido RECHAZADO.',
            'FINALIZADA': 'Felicidades, su proyecto de residencia ha concluido satiisfactoriamente.',
            'CANCELADA': 'Lamentamos informarle que su proyecto de residencia ha sido CANDELADO.',            
        }
        mensaje = mensajes.get(estado)    
        
    # Observacion anteproyecto - Para el Estudiante   
    elif tipo == 3:
        mensaje = 'Su anteproyecto tiene una observacion. Es importante que revises las observaciones que se han realizado y subas tus cambios lo mas pronto posible.'
    
    # Expediente
    elif tipo == 4:
        mensajes = {
            'COMPLETO': 'Su expediente esta completo. Solo falta que sus documentos sean revisados para verificar que no exista algun problema con ellos.',
            'FINALIZADO': 'Felicidades!. No se encontro ningun error con sus documentos. Ya puede pasar a la oficina de la jefa del departamento de vinculacion por su documento.',            
        }
        mensaje = mensajes.get(estado)    
            
        
    try:
        send_mail(
        asunto,
        mensaje,
        'jefatura.vinculacion.sistemas@itoaxaca.edu.mx',
        lista_destinos,
    )
    except BadHeaderError:
        return redirect('404')   
    
        