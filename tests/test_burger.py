from unittest.mock import Mock
from data import TestText
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE


class TestBurger:
    def test_set_bun(self):
        mock_bun = Mock()
        mock_bun.bun = Bun(TestText.bun_name, TestText.bun_price)
        burger = Burger()
        burger.set_buns(mock_bun.bun)

        assert burger.bun.get_name() == TestText.bun_name

    def test_add_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)

        assert len(burger.ingredients) == 1

    def test_remove_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)

        assert len(burger.ingredients) == 0

    def test_move_ingredient(self):
        burger = Burger()
        mock_ingredient_1 = Mock()
        mock_ingredient_2 = Mock()
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)
        burger.move_ingredient(0, 1)

        assert burger.ingredients == [mock_ingredient_2, mock_ingredient_1]

    def test_get_price(self):
        burger = Burger()
        mock_bun = Mock()
        mock_ingredient = Mock()
        mock_bun.get_price.return_value = TestText.bun_price
        mock_ingredient.get_price.return_value = TestText.ingredient_price
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)

        assert burger.get_price() == (mock_bun.get_price()*2 + mock_ingredient.get_price())

    def test_get_receipt(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = TestText.bun_name
        mock_bun.get_price.return_value = TestText.bun_price
        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_ingredient.get_name.return_value = TestText.ingredient_name
        mock_ingredient.get_price.return_value = TestText.ingredient_price
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        expected_result = ('(==== Краторная булка N-200i ====)\n''= sauce Соус Spicy-X =\n'
                           '(==== Краторная булка N-200i ====)\n''\n''Price: 2600')

        assert burger.get_receipt() == expected_result




