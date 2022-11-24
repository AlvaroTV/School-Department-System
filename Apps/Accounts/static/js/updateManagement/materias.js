const btnAdd = document.querySelectorAll('.btnAdd');
const elementValue = document.querySelectorAll('.elementValue');

window.onload = function() {
    btnAdd.forEach((btn, index) => {
        btn.addEventListener('click', function (e) {
            e.preventDefault();
            var target = e.target;            
            var ref = e.target.href;
            
            if (target.tagName === 'TD'){                                
                ref = target.childNodes[1].href;                
            }else if(target.tagName === 'P'){                   
                ref = target.parentNode.href;
            }                                                      
            
            Swal.fire({
                title: 'Desea agregar esta materia a su perfil academico?',
                text: elementValue.item(index).textContent,
                icon: 'warning',
                showCancelButton: true,
                confirmButtonColor: '#3085d6',
                cancelButtonColor: '#d33',
                confirmButtonText: 'Si, agregar!',
                allowOutsideClick: () => false,
                allowEscapeKey: () => false,
                preConfirm: () => {
                    Swal.fire(
                        'Agregado!',
                        'El elemento ha sido agregado.',
                        'success'
                    )                    
                    setTimeout(() => { location.href = ref; }, 1500);
                }
            })
        })
    })
};