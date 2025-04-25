from statistics import mean
from app.reddit_scraper import RedditScraper
from app.sentiment_anylyzer import SentimentAnalyzer


class SentimentService:
    def __init__(self, scraper: RedditScraper, analyzer: SentimentAnalyzer):
        self.scraper = scraper
        self.analyzer = analyzer

    def analyze_subreddit(self, subreddit_name: str, post_limit: int = 10, comment_limit: int = 10):
        posts = self.scraper.fetch_posts(subreddit_name, limit=post_limit)

        sentiment_report = {}
        for post in posts:
            title_score = self.analyzer.analyze(post["title"])
            body_score = self.analyzer.analyze(post["body"])
            comment_scores = []
            sentiment_report[post["id"]] = {
                "title": post["title"],
                "title_score": title_score,
                "body_score": body_score
            }

            comments = self.scraper.fetch_comments_by_post_id(
                post["id"], limit=comment_limit)

            for comment in comments:
                comment_score = self.analyzer.analyze(comment["body"])
                comment_scores.append(comment_score)

            sentiment_report[post["id"]]["comments_score"] = mean(
                comment_scores)

        return sentiment_report
