from typing import Mapping, Union, Sequence


class Basket:

    contents: Mapping[str, int] = {}

    def __init__(self):

        self.contents = {}

    def add_item(self, item: str, quantity: int):

        if item in self.contents:
            self.contents[item] += quantity

        else:
            self.contents[item] = quantity


def calculate_basket_subtotal(basket: Basket, catalog: Mapping[str, float]) -> float:

    subtotal: float = 0

    for item in basket.contents:

        subtotal += catalog[item] * basket.contents[item]

    return subtotal


def get_item_discounts(
    basket: Basket,
    catalog: Mapping[str, float],
    offers: Mapping[str, Mapping[str, Union[Sequence[int], float]]],
) -> float:

    discount: float = 0

    for item in basket.contents:

        if item in offers['PercentageDiscount']:

            discount += offers['PercentageDiscount'][item] * catalog[item] * basket.contents[item]

    return discount


def get_buy_x_get_y_discounts(
    basket: Basket,
    catalog: Mapping[str, float],
    offers: Mapping[str, Mapping[str, Union[Sequence[int], float]]],
) -> float:

    discount: float = 0

    for item in basket.contents:

        if item in offers['BuyXGetY']:

            x = offers['BuyXGetY'][item][0]
            y = offers['BuyXGetY'][item][1]

            items_needed_for_eligibility = x + y

            discount += basket.contents[item] // items_needed_for_eligibility * y * catalog[item]

    return round(discount, 2)
