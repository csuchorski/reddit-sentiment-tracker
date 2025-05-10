from app.models.roberta_model import RobertaModel
from app.models.text_blob_model import TextBlobModel
from app.models.vader_model import VaderModel


class ModelFactory():
    _model_cache = {}

    @staticmethod
    def create_model(model_type):
        model_type = model_type.lower()

        if model_type in ModelFactory._model_cache:
            return ModelFactory._model_cache[model_type]

        match model_type:
            case "vader":
                model = VaderModel()
            case "roberta":
                model = RobertaModel()
            case "textblob":
                model = TextBlobModel()
            case _:
                raise ValueError(f"Unknown model type: {model_type}")

        ModelFactory._model_cache[model_type] = model
        return model
