class Product():
    """Класс Продукт"""

    def __init__(self, title: str, cost: int):
        self.__title = title
        self.__cost = cost

    def get_title(self):
        return self.__title
    
    def set_title(self, title: str):
        self.__title = title

    def get_cost(self):
        return self.__cost
    
    def set_cost(self, cost: int):
        self.__cost = cost

    def __str__(self) -> str:
        return f"Product: {self.__title}\tcost: {self.__cost}"
