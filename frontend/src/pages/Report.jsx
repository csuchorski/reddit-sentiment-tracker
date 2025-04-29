import { useParams, useLocation } from "react-router-dom";

function Report() {
  const { subreddit } = useParams(); // Get the subreddit from the URL
  const location = useLocation(); // Access the state passed via navigate
  const data = location.state; // Get the data passed from SubredditForm

  return (
    <div>
      <h1>Report for subreddit: {subreddit}</h1>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  );
}

export default Report;
