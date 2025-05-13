import SubredditForm from "../components/SubredditForm";
import "../styles/Home.css";
function Home() {
  return (
    <div className="home">
      <h1>Subreddit analyzer</h1>
      <div>
        <SubredditForm />
      </div>
    </div>
  );
}

export default Home;
