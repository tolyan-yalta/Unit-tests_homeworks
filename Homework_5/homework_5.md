### Задание 1. 
*Представьте, что вы работаете над разработкой простого приложения для записной книжки, которое позволяет пользователям добавлять, редактировать и удалять контакты.   
Ваша задача - придумать как можно больше различных тестов (юнит-тесты, интеграционные тесты, сквозные тесты) для этого приложения. Напишите название каждого теста, его тип и краткое описание того, что этот тест проверяет.

1. testAddUset - юнит-тест, проверяет добавление пользователя в базу данных;
2. testEditUset - юнит-тест, проверяет редактирование пользователя в базе данных;
3. testDeleteUser - юнит-тест, проверяет удаление пользователя из базы данных;
4. testGetUser - юнит-тест, проверяет получение пользователя из базы данных 
5. testGetAllUsers - юнит-тест,  проверяет получение списка всех пользователей из базы данных 
6. testAddAndtEditUser - интеграционный тест, добавляет пользователя в базу и затем редактирует его
7. testAddAndDeleteUser - интеграционный тест, добавляет пользователя в базу и затем удаляет его 
8. testGetAllAndDeleteUsersr- интеграционный тест, получает список всех пользователе, а затем удаляет их всех
9. testFullActions - сквозной тест, тестирует всю цепочку действий, добавляет, редактирует и удаляет пользователя

### Задание 2. 
*Ниже список тестовых сценариев. Ваша задача - определить тип каждого теста (юнит-тест, интеграционный тест, сквозной тест) и объяснить, почему вы так решили.

Проверка того, что функция addContact корректно добавляет новый контакт в список контактов"".   
""Проверка того, что при добавлении контакта через пользовательский интерфейс, контакт корректно отображается в списке контактов"".   
""Проверка полного цикла работы с контактом: создание контакта, его редактирование и последующее удаление"".

Ответы:
1. Юнит-тест, так как проверяется работа одного модуля (добавление контакта).
2. Интеграционный тест, так как проверяется работа двух модулей, добавление контакта и вывод списка контактов.
3. Сквозной тест, так как проверка полного цикла работы это и есть по определению сквозной тест.

