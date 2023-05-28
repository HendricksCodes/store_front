import pytest
from products import Product


def test_create_normal_product():
    product = Product("MacBook Air M2", price=1450, quantity=100)
    assert product.get_quantity() == 100
    assert product.is_active() is True


def test_create_product_with_invalid_details():
    with pytest.raises(Exception):
        Product("", price=1450, quantity=100)
    with pytest.raises(Exception):
        Product("MacBook Air M2", price=-1450, quantity=100)


def test_product_quantity_reaches_zero():
    product = Product("MacBook Air M2", price=1450, quantity=5)
    assert product.is_active() is True
    product.buy(5)
    assert product.get_quantity() == 0
    assert product.is_active() is True


def test_product_purchase_modifies_quantity_and_returns_right_output():
    product = Product("MacBook Air M2", price=1450, quantity=10)
    assert product.buy(5) == 7250.0
    assert product.get_quantity() == 5


def test_buying_larger_quantity_than_exists_invokes_exception():
    product = Product("MacBook Air M2", price=1450, quantity=10)
    with pytest.raises(Exception):
        product.buy(15)

