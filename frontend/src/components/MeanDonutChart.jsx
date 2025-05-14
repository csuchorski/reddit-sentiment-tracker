import { Chart as ChartJS, ArcElement } from "chart.js";
import { Doughnut } from "react-chartjs-2";

ChartJS.register(ArcElement);

function getPrimaryColor(label) {
  switch (label) {
    case "positive":
      return { bg: "rgba(0, 248, 74, 0.76)", border: "#06c755" };

    case "negative":
      return { bg: "rgba(255, 59, 59, 0.8)", border: "#e92e2e" };

    case "neutral":
    default:
      return { bg: "rgba(180,180,180,0.8)", border: "#888" };
  }
}

function MeanDonutChart({ label, score }) {
  const primaryColor = getPrimaryColor(label);

  const data = {
    datasets: [
      {
        label: "Positivity",
        data: [Math.abs(score), 1 - Math.abs(score)],
        backgroundColor: [primaryColor.bg, "rgba(255, 255, 255, 0.84)"],
        borderColor: [primaryColor.border, "rgba(54, 162, 235, 1)"],
        borderWidth: 1,
      },
    ],
  };

  return <Doughnut data={data} />;
}

export default MeanDonutChart;
