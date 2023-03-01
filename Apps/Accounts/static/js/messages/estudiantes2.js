const btnDelete = document.querySelectorAll('.btnDelete');
const elementValue2 = document.querySelectorAll('.elementValue2');


Swal.fire({
  title: '¿Finalizar o agregar más materias?',  
  width: 600,
  padding: '3em',
  color: '#716add',
  background: '#fff url(/media/trees.png)',
  backdrop: `
      rgba(0,0,123,0.4)      
      left top
      no-repeat
    `,
  showCancelButton: true,
  cancelButtonColor: '#28a745',
  confirmButtonColor: '#3085d6',  
  cancelButtonText: 'Agregar materia',
  confirmButtonText: '¡Finalizar!'
}).then((result) => {
  if (result.isConfirmed) {
    Swal.fire(
      '¡Guardado!',
      'Las materias han sido guardadas.',
      'success'
    )
    location.href = '/anteproyecto'
  }
})

btnDelete.forEach((btn, index) => {
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
          title: '¿Desea remover esta materia?',
          text: elementValue2.item(index).textContent,
          icon: 'warning',
          showCancelButton: true,
          confirmButtonColor: '#3085d6',
          cancelButtonColor: '#d33',
          confirmButtonText: '¡Sí, remover!',
          allowOutsideClick: () => false,
          allowEscapeKey: () => false,
          preConfirm: () => {
              Swal.fire(
                  '¡Eliminado!',
                  'El elemento ha sido removido.',
                  'success'
              )                    
              location.href = ref;
          }
      })
  })
})