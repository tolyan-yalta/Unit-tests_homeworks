## Домашние задания по курсу "Unit-тесты (семинары)"

### Добавлено д/з 1 (Homework_1)

### Добавлено д/з 2 (Homework_2)

### Добавлено д/з 3 (Homework_3)

### Добавлено д/з 4 (Homework_4)

### Добавлено д/з 5 (Homework_5)

### Добавлено д/з 6 (Homework_6)

#### Задание 1. 
Создайте программу на Python или Java, которая принимает два списка чисел и выполняет следующие действия:   
a. Рассчитывает среднее значение каждого списка.   
b. Сравнивает эти средние значения и выводит соответствующее сообщение:
- ""Первый список имеет большее среднее значение"", если среднее значение первого списка больше.
- ""Второй список имеет большее среднее значение"", если среднее значение второго списка больше.
- ""Средние значения равны"", если средние значения списков равны.

#### Важно:
* Приложение должно быть написано в соответствии с принципами объектно-ориентированного программирования.   
    > файл CompareAverage.py
* Используйте Pytest (для Python) или JUnit (для Java) для написания тестов, которые проверяют правильность работы программы. Тесты должны учитывать различные сценарии использования вашего приложения.
    > файл test_homework.py   
    > запуск теста через терминал (закоментированная строка в файле 36)   
    > python -m pytest ./Homework_6/test_homework.py -vv   
    > результат: строки 37-44   
* Используйте pylint (для Python) или Checkstyle (для Java) для проверки качества кода.
    > запуск линтера через терминал (закоментированная строка в файле 47)   
    > pylint ./Homework_6/test_homework.py   
    > результат: строки 48-59   
* Сгенерируйте отчет о покрытии кода тестами. Ваша цель - достичь минимум 90% покрытия.  
    > запуск оценки покрытия кода через терминал (закоментированная строка в файле 62)   
    > coverage run -m pytest   
    > результат: строки 63-68   
    > запуск для получения report через терминал (закоментированная строка в файле 70)   
    > coverage report -m   
    > результат: строки 71-76   

#### Достигнуто 100% покрытия
