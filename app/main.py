from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

from app.reddit_scraper import RedditScraper
from app.sentiment_anylyzer import SentimentAnalyzer
from app.sentiment_service import SentimentService

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


scraper = RedditScraper()
analyzer = SentimentAnalyzer()
service = SentimentService(scraper, analyzer)


@app.get("/analyze")
def analyze_subreddit(subreddit: str = Query(default="popular"), posts: int = 10, comments: int = 10):
    result = service.analyze_subreddit(subreddit, posts, comments)
    return result
