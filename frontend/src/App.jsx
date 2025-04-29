import { useState } from "react";
import SubredditForm from "./components/SubredditForm";
import "./App.css";
import PostList from "./components/PostList";

function App() {
  const [subredditData, setSubredditData] = useState(null);

  const analyzeSubreddit = async (subreddit, postLimit, commentLimit) => {
    try {
      const response = await fetch(
        `http://localhost:8000/analyze?subreddit=${subreddit}&posts=${postLimit}&comments=${commentLimit}`
      );
      const data = await response.json();
      setSubredditData(data);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div>
      <h1>Subreddit Sentiment Analyzer</h1>
      <SubredditForm onSubmit={analyzeSubreddit} />
      {subredditData && <PostList postData={subredditData} />}
    </div>
  );
}

export default App;
