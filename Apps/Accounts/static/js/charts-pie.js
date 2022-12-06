/**
 * For usage, visit Chart.js docs https://www.chartjs.org/docs/latest/
 */


const anteproyectosE = document.getElementById('anteproyectosE').textContent
const anteproyectosP = document.getElementById('anteproyectosP').textContent
const anteproyectosER = document.getElementById('anteproyectosER').textContent
const anteproyectosRE = document.getElementById('anteproyectosRE').textContent
const anteproyectosA = document.getElementById('anteproyectosA').textContent
const anteproyectosR = document.getElementById('anteproyectosR').textContent

const residenciasI = document.getElementById('residenciasI').textContent
const residenciasEP = document.getElementById('residenciasEP').textContent
const residenciasP = document.getElementById('residenciasP').textContent
const residenciasF = document.getElementById('residenciasF').textContent

const config = {
  type: 'pie',
  data: data,
  options: {
    responsive: true,
    plugins: {
      legend: {
        position: 'top',
      },
      title: {
        display: true,
        text: 'Chart.js Pie Chart'
      }
    }
  },
};

const pieConfig1 = {
  type: 'pie',
  data: {
    datasets: [
      {
        data: [anteproyectosE, anteproyectosP, anteproyectosER, anteproyectosRE, anteproyectosA, anteproyectosR],
        /**
         * These colors come from Tailwind CSS palette
         * https://tailwindcss.com/docs/customizing-colors/#default-color-palette
         */
        backgroundColor: ['#73B761', '#2c3038', '#FE9666', '#F2C80F', '#4A8DDC', '#D83B01'],
        label: 'Dataset 1',
      },
    ],
    labels: ['ENVIADO', 'PENDIENTE', 'EN REVISION', 'REVISADO', 'ACEPTADO', 'RECHAZADO'],
  },
  options: {
    responsive: true,
    
    /**
     * Default legends are ugly and impossible to style.
     * See examples in charts.html to add your own legends
     *  */
    legend: {
      display: false,
    },
  },
}

const pieConfig2 = {
  type: 'doughnut',
  data: {
    datasets: [
      {
        data: [residenciasI, residenciasEP, residenciasP, residenciasF],
        /**
         * These colors come from Tailwind CSS palette
         * https://tailwindcss.com/docs/customizing-colors/#default-color-palette
         */
        backgroundColor: ['#2192FF', '#FCE700', '#7e3af2', '#38E54D', '#D83B01'],
        label: 'Dataset 1',
      },
    ],
    labels: ['INICIADA', 'EN PROCESO', 'PROROGA', 'FINALIZADA', 'RECHAZADA'],
  },
  options: {
    responsive: true,
    cutoutPercentage: 80,
    /**
     * Default legends are ugly and impossible to style.
     * See examples in charts.html to add your own legends
     *  */
    legend: {
      display: false,
    },
  },
}

// change this to the id of your chart element in HMTL
const pieCtx1 = document.getElementById('pie1')
const pieCtx2 = document.getElementById('pie2')
window.myPie1 = new Chart(pieCtx1, pieConfig1)
window.myPie2 = new Chart(pieCtx2, pieConfig2)
