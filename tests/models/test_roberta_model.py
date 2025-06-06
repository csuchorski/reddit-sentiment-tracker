from unittest.mock import patch, MagicMock
import pytest
from app.models.roberta_model import RobertaModel


@pytest.fixture
def mock_pipeline():
    with patch("app.models.roberta_model.pipeline") as mock_pipeline:
        yield mock_pipeline


def test_analyze_positive(mock_pipeline):
    mock_classifier = MagicMock()
    mock_classifier.return_value = [{"label": "positive", "score": 0.85}]
    mock_pipeline.return_value = mock_classifier

    roberta = RobertaModel()
    score = roberta.analyze("I love this!")
    assert score == pytest.approx(0.85)
    assert roberta.get_label(score) == "positive"


def test_analyze_negative(mock_pipeline):
    mock_classifier = MagicMock()
    mock_classifier.return_value = [{"label": "negative", "score": 0.7}]
    mock_pipeline.return_value = mock_classifier

    roberta = RobertaModel()
    score = roberta.analyze("I hate this!")
    assert score == pytest.approx(-0.7)
    assert roberta.get_label(score) == "negative"


def test_analyze_neutral(mock_pipeline):
    mock_classifier = MagicMock()
    mock_classifier.return_value = [{"label": "neutral", "score": 0.5}]
    mock_pipeline.return_value = mock_classifier

    roberta = RobertaModel()
    score = roberta.analyze("The sky is blue")
    assert score == pytest.approx(0)
    assert roberta.get_label(score) == "neutral"


@pytest.mark.parametrize(
    "score, expected_label",
    [
        (1.0, "positive"),
        (0.01, "positive"),
        (0.0, "neutral"),
        (-0.01, "negative"),
        (-1.0, "negative"),
    ]
)
def test_get_label(score, expected_label):
    model = RobertaModel.__new__(RobertaModel)
    assert model.get_label(score) == expected_label
