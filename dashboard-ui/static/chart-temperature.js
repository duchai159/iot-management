var ctx = document.getElementById("temperature_chart").getContext("2d");
var temperature_chart = new Chart(ctx, {
  type: "line",
  data: {
    labels: [],
    datasets: [
      {
        label: "Real-time Data",
        data: [],
        backgroundColor: "rgba(255, 99, 132, 0.2)",
        borderColor: "rgba(255, 99, 132, 0.6)",
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
          text: "Value (°C)",
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
        text: "Real-time Temperature Chart",
                font: {
          size: 16,
        },
        position: "top",
        align: "center",
      },
    },
  },
});

function updateChartTemp(value, time) {
      if (temperature_chart.data.labels.length >= maxDataPoints) {
        temperature_chart.data.labels.shift(); // Xóa nhãn cũ nhất
        temperature_chart.data.datasets[0].data.shift(); // Xóa dữ liệu cũ nhất
      }
      temperature_chart.data.labels.push(time);
      temperature_chart.data.datasets[0].data.push(value);
      temperature_chart.update();
}
