const btnDelete = document.querySelectorAll('.btnDelete');
const btnAdd = document.querySelectorAll('.btnAdd');

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
                title: 'Esta seguro que quiere rechazar la invitacion?',                
                icon: 'warning',
                showCancelButton: true,
                confirmButtonColor: '#3085d6',
                cancelButtonColor: '#d33',
                confirmButtonText: 'Si, rechazar!',
                allowOutsideClick: () => false,
                allowEscapeKey: () => false,
                preConfirm: () => {
                    Swal.fire(
                        'Rechazada!',
                        'Invitacion rechazada.',
                        'success'
                    )                    
                    location.href = ref;
                }
            })
        })
    })

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
                title: 'Esta seguro que quiere aceptar la invitacion?',                
                icon: 'warning',
                showCancelButton: true,
                confirmButtonColor: '#3085d6',
                cancelButtonColor: '#d33',
                confirmButtonText: 'Si, aceptar!',
                allowOutsideClick: () => false,
                allowEscapeKey: () => false,
                preConfirm: () => {
                    Swal.fire(
                        'Aceptada!',
                        'Invitacion aceptada.',
                        'success'
                    )                    
                    location.href = ref;
                }
            })
        })
    })
};