from app.sentiment_anylyzer import SentimentAnalyzer


def test_positive_sentiment():
    analyzer = SentimentAnalyzer()
    positive_input = "I love this!"

    result = analyzer.analyze(positive_input)
    label = analyzer.get_label(result)

    assert label == "positive"


def test_neutral_sentiment():
    analyzer = SentimentAnalyzer()
    neutral_input = "The sky is blue"

    result = analyzer.analyze(neutral_input)
    label = analyzer.get_label(result)

    assert label == "neutral"


def test_negative_sentiment():
    analyzer = SentimentAnalyzer()
    negative_input = "I hate this!"

    result = analyzer.analyze(negative_input)
    label = analyzer.get_label(result)

    assert label == "negative"
