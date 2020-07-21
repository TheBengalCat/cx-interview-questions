from shopping_basket import Basket, calculate_basket_subtotal

catalog = {"peach": 1.53, "tomato": 0.60, "cornflakes": 2.35}


def test_new_basket_returns_empty_dict():

    basket = Basket()

    assert basket.contents == {}


def test_add_item_to_basket():

    basket = Basket()

    basket.add_item("peach", 2)

    assert len(basket.contents) == 1
    assert basket.contents["peach"] == 2


def test_add_multiple_items_to_basket():

    basket = Basket()

    basket.add_item("peach", 1)
    basket.add_item("tomato", 3)
    basket.add_item("corn", 8)

    assert len(basket.contents) == 3
    assert basket.contents["tomato"] == 3
    assert basket.contents["peach"] == 1
    assert basket.contents["corn"] == 8


def test_add_same_item_increases_quantity():

    basket = Basket()

    basket.add_item("peach", 1)
    basket.add_item("peach", 3)

    assert basket.contents["peach"] == 4


def test_calculate_basket_subtotal_with_empty_basket():

    basket = Basket()

    subtotal = calculate_basket_subtotal(basket, catalog)

    assert subtotal == 0


def test_calculate_basket_subtotal_with_one_item():

    basket = Basket()

    basket.add_item("tomato", 1)

    subtotal = calculate_basket_subtotal(basket, catalog)

    assert subtotal == 0.60


def test_calculate_basket_subtotal_with_multiple_items():

    basket = Basket()

    basket.add_item("tomato", 2)
    basket.add_item("peach", 1)

    subtotal = calculate_basket_subtotal(basket, catalog)

    assert subtotal == 2.73
