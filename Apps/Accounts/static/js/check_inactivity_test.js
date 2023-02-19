// Refresh Rate is how often you want to refresh the page 
// bassed off the user inactivity. 
var refresh_rate = 25; //<-- In seconds, change to your needs
var last_user_action = 0;
var has_focus = false;
var lost_focus_count = 0;
// If the user loses focus on the browser to many times 
// we want to refresh anyway even if they are typing. 
// This is so we don't get the browser locked into 
// a state where the refresh never happens.    
var focus_margin = 10;

// Reset the Timer on users last action
function reset() {
    last_user_action = 0;
    console.log("Reset");
}

function windowHasFocus() {
    has_focus = true;
}

function windowLostFocus() {
    has_focus = false;
    lost_focus_count++;
    console.log(lost_focus_count + " <~ Lost Focus");
}

// Count Down that executes ever second
setInterval(function () {
    last_user_action++;
    refreshCheck();
}, 1000);

// The code that checks if the window needs to reload
function refreshCheck() {
    var focus = window.onfocus;
    if (refresh_rate - last_user_action === 20) {
        let timerInterval;
        Swal.fire({
            title: 'Tu sesion esta por expirar, deseas continuar?',
            html: 'La sesion se cerrara en <b></b> segundos.',
            icon: 'warning',
            timer: 20000,
            timerProgressBar: true,
            didOpen: () => {
                Swal.showLoading()
                const b = Swal.getHtmlContainer().querySelector('b')
                timerInterval = setInterval(() => {
                    b.textContent = Math.trunc(Swal.getTimerLeft() / 1000)
                }, 1000)
            },
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#3085d6',
            confirmButtonText: 'Si, continuar!',
            cancelButtonText: 'Si, continuar!',
            allowOutsideClick: () => false,
            allowEscapeKey: () => false,
            preConfirm: () => {
                Swal.fire(
                    'Entendido!',
                    'Su sesion continua.',
                    'success'
                )
                //last_user_action = refresh_rate              
            }
        }).then((result) => {
            /* Read more about handling dismissals below */
            if (result.dismiss === Swal.DismissReason.timer) {
                window.location.reload();
                reset();
            }
        })
    }
    //if ((last_user_action >= refresh_rate && !has_focus && document.readyState == "complete") || lost_focus_count > focus_margin) {
    //    window.location.reload(); // If this is called no reset is needed
    //    reset(); // We want to reset just to make sure the location reload is not called.
    //}

}
window.addEventListener("focus", windowHasFocus, false);
window.addEventListener("blur", windowLostFocus, false);
window.addEventListener("click", reset, false);
window.addEventListener("mousemove", reset, false);
window.addEventListener("keypress", reset, false);
window.addEventListener("scroll", reset, false);
document.addEventListener("touchMove", reset, false);
document.addEventListener("touchEnd", reset, false);