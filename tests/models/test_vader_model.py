import pytest
from app.models.vader_model import VaderModel


def test_analyze_positive():
    model = VaderModel()
    positive_input = "I love this!"

    result = model.analyze(positive_input)

    assert result >= 0.05


def test_analyze_neutral():
    model = VaderModel()
    neutral_input = "The sky is blue"

    result = model.analyze(neutral_input)

    assert result < 0.05 and result > -0.05


def test_analyze_negative():
    model = VaderModel()
    negative_input = "I hate this!"

    result = model.analyze(negative_input)
    assert result <= -0.05


@pytest.mark.parametrize(
    "score, expected_label",
    [
        (1.0, "positive"),
        (0.05, "positive"),
        (0.04, "neutral"),
        (0.0, "neutral"),
        (-0.04, "neutral"),
        (-0.05, "negative"),
        (-1.0, "negative"),
    ]
)
def test_get_label(score, expected_label):
    model = VaderModel.__new__(VaderModel)
    assert model.get_label(score) == expected_label
