"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def coll():
    return Item("Смартфон", 10000, 20)


def test_calculate_total_price(coll):
    coll.calculate_total_price()
    assert coll.total_price == 200000


def test_apply_discount(coll):
    Item.pay_rate = 0.5
    coll.apply_discount()
    assert coll.price == 5000


def test_get_name(coll):
    assert coll.get_name == 'Смартфон'


def test_get_name_setter(coll):
    coll.get_name = 'Смартфон105647747'
    assert coll.name == 'Смартфон10'
    coll.get_name = 'Смарт'
    assert coll.name == 'Смарт'


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5

def test__dunder_methods__(coll):
    assert repr(coll) == "Item('Смартфон', 10000, 20)"
    assert str(coll) == 'Смартфон'
