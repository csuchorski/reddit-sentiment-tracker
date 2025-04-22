import praw
import os
from dotenv import load_dotenv


class RedditScraper:
    def __init__(self):
        load_dotenv()
        self.reddit = self._create_reddit_instance()

    def _create_reddit_instance(self):
        reddit = praw.Reddit(
            client_id=os.getenv("REDDIT_CLIENT_ID"),
            client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
            user_agent=os.getenv("REDDIT_USER_AGENT")
        )

        return reddit

    def fetch_posts(self, subreddit_name, limit=5):
        subreddit = self.reddit.subreddit(subreddit_name)
        posts = []
        for post in subreddit.hot(limit=limit):
            posts.append({
                "id": post.id,
                "title": post.title,
                "body": post.selftext,
                "subreddit": subreddit.display_name,
                "created_at": post.created_utc
            })

        return posts

    def fetch_comments(self, post, limit=10):
        post.comments.replace_more(limit=0)
        comments = []
        for comment in post.comments.list()[:limit]:
            comments.append({
                "id": comment.id,
                "body": comment.body,
                "score": comment.score,
                "created_at": comment.created_utc
            })

        return comments

    def fetch_comments_by_id(self, post_id, limit=10):
        post = self.reddit.submission(id=post_id)
        return self.fetch_comments(post, limit=limit)
