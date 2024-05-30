var ctx = document.getElementById("gas_chart").getContext("2d");
var gas_chart = new Chart(ctx, {
  type: "line",
  data: {
    labels: [],
    datasets: [
      {
        label: "Real-time Data",
        data: [],
        backgroundColor: "rgba(54, 162, 235, 0.2)",
        borderColor: "rgba(54, 162, 235, 0.6)",
        borderWidth: 1,
      },
    ],
  },
  options: {
    scales: {
      x: {
        beginAtZero: true,
        title: {
          display: true,
          text: "Time (HH:mm:ss)",
        },
      },
      y: {
        beginAtZero: true,
        
        title: {
          display: true,
          text: "Value (ppm)",
        },
      },
    },
    plugins: {
      zoom: {
        pan: {
          enabled: true,
          mode: "x", // Cho phép cuộn ngang
          speed: 10,
          threshold: 10,
        },
        zoom: {
          wheel: {
            enabled: true,
          },
          drag: {
            enabled: true,
          },
          pinch: {
            enabled: true,
          },
          mode: "x", // Cho phép phóng to, thu nhỏ ngang
          speed: 0.1,
        },
      },

      title: {
        display: true,
        text: "Real-time Gas Chart",
                font: {
          size: 16,
        },
        position: "top",
        align: "center",
      },
    },
  },
});

function updateChartGas(value, time){
      if (gas_chart.data.labels.length >= maxDataPoints) {
        gas_chart.data.labels.shift(); // Xóa nhãn cũ nhất
        gas_chart.data.datasets[0].data.shift(); // Xóa dữ liệu cũ nhất
      }
      gas_chart.data.labels.push(time);
      gas_chart.data.datasets[0].data.push(value);
      gas_chart.update();
}
