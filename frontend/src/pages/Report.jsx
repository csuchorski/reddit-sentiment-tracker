import { useParams, useLocation } from "react-router-dom";
import PostCard from "../components/PostCard";
import "../styles/Report.css";

function Report() {
  const { subreddit } = useParams();
  const location = useLocation();
  const data = location.state;

  console.log(data);

  return (
    <div className="report-container">
      <h1>Report for subreddit: {subreddit}</h1>
      <div className="post-grid">
        {data &&
          Object.entries(data).map(([postId, postData]) => (
            <PostCard
              key={postId}
              id={postId}
              title={postData.title}
              titleScore={postData.title_score}
              bodyScore={postData.body_score}
              commentScore={postData.comments_score}
            />
          ))}
      </div>
    </div>
  );
}

export default Report;
