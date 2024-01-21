from src.keyboard import Keyboard
import pytest


@pytest.fixture
def coll():
    return Keyboard('Dark Project KD87A', 9600, 5)


def test_str_keyboard(coll):
    assert str(coll) == "Dark Project KD87A"

    assert str(coll.language) == "EN"


def test_change_lang(coll):
    coll.change_lang()
    assert coll.language == 'RU'

    coll.change_lang()
    assert coll.language == 'EN'


def test_the_wrong_lang(coll):
    with pytest.raises(AttributeError):
        coll.language = 'CH'
