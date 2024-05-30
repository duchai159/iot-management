var ctx = document.getElementById("light_chart").getContext("2d");
var light_chart = new Chart(ctx, {
  type: "line",
  data: {
    labels: [],
    datasets: [
      {
        label: "Real-time Data",
        data: [],
        backgroundColor: "rgba(255, 205, 86, 0.2)",
        borderColor: "rgba(255, 205, 86, 0.9)",
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
          text: "Value (V)",
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
        text: "Real-time Light Chart",
                font: {
          size: 16,
        },
        position: "top",
        align: "center",
      },
    },
  },
});

function updateChartLight(value, time) {
      if (light_chart.data.labels.length >= maxDataPoints) {
        light_chart.data.labels.shift(); // Xóa nhãn cũ nhất
        light_chart.data.datasets[0].data.shift(); // Xóa dữ liệu cũ nhất
      }
      light_chart.data.labels.push(time);
      light_chart.data.datasets[0].data.push(value);
      light_chart.update();
}
