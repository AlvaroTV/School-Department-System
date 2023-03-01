const btnDelete = document.querySelectorAll('.btnDelete');
const btnDelete2 = document.querySelectorAll('.btnDelete2');
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
                title: '¿Desea eliminar este elemento del Anteproyecto?',
                text: elementValue.item(index).textContent,
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
                        'El elemento ha sido removido.',
                        'success'
                    )                    
                    location.href = ref;
                }
            })
        })
    })

    btnDelete2.forEach((btn, index) => {
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
                title: '¿Desea cancelar el Anteproyecto para este estudiante?',
                text: elementValue.item(index).textContent,
                icon: 'warning',
                showCancelButton: true,
                confirmButtonColor: '#3085d6',
                cancelButtonColor: '#d33',
                confirmButtonText: '¡Sí, cancelar el Anteproyecto del estudiante!',
                allowOutsideClick: () => false,
                allowEscapeKey: () => false,
                preConfirm: () => {
                    Swal.fire(
                        'Cancelado!',
                        'Se ha cancelado el Anteproyecto del estudiante.',
                        'success'
                    )                    
                    location.href = ref;
                }
            })
        })
    })
};