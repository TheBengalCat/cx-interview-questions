from typing import Mapping, Union, Sequence, Tuple


class Basket:

    contents: Mapping[str, int] = {}

    def __init__(self):

        self.contents = {}

    def add_item(self, item: str, quantity: int):

        if item in self.contents:
            self.contents[item] += quantity

        else:
            self.contents[item] = quantity


def checkout_basket(
    basket: Basket,
    catalog: Mapping[str, float],
    offers: Mapping[str, Mapping[str, Union[Sequence[int], float]]],
) -> Tuple[float]:

    subtotal: float = 0
    discount: float = 0
    total: float = 0

    for item in basket.contents:
        if item in catalog:
            subtotal += catalog[item] * basket.contents[item]

    discount += get_item_discounts(basket, catalog, offers)
    discount += get_buy_x_get_y_discounts(basket, catalog, offers)

    subtotal = round(subtotal, 2)
    total = round(subtotal - discount, 2)

    return subtotal, discount, total


def get_item_discounts(
    basket: Basket,
    catalog: Mapping[str, float],
    offers: Mapping[str, Mapping[str, Union[Sequence[int], float]]],
) -> float:

    discount: float = 0

    for item in basket.contents:

        if item in offers["PercentageDiscount"]:

            discount += (
                offers["PercentageDiscount"][item]
                * catalog[item]
                * basket.contents[item]
            )

    return round(discount, 2)


def get_buy_x_get_y_discounts(
    basket: Basket,
    catalog: Mapping[str, float],
    offers: Mapping[str, Mapping[str, Union[Sequence[int], float]]],
) -> float:

    discount: float = 0

    for item in basket.contents:

        if item in offers["BuyXGetY"]:

            x = offers["BuyXGetY"][item][0]
            y = offers["BuyXGetY"][item][1]

            items_needed_for_eligibility = x + y

            discount += (
                basket.contents[item]
                // items_needed_for_eligibility
                * y
                * catalog[item]
            )

    return round(discount, 2)
