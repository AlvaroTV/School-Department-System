const url = window.location
const pathStrSplit = url.pathname.split('/')
const pathName = pathStrSplit[1]

const dashboard = document.getElementById('id_dashboard')
const anteproyectos = document.getElementById('id_anteproyectos')
const residencias = document.getElementById('id_residencias')
const expedientes = document.getElementById('id_expedientes')
const estudiantes = document.getElementById('id_estudiantes')
const docentes = document.getElementById('id_docentes')

console.log('c:')
console.log(url.pathname)
console.log(pathStrSplit)


if (pathName == 'anteproyectos' | pathName == 'verAnteproyecto' | pathName == 'editarAnteproyectoAdmin' | pathName == 'editarObservaciones' | pathName == 'asignarRevisor1' | pathName == 'asignarRevisor2') {
    anteproyectos.hidden = false
} else if (pathName == 'residencias' | pathName == 'verResidencia' | pathName == 'editarResidenciaAdmin' | pathName == 'asignarAsesorIL' | pathName == 'asignarRevisorL') {
    residencias.hidden = false
} else if (pathName == 'expedientes' | pathName == 'verExpediente') {
    expedientes.hidden = false
} else if (pathName == 'estudiantes' | pathName == 'verEstudiante') {
    estudiantes.hidden = false
} else if (pathName == 'docentes' | pathName == 'verDocente') {
    docentes.hidden = false
} else if (pathName == ''){
    dashboard.hidden = false
}



//window.location.href.toString().split(window.location.host)[1]


