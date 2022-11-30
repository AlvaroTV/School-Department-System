const $uploadForm = document.getElementById('uploadForm');
//! Aqui debo agregar uno para cada formulario. En la pagina de reportes hay 3 Formularios. Ojito con eso.
(function() {
    $uploadForm.addEventListener('submit', function (e) {
        e.preventDefault();        
        console.log(e.target.href)
        Swal.fire({
            title: 'Desea enviar el docuemnto?',
            text: 'Una vez enviado no se podra modificar!',
            icon: 'question',
            showDenyButton: true,
            showCancelButton: true,
            confirmButtonText: 'Enviar',
            denyButtonText: `No enviar`,
            allowOutsideClick: () => false,
            allowEscapeKey: () => false,
        }).then((result) => {
            if (result.isConfirmed) {                                
                Swal.fire('Enviado!', '', 'success');                
                setTimeout(() => { $uploadForm.submit(); }, 1500);
            } else if (result.isDenied) {
                Swal.fire('Envio cancelado', '', 'info');
            }
        });
    });
})();