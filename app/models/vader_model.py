from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from app.models.base_model import SentimentAnalyzerModel


class VaderModel(SentimentAnalyzerModel):
    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()

    def analyze(self, text):
        score_dict = self.analyzer.polarity_scores(text)

        return score_dict["compound"]

    def get_label(self, score):
        if score >= 0.05:
            return "positive"
        elif score <= -0.05:
            return "negative"
        else:
            return "neutral"
