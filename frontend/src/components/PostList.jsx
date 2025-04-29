function PostList({ postData }) {
  if (!postData || typeof postData !== "object") {
    return <p>No posts found or loading...</p>;
  }
  const listItems = Object.entries(postData).map(([postId, post]) => (
    <li key={postId}>
      <strong>{post.title}</strong>
      <p>Title Sentiment Score:{post.title_score}</p>
      <p>Body Sentiment Score:{post.body_score}</p>
      <p>Average Comment Sentiment Score:{post.comments_score}</p>
    </li>
  ));

  return <ul id="post-list">{listItems}</ul>;
}

export default PostList;
