import "../styles/PostCard.css";

function PostCard({ id, title, titleScore, bodyScore, commentScore }) {
  return (
    <div className="post-card">
      <h3 className="post-title">{title}</h3>
      <p>{id}</p>
      <div className="scores-container">
        <div className="score">
          <span className="score-label">Title score: </span>
          <span className="score-value">{titleScore.toFixed(2)}</span>
        </div>
        <div className="score">
          <span className="score-label">Body score: </span>
          <span className="score-value">{bodyScore.toFixed(2)}</span>
        </div>
        <div className="score">
          <span className="score-label">Comment score: </span>
          <span className="score-value">{commentScore.toFixed(2)}</span>
        </div>
      </div>
    </div>
  );
}

export default PostCard;
