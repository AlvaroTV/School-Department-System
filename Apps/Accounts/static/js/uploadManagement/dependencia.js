const $uploadForm = document.getElementById('uploadForm');

(function() {
    $uploadForm.addEventListener('submit', function (e) {
        e.preventDefault();        
        console.log(e.target.href)
        Swal.fire({
            title: 'Los datos de la organización o empresa están correctos? ',
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
                $uploadForm.submit();
            } else if (result.isDenied) {
                Swal.fire('Envio cancelado', '', 'info');
            }
        });
    });
})();