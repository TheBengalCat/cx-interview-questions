from shopping_basket import Basket, calculate_basket_subtotal, get_item_discounts

catalog = {"peach": 1.53, "tomato": 0.60, "cornflakes": 2.35}

offers = {"BuyXGetY": {"peach": [2, 1]}, "PercentageDiscount": {"tomato": 0.25}}


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


def test_calculate_percentage_discount_for_one_item():
    # Discount tomato by 25%

    offers = {"BuyXGetY": {"": []}, "PercentageDiscount": {"tomato": 0.25}}

    basket = Basket()

    basket.add_item('tomato',1)

    discount = get_item_discounts(basket, catalog, offers)

    assert discount == 0.15

def test_calculate_percentage_discount_for_multiple_items():
    # Discount tomato by 25% and cornflakes by 50%

    offers = {"BuyXGetY": {"": []}, "PercentageDiscount": {"tomato": 0.25, "cornflakes": 0.50}}

    basket = Basket()

    basket.add_item('tomato', 1)
    basket.add_item('cornflakes', 2)

    discount = get_item_discounts(basket, catalog, offers)

    assert discount == 2.50
