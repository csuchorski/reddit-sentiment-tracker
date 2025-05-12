import { useState } from "react";
import { useNavigate } from "react-router-dom";

function SubredditForm() {
  const [subreddit, setSubreddit] = useState("");
  const [postLimit, setPostLimit] = useState(4);
  const [commentLimit, setCommentLimit] = useState(10);
  const [model, setModel] = useState("roberta");
  const navigate = useNavigate();

  const fetchData = async () => {
    const response = await fetch(
      `http://localhost:8000/analyze?subreddit=${subreddit}&posts=${postLimit}&comments=${commentLimit}&model=${model}`
    );

    if (!response.ok) {
      throw new Error("Failed to fetch data");
    }

    return response.json();
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const data = await fetchData();
      navigate(`/report/${subreddit}`, { state: data });
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <form className="form" onSubmit={handleSubmit}>
      <div className="field">
        <label htmlFor="subreddit" className="label">
          Subreddit
        </label>
        <input
          className="input"
          type="text"
          id="subreddit"
          placeholder="e.g. technology"
          value={subreddit}
          onChange={(e) => setSubreddit(e.target.value)}
          required
        />
      </div>
      <div className="field">
        <label htmlFor="postLimit" className="label">
          Post limit
        </label>
        <input
          className="input"
          type="number"
          id="postLimit"
          placeholder="10"
          value={postLimit}
          onChange={(e) => setPostLimit(e.target.value)}
        />
      </div>
      <div className="field">
        <label htmlFor="commentLimit" className="label">
          Comment Limit
        </label>
        <input
          className="input"
          type="number"
          id="commentLimit"
          placeholder="30"
          value={commentLimit}
          onChange={(e) => setCommentLimit(e.target.value)}
        />
      </div>

      <div className="field">
        <fieldset>
          <legend>Select model used for analysis</legend>
          <label>
            <input
              type="radio"
              value="vader"
              checked={model === "vader"}
              onChange={() => setModel("vader")}
            />
            VADER
          </label>
          <label>
            <input
              type="radio"
              value="TextBlob"
              checked={model === "TextBlob"}
              onChange={() => setModel("TextBlob")}
            />
            TextBlob
          </label>
          <label>
            <input
              type="radio"
              value="roberta"
              checked={model === "roberta"}
              onChange={() => setModel("roberta")}
            />
            RoBERTa
          </label>
        </fieldset>
      </div>

      <button type="submit">Analyze</button>
    </form>
  );
}

export default SubredditForm;
