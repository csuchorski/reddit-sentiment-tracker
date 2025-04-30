from statistics import mean
from app.reddit_scraper import RedditScraper
from app.sentiment_anylyzer import SentimentAnalyzer


class SentimentService:
    def __init__(self, scraper: RedditScraper, analyzer: SentimentAnalyzer):
        self.scraper = scraper
        self.analyzer = analyzer

    def analyze_subreddit(self, subreddit_name: str, post_limit: int = 10, comment_limit: int = 10):
        posts = self.scraper.fetch_posts(subreddit_name, limit=post_limit)

        post_reports = {}
        for post in posts:
            comments = self.scraper.fetch_comments_by_post_id(
                post["id"], limit=comment_limit)

            post_analysis = self._analyze_post(post, comments)
            post_reports[post["id"]] = post_analysis

        summary = self._generate_summary(post_reports.values())

        return {
            "summary": summary,
            "posts": post_reports
        }

    def _generate_summary(self, posts: list) -> dict:
        title_scores = [post["title_score"] for post in posts]
        body_scores = [post["body_score"] for post in posts]
        comment_scores = [post["mean_comment_score"] for post in posts]

        mean_title_score = mean(title_scores) if len(title_scores) else None
        mean_body_score = mean(body_scores) if len(body_scores) else None
        mean_comment_score = mean(comment_scores) if len(
            comment_scores) else None
        return {
            "mean_title_score": mean_title_score,
            "mean_body_score": mean_body_score,
            "mean_comment_score": mean_comment_score
        }

    def _analyze_post(self, post: dict, comments: list) -> dict:
        title_score = self.analyzer.analyze(post["title"])
        body_score = self.analyzer.analyze(post["body"])

        comment_scores = [self.analyzer.analyze(
            comment["body"]) for comment in comments]

        mean_comment_score = mean(comment_scores) if len(
            comment_scores) else None

        return {
            "title": post["title"],
            "title_score": title_score,
            "body_score": body_score,
            "mean_comment_score": mean_comment_score
        }
