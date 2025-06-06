import pytest
from app.factory.model_factory import ModelFactory
from app.models.roberta_model import RobertaModel
from app.models.text_blob_model import TextBlobModel
from app.models.vader_model import VaderModel


@pytest.fixture
def clear_model_cache():
    ModelFactory._model_cache.clear()


def test_create_roberta_model():
    model = ModelFactory.create_model("roberta")
    assert isinstance(model, RobertaModel)


def test_create_text_blob_model():
    model = ModelFactory.create_model("textblob")
    assert isinstance(model, TextBlobModel)


def test_create_vader_model():
    model = ModelFactory.create_model("vader")
    assert isinstance(model, VaderModel)


def test_create_invalid_model():
    with pytest.raises(ValueError, match="Invalid model type: invalid_model"):
        ModelFactory.create_model("invalid_model")


@pytest.mark.parametrize("model_type", ["vader", "roberta", "textblob"])
def test_model_cache(model_type):
    model1 = ModelFactory.create_model(model_type)
    model2 = ModelFactory.create_model(model_type)
    assert model1 is model2
