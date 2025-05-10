from app.factory.model_factory import ModelFactory


class SentimentAnalyzer:
    def __init__(self, model_type="vader"):
        self.model_type = None
        self.model = None
        self.set_model(model_type)

    def set_model(self, model_type):
        if self.model_type != model_type:
            self.model_type = model_type
            self.model = ModelFactory.create_model(model_type)

    def analyze(self, text):
        return self.model.analyze(text)

    def get_label(self, score):
        return self.model.get_label(score)
