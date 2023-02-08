Swal.fire({
  title: 'Finalizar o agregar mas materias?',  
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
  confirmButtonText: 'Finalizar!'
}).then((result) => {
  if (result.isConfirmed) {
    Swal.fire(
      'Guardado!',
      'Las materias han sido guardadas.',
      'success'
    )
    location.href = '/anteproyecto'
  }
})
