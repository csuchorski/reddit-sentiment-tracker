from app.models.vader_model import VaderModel


class ModelFactory():
    @staticmethod
    def create_model(model_type):
        model_type = model_type.lower()
        if model_type == "vader":
            return VaderModel()
        else:
            raise ValueError(f"Unknown model type: {model_type}")
