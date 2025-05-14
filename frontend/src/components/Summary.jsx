import "../styles/Summary.css";
import MeanDonutChart from "./MeanDonutChart";

function Summary({ meanTitleScore, meanBodyScore, meanCommentScore }) {
  return (
    <div className="summary">
      <h2>Sentiment Summary</h2>
      <div className="chart-container">
        <span className="donut-chart">
          <MeanDonutChart label="positive" score={meanTitleScore} />
          Mean Title Score: {meanTitleScore.toFixed(2)}
        </span>
        <span className="donut-chart">
          <MeanDonutChart label="neutral" score={meanBodyScore} />
          Mean Body Score: {meanBodyScore.toFixed(2)}
        </span>{" "}
        <span className="donut-chart">
          <MeanDonutChart label="negative" score={meanCommentScore} />
          Mean Comment Score: {meanCommentScore.toFixed(2)}
        </span>
      </div>
    </div>
  );
}

export default Summary;
