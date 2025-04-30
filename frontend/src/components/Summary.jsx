function Summary({ meanTitleScore, meanBodyScore, meanCommentScore }) {
  return (
    <div className="summary">
      <h2>Sentiment Summary</h2>
      <p>Mean Title Score: {meanTitleScore.toFixed(2)}</p>
      <p>Mean Body Score: {meanBodyScore.toFixed(2)}</p>
      <p>Mean Comment Score: {meanCommentScore.toFixed(2)}</p>
    </div>
  );
}

export default Summary;
