# Задание 1. Создайте программу на Python или Java, которая принимает два списка чисел
# и выполняет следующие действия:
# a. Рассчитывает среднее значение каждого списка.
# b. Сравнивает эти средние значения и выводит соответствующее сообщение:
# - ""Первый список имеет большее среднее значение"", если среднее значение первого списка больше.
# - ""Второй список имеет большее среднее значение"", если среднее значение второго списка больше.
# - ""Средние значения равны"", если средние значения списков равны.

import pytest
from CompareAverage import СompareAverage


def test_average_list():
    list1 = [3, 14, 4, 9, 23, 7, 2, 18, 5, 10, 13, 16, 19]  # 11.0
    list2 = [12, 3, 8, 9, 22, 7, 5, 11, 15, 1, 6, 14, 4]    # 9.0
    assert СompareAverage.get_average_list(list1) == 11.0
    assert СompareAverage.get_average_list(list2) == 9.0


def test_comparison_average_lists():
    list1 = [3, 14, 4, 9, 23, 7, 2, 18, 5, 10, 13, 16, 19]  # 11.0
    list2 = [12, 3, 8, 9, 22, 7, 5, 11, 15, 1, 6, 14, 4]    # 9.0
    list3 = [12, 13, 8, 9, 22, 7, 5, 30, 15, 1, 6, 24, 4]    # 12.0
    list4 = [12, 11, 8, 9, 20, 7, 5, 24, 14, 1, 6, 22, 4]    # 11.0
    
    assert (СompareAverage.comparison_average_lists(list1, list2) 
            == "Первый список имеет большее среднее значение")
    assert СompareAverage.comparison_average_lists(list1, list3) == "Второй список имеет большее среднее значение"
    assert СompareAverage.comparison_average_lists(list1, list4) == "Средние значения равны"

# не работает в VSCode, только для PyCharm
# if __name__ == '__main__':
#     pytest.main(["-vv"])

# Необходимо запускать через терминал
# python -m pytest ./Homework_6/test_homework.py -vv
# =========================================================================== test session starts ===========================================================================
# platform win32 -- Python 3.10.11, pytest-7.4.2, pluggy-1.3.0 -- G:\GeekBrains\33. Unit-тесты\Homeworks\.venv\Scripts\python.exe
# cachedir: .pytest_cache
# rootdir: G:\GeekBrains\33. Unit-тесты\Homeworks
# collected 2 items                                                                                                                                                           
# Homework_6/test_homework.py::test_average_list PASSED                                                                                                                [ 50%] 
# Homework_6/test_homework.py::test_comparison_average_lists PASSED                                                                                                    [100%] 
# ============================================================================ 2 passed in 0.02s ============================================================================

# Необходимо запускать через терминал
# $ pylint ./Homework_6/test_homework.py
# ************* Module test_homework
# Homework_6\test_homework.py:25:0: C0303: Trailing whitespace (trailing-whitespace)
# Homework_6\test_homework.py:26:65: C0303: Trailing whitespace (trailing-whitespace)
# Homework_6\test_homework.py:28:0: C0301: Line too long (114/100) (line-too-long)
# Homework_6\test_homework.py:1:0: C0114: Missing module docstring (missing-module-docstring)
# Homework_6\test_homework.py:10:0: E0401: Unable to import 'Homework_6.CompareAverage' (import-error)
# Homework_6\test_homework.py:10:0: C2403: Module name "СompareAverage" contains a non-ASCII character, use an ASCII-only alias for import. (non-ascii-module-import)
# Homework_6\test_homework.py:13:0: C0116: Missing function or method docstring (missing-function-docstring)
# Homework_6\test_homework.py:20:0: C0116: Missing function or method docstring (missing-function-docstring)
# Homework_6\test_homework.py:20:0: E0102: function already defined line 13 (function-redefined)
# ------------------------------------------------------------------
# Your code has been rated at 0.00/10 (previous run: 0.00/10, +0.00)

# Необходимо запускать через терминал
# coverage run -m pytest
# ============================================= test session starts ==============================================
# platform win32 -- Python 3.10.11, pytest-7.4.2, pluggy-1.3.0
# rootdir: G:\GeekBrains\33. Unit-тесты\Homeworks
# collected 2 items
# Homework_6\test_homework.py ..                                                                            [100%] 
# ============================================== 2 passed in 0.13s ===============================================  

# coverage report -m
# Name                           Stmts   Miss  Cover   Missing
# ------------------------------------------------------------
# Homework_6\CompareAverage.py      14      0   100%
# Homework_6\test_homework.py       15      0   100%
# ------------------------------------------------------------
# TOTAL                             29      0   100%
