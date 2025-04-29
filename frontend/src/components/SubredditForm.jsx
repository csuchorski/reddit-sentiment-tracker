import { useState } from "react";

function SubredditForm({ onSubmit }) {
  const [subreddit, setSubreddit] = useState("");
  const [postLimit, setPostLimit] = useState(10);
  const [commentLimit, setCommentLimit] = useState(30);

  const handleSubmit = (e) => {
    e.preventDefault();

    onSubmit(subreddit, postLimit, commentLimit);
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder="e.g. technology"
        value={subreddit}
        onChange={(e) => setSubreddit(e.target.value)}
        required
      />
      <input
        type="number"
        placeholder="10"
        value={postLimit}
        onChange={(e) => setPostLimit(e.target.value)}
      />
      <input
        type="number"
        placeholder="30"
        value={commentLimit}
        onChange={(e) => setCommentLimit(e.target.value)}
      />

      <button type="submit">Analyze</button>
    </form>
  );
}

export default SubredditForm;
