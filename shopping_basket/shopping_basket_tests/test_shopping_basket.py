from shopping_basket import Basket

def test_new_basket_returns_empty_dict():

    basket = Basket()

    assert basket.contents == {}

def test_add_item_to_basket():

    basket = Basket()

    basket.add_item('peach', 2)

    assert len(basket.contents) == 1
    assert basket.contents['peach'] == 2