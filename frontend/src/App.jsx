import { useState } from "react";
import SubredditForm from "./components/SubredditForm";
import "./App.css";

function App() {
  const [subredditData, setSubredditData] = useState(null);

  const analyzeSubreddit = async (subreddit, postLimit, commentLimit) => {
    try {
      const response = fetch(
        `http://localhost:8000/analyze?subreddit=${subreddit}&posts=${postLimit}&comments=${commentLimit}`
      );
      const data = (await response).json();
      setSubredditData(data);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div>
      <h1>Subreddit Sentiment Analyzer</h1>
      <SubredditForm onSubmit={analyzeSubreddit} />
    </div>
  );
}

export default App;
