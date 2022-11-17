/**
 * For usage, visit Chart.js docs https://www.chartjs.org/docs/latest/
 */
var dataPie1 = document.getElementById('dataPie1').textContent
const lista1 = list_to_array(dataPie1)
const dataP1 = split_list(lista1, 6)

const barConfig1 = {
  type: 'bar',
  data: {
    labels: dataP1[0],
    datasets: [
      {
        label: 'Total Estudiantes',
        backgroundColor: '#FF6D28',
        // borderColor: window.chartColors.red,
        borderWidth: 1,
        data: dataP1[1],
      },
      {
        label: 'Estudiantes con Anteproyecto',
        backgroundColor: '#6FEDD6',
        // borderColor: window.chartColors.blue,
        borderWidth: 1,
        data: dataP1[2],
      },
      {
        label: 'Anteproyectos Registrados',
        backgroundColor: '#FCE700',
        // borderColor: window.chartColors.blue,
        borderWidth: 1,
        data: dataP1[4],
      },
    ],
  },
  options: {
    responsive: true,
    legend: {
      display: false,
    },
  },
}

const barConfig2 = {
  type: 'bar',
  data: {
    labels: dataP1[0],
    datasets: [
      {
        label: 'Total Estudiantes',
        backgroundColor: '#A149FA',
        // borderColor: window.chartColors.red,
        borderWidth: 1,
        data: dataP1[1],
      },
      {
        label: 'Estudiantes con Residencia',
        backgroundColor: '#82CD47',
        // borderColor: window.chartColors.blue,
        borderWidth: 1,
        data: dataP1[3],
      },
      {
        label: 'Residencias Registradas',
        backgroundColor: '#2192FF',
        // borderColor: window.chartColors.blue,
        borderWidth: 1,
        data: dataP1[5],
      },
    ],
  },
  options: {
    responsive: true,
    legend: {
      display: false,
    },
  },
}


const barsCtx1 = document.getElementById('bars1')
const barsCtx2 = document.getElementById('bars2')
window.myBar = new Chart(barsCtx1, barConfig1)
window.myBar = new Chart(barsCtx2, barConfig2)


function list_to_array(list) {
  var data = list.replace(/[\[\]']+/g, '');
  data = data.replace(/\s/g, '');
  data = data.split(',');
  return data;
}

function split_list(data, numArrays) {
  const length = (data.length)/numArrays;
  console.log('lenght:',length);
  var inicio = 0
  var fin = 0
  var final_data = []
  // 12/3 = 4
  // 0 - 3      inicio = 4 * 0 = 0  // fin = (6*1)-1 = 5
  // 4 - 7      inicio = 4 * 1 = 4  // fin = (4*2)-1 = 7
  // 8 - 11     inicio = 4 * 2 = 8  // fin = (4*3)-1 = 11

  //numArrays = 6
  //24/6 = 4
  //0 - 3       Inicio = 6 * 0 = 0  // Fin = (4 * 1)-1 = 3  
  for (let i = 0; i <= (numArrays - 1); i++) {
    inicio = length * i
    fin = (length*(i+1))    
    final_data.push(data.slice(inicio, fin));    
  } 
  
  return final_data;
}