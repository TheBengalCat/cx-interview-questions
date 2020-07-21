from shopping_basket import Basket, checkout_basket, get_item_discounts, get_buy_x_get_y_discounts

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


def test_checkout_basket_with_empty_basket():

    basket = Basket()

    subtotal, discount, total = checkout_basket(basket, catalog, offers)

    assert subtotal == 0
    assert discount == 0
    assert total == 0


def test_calculate_basket_subtotal_with_one_item():

    basket = Basket()

    basket.add_item("tomato", 1)

    subtotal, discount, total = checkout_basket(basket, catalog, offers)

    assert subtotal == 0.60



def test_calculate_basket_subtotal_with_multiple_items():

    basket = Basket()

    basket.add_item("tomato", 2)
    basket.add_item("peach", 1)

    subtotal, discount, total = checkout_basket(basket, catalog, offers)

    assert subtotal == 2.73


def test_calculate_percentage_discount_for_one_item():
    # Discount tomato by 25%

    offers = {"BuyXGetY": {"": []}, "PercentageDiscount": {"tomato": 0.25}}

    basket = Basket()

    basket.add_item('tomato', 1)

    subtotal, discount, total = checkout_basket(basket, catalog, offers)

    assert subtotal == 0.60
    assert discount == 0.15
    assert total == 0.45


def test_calculate_percentage_discount_for_multiple_items():
    # Discount tomato by 25% and cornflakes by 50%

    offers = {"BuyXGetY": {"": []}, "PercentageDiscount": {"tomato": 0.25, "cornflakes": 0.50}}

    basket = Basket()

    basket.add_item('tomato', 1)
    basket.add_item('cornflakes', 2)

    subtotal, discount, total = checkout_basket(basket, catalog, offers)

    assert subtotal == 5.30
    assert discount == 2.50
    assert total == 2.80

def test_calculate_buy_x_get_y_for_one_item_type():
    # Buy 2 Get 1 Free on peaches

    offers = {"BuyXGetY": {"peach": [2, 1]}, "PercentageDiscount": {"cornflakes": 0.25}}

    basket = Basket()

    basket.add_item('peach', 3)

    subtotal, discount, total = checkout_basket(basket, catalog, offers)

    assert subtotal == 4.59
    assert discount == 1.53
    assert total == 3.06


def test_calculate_buy_x_get_y_for_multiple_items():
    # Buy 2 Get 1 Free on peaches && Buy 3 Get 2 Free on tomatos

    offers = {"BuyXGetY": {"peach": [2, 1], "tomato": [3, 2]}, "PercentageDiscount": {"cornflakes": 0.25}}

    basket = Basket()

    basket.add_item('peach', 3)
    basket.add_item('tomato', 15)

    subtotal, discount, total = checkout_basket(basket, catalog, offers)

    assert subtotal == 13.59
    assert discount == 5.13
    assert total == 8.46


def test_buy_three_get_two_and_buy_four_get_one():
    # Buy 4 Get 1 Free on peaches && Buy 3 Get 2 Free on tomatos

    offers = {"BuyXGetY": {"peach": [4, 1], "tomato": [3, 2]}, "PercentageDiscount": {"cornflakes": 0.25}}

    basket = Basket()

    basket.add_item('peach', 16)
    basket.add_item('tomato', 23)

    subtotal, discount, total = checkout_basket(basket, catalog, offers)

    assert subtotal == 38.28
    assert discount == 9.39
    assert total == 28.89

def test_multiple_buy_x_get_y_offers_with_excess_and_inelegible_quantities():
    # Buy 3 Get 1 Free on peaches && Buy 3 Get 2 Free on tomatos

    offers = {"BuyXGetY": {"peach": [3, 1], "tomato": [3, 2]}, "PercentageDiscount": {"cornflakes": 0.25}}

    basket = Basket()

    basket.add_item('peach', 23)
    basket.add_item('tomato', 4)
    basket.add_item('corn', 5)

    subtotal, discount, total = checkout_basket(basket, catalog, offers)

    assert subtotal == 37.59
    assert discount == 7.65
    assert total == 29.94


def test_both_offers_being_used_on_seperate_items():
    # Buy 3 Get 1 Free on peaches && 25% off cornflakes

    offers = {"BuyXGetY": {"peach": [3, 1], "tomato": [3, 2]}, "PercentageDiscount": {"cornflakes": 0.25}}

    basket = Basket()

    basket.add_item('peach', 4)
    basket.add_item('cornflakes', 5)

    subtotal, discount, total = checkout_basket(basket, catalog, offers)

    assert subtotal == 17.87
    assert discount == 4.47
    assert total == 13.40