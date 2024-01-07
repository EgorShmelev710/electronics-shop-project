"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def coll():
    return Item("Смартфон", 10000, 20)


def test_init(coll):
    assert coll.name == 'Смартфон'


def test_calculate_total_price(coll):
    coll.calculate_total_price()
    assert coll.total_price == 200000


def test_apply_discount(coll):
    Item.pay_rate = 0.5
    coll.apply_discount()
    assert coll.price == 5000
