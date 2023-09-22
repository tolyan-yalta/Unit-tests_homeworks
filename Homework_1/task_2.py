import unittest
from product import Product
from shop import Shop


class TestShop(unittest.TestCase):

    def setUp(self):
        """Метод вызывается перед каждым вызовом теста (создается список продуктов)."""
        self.list_products = [Product("apple", 5), 
                        Product("tomato", 3),
                        Product("potato", 7),
                        Product("orange", 2), 
                        Product("cherry", 8)]
        self.shop = Shop()
        for item in self.list_products:
            self.shop.add_products(item)

    def tearDown(self) -> None:
        """Метод вызывается после каждого вызова теста (очищается список продуктов)."""
        self.shop.__del__()

    def test_shop_not_empty(self):
        """Метод для проверки, что магазин хранит верный список продуктов (количество продуктов)"""
        self.assertEqual(len(self.shop.get_products()), 5)


    def test_get_most_expensive_product(self):
        """Метод для проверки, что метод get_most_expensive_product() возвращает верный самый дорогой продукт."""
        self.assertEqual(self.shop.get_most_expensive_product().get_cost(), 8)
        pass

    def test_sort_products_by_price(self):
        """Метод для проверки, что метод sort_products_by_price() 
            возвращает верно отсортированный по цене список продуктов."""
        # вручную отсортированный список продуктов
        sample_list = [self.list_products[3], 
                        self.list_products[1], 
                        self.list_products[0], 
                        self.list_products[2], 
                        self.list_products[4],]
        self.assertListEqual(self.shop.sort_products_by_price(), sample_list)

if __name__ == '__main__':
    unittest.main(verbosity=2)
