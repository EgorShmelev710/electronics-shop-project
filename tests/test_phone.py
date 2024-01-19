import pytest
from src.phone import Phone


@pytest.fixture
def coll():
    return Phone("iPhone 14", 120_000, 5, 2)


def test__repr__(coll):
    assert repr(coll) == "Phone('iPhone 14', 120000, 5, 2)"
    assert str(coll) == 'iPhone 14'
