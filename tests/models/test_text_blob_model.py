import pytest
from app.models.text_blob_model import TextBlobModel


def test_analyze_positive():
    model = TextBlobModel()
    positive_input = "I love this!"

    result = model.analyze(positive_input)

    assert result > 0.0


def test_analyze_neutral():
    model = TextBlobModel()
    neutral_input = "The sky is blue"

    result = model.analyze(neutral_input)

    assert result == 0.0


def test_analyze_negative():
    model = TextBlobModel()
    negative_input = "I hate this!"

    result = model.analyze(negative_input)
    assert result < 0


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
    model = TextBlobModel.__new__(TextBlobModel)
    assert model.get_label(score) == expected_label
