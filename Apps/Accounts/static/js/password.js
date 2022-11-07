function validarPassword(){
  var pass = document.getElementById('confirm_password').value;
  var conf_pass = document.getElementById('confirm_password1').value;

  if(pass != '' && conf_pass !== ''){
    if(pass === conf_pass){
        document.getElementById('recibido').innerHTML = "Password: " + conf_pass + "  coincide correctamente, se ah cambiado la contraseña";

        document.getElementById('recibido').style.color = 'green';
        document.getElementById('recibido').style.fontSize = '1em';
    
      }
      else{
        document.getElementById('recibido').innerHTML = "     Error: El valor de las contraseñas no coinciden";
        document.getElementById('recibido').style.color = 'red';
        document.getElementById('recibido').style.fontSize = '1em';
      }
  }

}
document.getElementById('enviar').addEventListener('click', validarPassword);


// ver o ocultar contraseña

function mostrarContrasena(){
    var tipo = document.getElementById("confirm_password");
    if(tipo.type == "password"){
        tipo.type = "text";
    }else{
        tipo.type = "password";
    }
}

function mostrarContrasena2(){
    var tipo = document.getElementById("confirm_password1");
    if(tipo.type == "password"){
        tipo.type = "text";
    }else{
        tipo.type = "password";
    }
}

// Estilos y comportamientos

function cambiarPass(){
    
}

function restablecerPass(){
   
}

function inicializarEstilos(){
    document.getElementById('confirm_password').addEventListener('click', cambiarPass);
    document.getElementById('confirm_password').addEventListener('blur', restablecerPass);
}

document.addEventListener('DOMContentLoaded', inicializarEstilos);