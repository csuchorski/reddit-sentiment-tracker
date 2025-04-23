import time
from unittest.mock import patch, MagicMock
from app.reddit_scraper import RedditScraper


@patch("praw.Reddit")
@patch("app.reddit_scraper.load_dotenv")
def test_init(mock_load_dotenv, mock_reddit):
    scraper = RedditScraper()

    mock_load_dotenv.assert_called_once()
    mock_reddit.assert_called_once()


@patch("praw.Reddit")
@patch("app.reddit_scraper.load_dotenv")
@patch("app.reddit_scraper.os.getenv")
def test_create_reddit_instance(mock_getenv, mock_load_dotenv, mock_reddit):
    mock_getenv.side_effect = lambda x: {
        "REDDIT_CLIENT_ID": "fake_id",
        "REDDIT_CLIENT_SECRET": "fake_secret",
        "REDDIT_USER_AGENT": "fake_user_agent"
    }.get(x)

    scraper = RedditScraper()

    mock_reddit.assert_called_once_with(
        client_id="fake_id",
        client_secret="fake_secret",
        user_agent="fake_user_agent"
    )


@patch("praw.Reddit")
@patch("app.reddit_scraper.load_dotenv")
def test_fetch_posts(mock_load_dotenv, mock_reddit):
    mock_subreddit = MagicMock()
    mock_reddit.return_value.subreddit.return_value = mock_subreddit

    dummy_posts = []
    for i in range(3):
        post = MagicMock()
        post.id = f"id_{i}"
        post.title = f"title_{i}"
        post.selftext = f"body_{i}"
        post.created_utc = time.time()+i
        dummy_posts.append(post)

    mock_subreddit.display_name = "fake_subreddit_name"
    mock_subreddit.hot.return_value = dummy_posts

    scraper = RedditScraper()
    result = scraper.fetch_posts("fake_subreddit_name", limit=3)

    mock_reddit.return_value.subreddit.assert_called_once_with(
        "fake_subreddit_name")
    mock_subreddit.hot.assert_called_once_with(limit=3)

    assert len(result) == 3
    for i, post in enumerate(result):
        assert post["id"] == f"id_{i}"
        assert post["title"] == f"title_{i}"
        assert post["body"] == f"body_{i}"
        assert post["subreddit"] == "fake_subreddit_name"
        assert isinstance(post["created_at"], float)


@patch("praw.Reddit")
@patch("app.reddit_scraper.load_dotenv")
def test_fetch_comments(mock_load_dotenv, mock_reddit):
    mock_post = MagicMock()

    dummy_comments = []
    for i in range(5):
        comment = MagicMock()
        comment.id = f"id_{i}"
        comment.body = f"body_{i}"
        comment.score = f"score_{i}"
        comment.created_utc = time.time()+i
        dummy_comments.append(comment)

    mock_post.comments.list.return_value = dummy_comments

    scraper = RedditScraper()
    result = scraper.fetch_comments(mock_post, limit=3)

    mock_post.comments.replace_more.assert_called_once_with(limit=0)
    mock_post.comments.list.assert_called_once()

    assert len(result) == 3
    for i, comment in enumerate(result):
        assert comment["id"] == f"id_{i}"
        assert comment["body"] == f"body_{i}"
        assert comment["score"] == f"score_{i}"
        assert isinstance(comment["created_at"], float)


@patch("praw.Reddit")
@patch("app.reddit_scraper.load_dotenv")
def test_fetch_comments_by_post_id(mock_load_dotenv, mock_reddit):
    scraper = RedditScraper()
    mock_post = MagicMock()
    mock_reddit.return_value.submission.return_value = mock_post

    scraper.fetch_comments = MagicMock()
    scraper.fetch_comments.return_value = "mocked_comments"
    result = scraper.fetch_comments_by_post_id("fake_id", limit=5)

    mock_reddit.return_value.submission.assert_called_once_with(id="fake_id")
    scraper.fetch_comments.assert_called_once_with(mock_post, limit=5)
    assert result == "mocked_comments"
