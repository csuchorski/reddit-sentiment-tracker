from textblob import TextBlob

from app.models.base_model import SentimentAnalyzerModel


class TextBlobModel(SentimentAnalyzerModel):
    def analyze(self, text: str):
        result = TextBlob(text)
        return result.sentiment.polarity

    def get_label(self, score):
        if score > 0:
            return "positive"
        elif score < 0:
            return "negative"
        else:
            return "neutral"
