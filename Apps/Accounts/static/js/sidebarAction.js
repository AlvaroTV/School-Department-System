const url = window.location
const pathStrSplit = url.pathname.split('/')
const pathName = pathStrSplit[1]

const dashboard = document.getElementById('id_dashboard')
const a_dashboard = document.getElementById('a_dashboard')
const anteproyectos = document.getElementById('id_anteproyectos')
const a_anteproyectos = document.getElementById('a_anteproyectos')
const anteproyectosH = document.getElementById('id_anteproyectosH')
const a_anteproyectosH = document.getElementById('a_anteproyectosH')
const residencias = document.getElementById('id_residencias')
const a_residencias = document.getElementById('a_residencias')
const residenciasH = document.getElementById('id_residenciasH')
const a_residenciasH = document.getElementById('a_residenciasH')
const expedientes = document.getElementById('id_expedientes')
const a_expedientes = document.getElementById('a_expedientes')
const reportes = document.getElementById('id_reportes')
const a_reportes = document.getElementById('a_reportes')
const estudiantes = document.getElementById('id_estudiantes')
const a_estudiantes = document.getElementById('a_estudiantes')
const docentes = document.getElementById('id_docentes')
const a_docentes = document.getElementById('a_docentes')
const materias = document.getElementById('id_materias')
const a_materias = document.getElementById('a_materias')
const avisos = document.getElementById('id_avisos')
const a_avisos = document.getElementById('a_avisos')
const materias_admin = document.getElementById('id_materias_ad')
const a_materias_admin = document.getElementById('a_materias_ad')
const dependencias_admin = document.getElementById('id_dependencias_ad')
const a_dependencias_admin = document.getElementById('a_dependencias_ad')
const gen_reportes = document.getElementById('id_gen_reportes')
const a_gen_reportes = document.getElementById('a_gen_reportes')
const estudiantes_aut = document.getElementById('id_estudiantes_aut')
const a_estudiantes_aut = document.getElementById('a_estudiantes_aut')

console.log(url.pathname)
console.log(pathName)


if (pathName == 'anteproyectos' | pathName == 'verAnteproyecto' | pathName == 'editarAnteproyectoAdmin' | pathName == 'editarObservaciones' | pathName == 'asignarRevisor1' | pathName == 'asignarRevisor2' | pathName == 'anteproyectosTeacher' | pathName =='anteproyectoA' | pathName == 'agregarComentario' | pathName == 'anteproyecto' | pathName == 'editAnteproyecto' | pathName == 'compatibilidadA' | pathName == 'dependencias' | pathName == 'altaDependencia' | pathName == 'asesoresExternos'| pathName == 'altaAsesorE' | pathName == 'altaDomicilioD' | pathName == 'altaTitularD' | pathName == 'invitar') {
    anteproyectos.hidden = false
    //a_anteproyectos.classList.add("dark:text-blue-500");
    a_anteproyectos.classList.add("dark:text-blue-500");
    a_anteproyectos.classList.add("text-blue-500");
} else if (pathName == 'anteproyectosH' | pathName =='anteproyectoH') {
    anteproyectosH.hidden = false    
    a_anteproyectosH.classList.add("dark:text-blue-500");
    a_anteproyectosH.classList.add("text-blue-500");
} else if (pathName == 'residencias' | pathName == 'verResidencia' | pathName == 'editarResidenciaAdmin' | pathName == 'asignarAsesorIL' | pathName == 'asignarRevisorL' | pathName == 'residenciasTeacher' | pathName == 'residencia' | pathName == 'verReporte') {
    residencias.hidden = false
    a_residencias.classList.add("dark:text-blue-500");
    a_residencias.classList.add("text-blue-500");
} else if (pathName == 'residenciasH' | pathName == 'verResidenciaH') {
    residenciasH.hidden = false    
    a_residenciasH.classList.add("dark:text-blue-500");
    a_residenciasH.classList.add("text-blue-500");
} else if (pathName == 'expedientes' | pathName == 'verExpediente' | pathName == 'expediente') {
    expedientes.hidden = false
    a_expedientes.classList.add("dark:text-blue-500");
    a_expedientes.classList.add("text-blue-500");
} else if (pathName == 'estudiantes' | pathName == 'verEstudiante') {
    estudiantes.hidden = false
    a_estudiantes.classList.add("dark:text-blue-500");
    a_estudiantes.classList.add("text-blue-500");
} else if (pathName == 'docentes' | pathName == 'verDocente' | pathName == 'editarDocente' | pathName == 'altaDocente' | pathName == 'act_docente_anteproyectosA' | pathName == 'act_docente_anteproyectosH' | pathName == 'act_docente_residenciasA' | pathName == 'act_docente_residenciasH') {
    docentes.hidden = false
    a_docentes.classList.add("dark:text-blue-500");
    a_docentes.classList.add("text-blue-500");
} else if (pathName == '' | pathName == 'teacher' | pathName == 'profile' | pathName == 'settings' | pathName == 'tProfile' | pathName == 'tSettings' | pathName == 'student' | pathName == 'faqs' | pathName == 'changePassword' | pathName == 'faqs' | pathName == 'faqs_s' | pathName == 'faqs_t'){
    dashboard.hidden = false
    a_dashboard.classList.add("dark:text-blue-500");
    a_dashboard.classList.add("text-blue-500");
} else if (pathName == 'materias' ){
    materias.hidden = false
    a_materias.classList.add("dark:text-blue-500");
    a_materias.classList.add("text-blue-500");
} else if (pathName == 'reportes' ){
    reportes.hidden = false
    a_reportes.classList.add("dark:text-blue-500");
    a_reportes.classList.add("text-blue-500");
} else if (pathName == 'avisos' | pathName == 'crear_aviso'){
    avisos.hidden = false
    a_avisos.classList.add("dark:text-blue-500");
    a_avisos.classList.add("text-blue-500");
} else if (pathName == 'materias_a' | pathName == 'altaMateria' | pathName == 'editarMateria'){
    materias_admin.hidden = false
    a_materias_admin.classList.add("dark:text-blue-500");
    a_materias_admin.classList.add("text-blue-500");
} else if (pathName == 'dependencias_a' | pathName == 'alta_dependencia' | pathName == 'editar_dependencia' | pathName == 'ver_dependencia' | pathName == 'altaDependencia_a' | pathName == 'alta_titular_dep' | pathName == 'alta_domicilio_dep'){
    dependencias_admin.hidden = false
    a_dependencias_admin.classList.add("dark:text-blue-500");
    a_dependencias_admin.classList.add("text-blue-500");
} else if (pathName == 'generar_reportes' | pathName == 'generar_reporte_estudiante' | pathName == 'generar_reporte_anteproyectos' | pathName == 'generar_reporte_residencias'){
    gen_reportes.hidden = false
    a_gen_reportes.classList.add("dark:text-blue-500");
    a_gen_reportes.classList.add("text-blue-500");
} else if (pathName == 'estudiantes_autorizados' | pathName == 'subir_estudiantes_a' ){
    estudiantes_aut.hidden = false
    a_estudiantes_aut.classList.add("dark:text-blue-500");
    a_estudiantes_aut.classList.add("text-blue-500");
}


//window.location.href.toString().split(window.location.host)[1]


