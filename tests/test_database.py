from data import TestDataBase
from conftest import db
import pytest
import allure


class TestDB:
    @allure.title('Проверка метода available_buns, проверка получения списка доступных булок из базы')
    @allure.description('С помощью параметризации выполняется 3 теста: проверяется по очереди '
                        'имя и стоимость каждой булки')
    @pytest.mark.parametrize('index_bun, bun_name, bun_price', TestDataBase.test_data_base_buns)
    def test_available_buns_db_success(self, db, index_bun, bun_name, bun_price):
        data_buns = db.available_buns()
        assert data_buns[index_bun].get_name() == bun_name and data_buns[index_bun].get_price() == bun_price

    @allure.title('Проверка метода available_ingredients, проверка получения списка доступных ингредиентов из базы')
    @allure.description('С помощью параметризации выполняется 6 тестов: проверяется по очереди '
                        'имя, тип и стоимость каждого ингредиента')
    @pytest.mark.parametrize('index_i, type_ingredient, name_ingredient, price_ingredient',
                             TestDataBase.test_data_base_ingredients)
    def test_available_ingredients_db_success(self, db, index_i, type_ingredient, name_ingredient, price_ingredient):
        data_ingredients = db.available_ingredients()
        assert (data_ingredients[index_i].get_name() == name_ingredient and
                data_ingredients[index_i].get_type() == type_ingredient and
                data_ingredients[index_i].get_price() == price_ingredient)