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
