from data import TestText
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:
    def test_get_ingredient_type_sauce(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, TestText.ingredient_name, TestText.ingredient_price)
        assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE

    def test_get_ingredient_type_filling(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, TestText.ingredient_name, TestText.ingredient_price)
        assert ingredient.get_type() == INGREDIENT_TYPE_FILLING

    def test_get_ingredient_name(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, TestText.ingredient_name, TestText.ingredient_price)
        assert ingredient.get_name() == TestText.ingredient_name

    def test_get_ingredient_price(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, TestText.ingredient_name, TestText.ingredient_price)
        assert ingredient.get_price() == TestText.ingredient_price
