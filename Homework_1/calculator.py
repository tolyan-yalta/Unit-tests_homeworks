class Calculator():
    """Класс калькулятор"""

    @staticmethod
    def calculation(first_operand: int, second_operand: int, operator: str):
        result: float
        match operator:
            case "+":
                result = first_operand + second_operand
            case "-":
                result = first_operand - second_operand
            case "*":
                result = first_operand * second_operand
            case "/":
                if second_operand != 0:
                    result = first_operand / second_operand
                else:
                    raise ZeroDivisionError("Division by zero is not possible")
            case _:
                raise ValueError(f"Unexpected value operator: {operator}")
        return result



if __name__ == '__main__':
    res_1 = Calculator.calculation(2, 6, '+')
    print(res_1)
    res_2 = Calculator.calculation(2, 2, '-')
    print(res_2)
    res_3 = Calculator.calculation(2, 7, '*')
    print(res_3)
    res_4 = Calculator.calculation(100, 50, '/')
    print(res_4)
    
