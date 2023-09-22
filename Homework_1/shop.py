from product import Product


class Shop():
    """Класс Магазин"""
    __products = []

    def get_products(self):
        return self.__products
    
    def add_products(self, product: Product):
        self.__products.append(product)

    def sort_products_by_price(self):
        """Метод сортирующий список продуктов по стоимости."""
        sorted_list = sorted(self.__products, key=Product.get_cost)
        # self.__products.sort(key=Product.get_cost)
        return sorted_list
        # return self.__products
    
    def get_most_expensive_product(self):
        """Метод возвращающий самый дорогой продукт."""
        max_product = max(self.__products, key=Product.get_cost)
        return max_product
    
    def __del__(self):
        self.__products.clear()
        # self.remove()
    

if __name__ == '__main__':
        shop = Shop()
        list_products = [("apple", 5), ("tomato", 3), ("potato", 7), ("orange", 2), ("cherry", 8)]
        for title, cost in list_products:
            temp = Product(title,cost)
            shop.set_products(temp)

        # print(f"Max cost: {shop.get_most_expensive_product()}")

        # for i in shop.get_products():
        #     print(i)

        res_sorted = shop.sort_products_by_price()
        for i in res_sorted:
            print(i)
