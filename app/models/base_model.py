from abc import ABC, abstractmethod


class SentimentAnalyzerModel(ABC):
    @abstractmethod
    def analyze(self, text):
        pass

    @abstractmethod
    def get_label(self, score):
        pass
