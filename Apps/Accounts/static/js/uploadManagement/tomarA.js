const btnSelect = document.querySelectorAll('.btnSelect');
const elementValue = document.querySelectorAll('.elementValueA');

window.onload = function() {
    btnSelect.forEach((btn, index) => {
        btn.addEventListener('click', function (e) {
            e.preventDefault();
            var target = e.target;            
            var ref = e.target.parentNode.href;                                             

            Swal.fire({
                title: 'Desea ser el Revisor de este anteproyecto?',
                text: elementValue.item(index).textContent,
                icon: 'warning',
                showCancelButton: true,
                confirmButtonColor: '#3085d6',
                cancelButtonColor: '#d33',
                confirmButtonText: 'Si, tomar!',
                allowOutsideClick: () => false,
                allowEscapeKey: () => false,
                preConfirm: () => {
                    Swal.fire(
                        'Asignado!',
                        'El anteproyecto le ha sido asignado.',
                        'success'
                    )                    
                    setTimeout(() => { location.href = ref; }, 1500);
                }
            })
        })
    })
};