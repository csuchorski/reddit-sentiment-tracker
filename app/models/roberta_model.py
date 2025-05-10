from transformers import pipeline

from app.models.base_model import SentimentAnalyzerModel


class RobertaModel(SentimentAnalyzerModel):
    def __init__(self):
        self.classifier = pipeline(task="sentiment-analysis",
                                   model="cardiffnlp/twitter-roberta-base-sentiment-latest")

    def analyze(self, text: str):
        score_dict = self.classifier(text)[0]
        if score_dict["label"] == "negative":
            score = score_dict["score"] * -1
        elif score_dict["label"] == "positive":
            score = score_dict["score"]
        else:
            score = 0

        return score

    def get_label(self, score):
        if score > 0:
            return "positive"
        elif score < 0:
            return "negative"
        else:
            return "neutral"
