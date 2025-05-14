import { useParams, useLocation } from "react-router-dom";
import PostCard from "../components/PostCard";
import Summary from "../components/Summary";
import "../styles/Report.css";

function Report() {
  const { subreddit } = useParams();
  const location = useLocation();
  const data = location.state;
  const summary = data.summary;
  const posts = data.posts;
  console.log(data);

  return (
    <div className="report-container">
      <h1>Report for subreddit: {subreddit}</h1>
      <div className="subreddit-summary">
        {summary && (
          <Summary
            titleLabel={summary.title_label}
            bodyLabel={summary.body_label}
            commentLabel={summary.comment_label}
            meanTitleScore={summary.mean_title_score}
            meanBodyScore={summary.mean_body_score}
            meanCommentScore={summary.mean_comment_score}
          />
        )}
      </div>
      <div className="post-grid">
        {data &&
          Object.entries(posts).map(([postId, postData]) => (
            <PostCard
              key={postId}
              id={postId}
              title={postData.title}
              titleScore={postData.title_score}
              bodyScore={postData.body_score}
              commentScore={postData.mean_comment_score}
            />
          ))}
      </div>
    </div>
  );
}

export default Report;
