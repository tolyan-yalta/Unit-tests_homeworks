class Discount():

    @staticmethod
    def calculating_discount(purchase_amount: float, discount_amount: int):
        # purchase_amount - сумма покупки
        # discount_amount - размер скидки
        result: float
        if discount_amount < 0:
            raise ValueError("The discount amount cannot be negative!")
        elif discount_amount > 100:
            raise ValueError("The discount amount cannot be more than 100 %!")
        result = purchase_amount * (1 - discount_amount / 100)
        return result
    

if __name__ == '__main__':
    res_1 = Discount.calculating_discount(100, 5)
    print(res_1)
    # res_2 = Discount.calculating_discount(100, -5)
    # print(res_2)
    # res_3 = Discount.calculating_discount(100, 105)
    # print(res_3)
