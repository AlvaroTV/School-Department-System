$.datepicker.regional['es'] = {
    closeText: 'Cerrar',
    prevText: '< Ant',
    nextText: 'Sig >',
    currentText: 'Hoy',
    monthNames: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
    monthNamesShort: ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'],
    dayNames: ['Domingo', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado'],
    dayNamesShort: ['Dom', 'Lun', 'Mar', 'Mié', 'Juv', 'Vie', 'Sáb'],
    dayNamesMin: ['Do', 'Lu', 'Ma', 'Mi', 'Ju', 'Vi', 'Sá'],
    weekHeader: 'Sm',    
    dateFormat: 'mm/dd/yy',
    //dateFormat: 'dd/mm/yy',
    firstDay: 1,
    isRTL: false,
    showMonthAfterYear: false,
    yearSuffix: ''
};

$.datepicker.setDefaults($.datepicker.regional['es']);

$(document).ready(function () {

    $('#id_periodoI_d').datepicker({
        changeMonth: true,
        changeYear: true
    });
    $('#id_periodoI_d').datepicker('show');

    $('#id_periodoI_h').datepicker({
        changeMonth: true,
        changeYear: true
    });
    $('#id_periodoI_h').datepicker('show');

    $('#id_periodoF_d').datepicker({
        changeMonth: true,
        changeYear: true
    });
    $('#id_periodoF_d').datepicker('show');    

    $('#id_periodoF_h').datepicker({
        changeMonth: true,
        changeYear: true
    });
    $('#id_periodoF_h').datepicker('show');
});