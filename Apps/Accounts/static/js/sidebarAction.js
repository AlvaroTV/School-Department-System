const url = window.location
const pathStrSplit = url.pathname.split('/')
const pathName = pathStrSplit[1]

const dashboard = document.getElementById('id_dashboard')
const anteproyectos = document.getElementById('id_anteproyectos')
const anteproyectosH = document.getElementById('id_anteproyectosH')
const residencias = document.getElementById('id_residencias')
const residenciasH = document.getElementById('id_residenciasH')
const expedientes = document.getElementById('id_expedientes')
const reportes = document.getElementById('id_reportes')
const estudiantes = document.getElementById('id_estudiantes')
const docentes = document.getElementById('id_docentes')
const materias = document.getElementById('id_materias')

console.log('c:')
console.log(url.pathname)
console.log(pathName)



if (pathName == 'anteproyectos' | pathName == 'verAnteproyecto' | pathName == 'editarAnteproyectoAdmin' | pathName == 'editarObservaciones' | pathName == 'asignarRevisor1' | pathName == 'asignarRevisor2' | pathName == 'anteproyectosTeacher' | pathName =='anteproyectoA' | pathName =='anteproyectoH' | pathName == 'agregarComentario' | pathName == 'anteproyecto' | pathName == 'editAnteproyecto') {
    anteproyectos.hidden = false
} else if (pathName == 'anteproyectosH' ) {
    anteproyectosH.hidden = false    
} else if (pathName == 'residencias' | pathName == 'verResidencia' | pathName == 'editarResidenciaAdmin' | pathName == 'asignarAsesorIL' | pathName == 'asignarRevisorL' | pathName == 'residenciasTeacher' | pathName == 'residencia' | pathName == 'verReporte') {
    residencias.hidden = false
} else if (pathName == 'residenciasH' ) {
    residenciasH.hidden = false    
} else if (pathName == 'expedientes' | pathName == 'verExpediente' | pathName == 'expediente') {
    expedientes.hidden = false
} else if (pathName == 'estudiantes' | pathName == 'verEstudiante') {
    estudiantes.hidden = false
} else if (pathName == 'docentes' | pathName == 'verDocente') {
    docentes.hidden = false
} else if (pathName == '' | pathName == 'teacher' | pathName == 'profile' | pathName == 'settings' | pathName == 'tProfile' | pathName == 'tSettings' | pathName == 'student' | pathName == 'faqs' | pathName == 'changePassword'){
    dashboard.hidden = false
} else if (pathName == 'materias' ){
    materias.hidden = false
} else if (pathName == 'reportes' ){
    reportes.hidden = false
} 



//window.location.href.toString().split(window.location.host)[1]


