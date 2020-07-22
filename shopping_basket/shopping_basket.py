from typing import Mapping, Union, Sequence, Tuple


class Basket:
    """
    Class that defines a shopping basket. Each basket
    has a contents dictionary that products can be added
    to using the add_item function
    """

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
    catalogue: Mapping[str, float],
    offers: Mapping[str, Mapping[str, Union[Sequence[int], float]]] = None,
) -> Tuple[float]:
    # Checkout function calculates subtotal, discount and total for a given
    # Basket, catalogue and set of offers

    subtotal: float = 0
    discount: float = 0
    total: float = 0

    for item in basket.contents:
        if item in catalogue:
            subtotal += catalogue[item] * basket.contents[item]

    if offers:
        discount += get_item_discounts(basket, catalogue, offers)
        discount += get_buy_x_get_y_discounts(basket, catalogue, offers)

    subtotal = round(subtotal, 2)
    total = round(subtotal - discount, 2)

    return subtotal, discount, total


def get_item_discounts(
    basket: Basket,
    catalogue: Mapping[str, float],
    offers: Mapping[str, Mapping[str, Union[Sequence[int], float]]],
) -> float:
    # Calculates discount value for any items with a percentage offer

    discount: float = 0

    for item in basket.contents:

        if item in offers["PercentageDiscount"]:

            discount += (
                offers["PercentageDiscount"][item]
                * catalogue[item]
                * basket.contents[item]
            )

    return round(discount, 2)


def get_buy_x_get_y_discounts(
    basket: Basket,
    catalogue: Mapping[str, float],
    offers: Mapping[str, Mapping[str, Union[Sequence[int], float]]],
) -> float:
    # Calculates the discount value given a buy-x-get-y offer

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
                * catalogue[item]
            )

    return round(discount, 2)
