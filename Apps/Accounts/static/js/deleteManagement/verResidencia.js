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
                title: 'Desea eliminar este elemento de la Residencia?',
                text: elementValue.item(index).textContent,
                icon: 'warning',
                showCancelButton: true,
                confirmButtonColor: '#3085d6',
                cancelButtonColor: '#d33',
                confirmButtonText: 'Si, eliminar!',
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
                title: 'Desea cancelar la Residencia para este estudiante?' + '\n(Su anteproyecto también será cancelado)',
                text: elementValue.item(index).textContent,
                icon: 'warning',
                showCancelButton: true,
                confirmButtonColor: '#3085d6',
                cancelButtonColor: '#d33',
                confirmButtonText: 'Si, cancelar la residencia al estudiante!',
                allowOutsideClick: () => false,
                allowEscapeKey: () => false,
                preConfirm: () => {
                    Swal.fire(
                        'Cancelado!',
                        'Se ha cancelado la Residencia del estudiante.',
                        'success'
                    )                    
                    location.href = ref;
                }
            })
        })
    })
};