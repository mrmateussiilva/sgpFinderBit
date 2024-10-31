const ctx = document.getElementById("graph-vendas");

new Chart(ctx, {
  type: "bar",
  data: {
    labels: ["Vendedor 1", "Vendedor 2", "Vendedor 3"],
    datasets: [
      {
        label: "Vendas",
        data: [12, 19, 3],
        borderWidth: 1,
      },
    ],
  },
  options: {
    scales: {
      y: {
        beginAtZero: true,
      },
    },
  },
});
