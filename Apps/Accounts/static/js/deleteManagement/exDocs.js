const btnDelete = document.querySelectorAll('.btnDelete');
const elementValue = document.querySelectorAll('.elementValue');

window.onload = function() {
    btnDelete.forEach((btn, index) => {
        btn.addEventListener('click', function (e) {
            e.preventDefault();
            var target = e.target;            
            var ref = e.target.href;

            if (target.tagName === 'svg'){                                
                ref = target.parentNode.href;
            }else if(target.tagName === 'path'){                             
                ref = target.parentNode.parentNode.href;
            }            

            Swal.fire({
                title: '¿Eliminar este documento?...' + '\n(No se podra revertir)',
                text: 'Expediente del estudiante: ' + elementValue.item(index).textContent,
                icon: 'warning',
                showCancelButton: true,
                confirmButtonColor: '#3085d6',
                cancelButtonColor: '#d33',
                confirmButtonText: '¡Sí, eliminar!',
                allowOutsideClick: () => false,
                allowEscapeKey: () => false,
                preConfirm: () => {
                    Swal.fire(
                        'Eliminado!',
                        'El documento ha sido eliminado.',
                        'success'
                    )                    
                    location.href = ref;
                }
            })
        })
    })
};