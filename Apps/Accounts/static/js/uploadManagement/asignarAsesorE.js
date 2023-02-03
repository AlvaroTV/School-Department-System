const btnSelect = document.querySelectorAll('.btnSelect');
const elementValue = document.querySelectorAll('.elementValue');

window.onload = function() {
    btnSelect.forEach((btn, index) => {
        btn.addEventListener('click', function (e) {
            e.preventDefault();
            var target = e.target;            
            var ref = e.target.href;
            console.log(target)

            if (target.tagName === 'svg'){                                
                ref = target.parentNode.href;
            }else if(target.tagName === 'path'){                             
                ref = target.parentNode.parentNode.href;
            }            

            console.log(ref)

            Swal.fire({
                title: 'Asignar este asesor externo al anteproyecto?',
                text: elementValue.item(index).textContent,
                icon: 'warning',
                showCancelButton: true,
                confirmButtonColor: '#3085d6',
                cancelButtonColor: '#d33',
                confirmButtonText: 'Si, asignar!',
                allowOutsideClick: () => false,
                allowEscapeKey: () => false,
                preConfirm: () => {
                    Swal.fire(
                        'Asignado!',
                        'El asesor ha sido asignado correctamente.',
                        'success'
                    )                    
                    location.href = ref;
                }
            })
        })
    })
};