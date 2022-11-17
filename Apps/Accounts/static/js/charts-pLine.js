var dataLine = document.getElementById('anteproyectos_months').textContent
dataLine = list_to_array(dataLine)
const maxY = Math.max(...dataLine) + 2

const pLineConfig = {
    type: 'line',
    data: {
        labels: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
        datasets: [
            {
                label: 'Anteproyectos',
                data: dataLine,
                borderColor: '#91C483',
                backgroundColor: '#e3fcbf70',
                pointStyle: 'circle',
                pointRadius: 13,
                pointHoverRadius: 15
            }
        ]
    },
    options: {
        maintainAspectRatio: false,
        responsive: true,
        legend: {
            display: false,
        },
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true,
                    min: 0,
                    max: maxY,
                    stepSize: 1,
                }
            }]
        }
    },
};

function list_to_array(list) {
    var data = list.replace(/[\[\]']+/g, '');
    data = data.replace(/\s/g, '');
    data = data.split(',');
    return data;
}

const pLineCtx = document.getElementById('prueba')
window.myPLine = new Chart(pLineCtx, pLineConfig)
