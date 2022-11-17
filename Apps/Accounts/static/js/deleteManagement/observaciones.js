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
                title: 'Eliminar esta Observacion?...' + '\n(No se podra revertir)',
                text: 'Elaborada por: ' + elementValue.item(index).textContent,
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
                    setTimeout(() => { location.href = ref; }, 1500);                    
                }
            })
        })
    })
};