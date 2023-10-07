# Задание №5
# Нужно написать сквозной тест с использованием Selenium, который авторизует пользователя на
# сайте https://www.saucedemo.com/.
# Данные для входа - логин: "standard_user", пароль: "secret_sauce".
# Проверить, что авторизация прошла успешно и отображаются товары.
# Вам необходимо использовать WebDriver для открытия страницы и методы sendKeys() для ввода
# данных в поля формы, и submit() для отправки формы. После этого, проверьте, что на странице
# отображаются продукты (productsLabel.getText() = "Products").

# pip install selenium
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
# pip install webdriver-manager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
# pip install pytest
import pytest

def test_saucedemo():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    driver.get("https://www.saucedemo.com/")
    assert "Swag Labs" in driver.title

    elem_name = driver.find_element(By.NAME, "user-name")
    elem_name.send_keys("standard_user")
    elem_password = driver.find_element(By.NAME, "password")
    elem_password.send_keys("secret_sauce")
    button = driver.find_element(By.NAME, "login-button")
    button.click()

    assert driver.find_element(By.CLASS_NAME, "title").text == "Products"

    driver.quit()


# запуск в PyCharm
if __name__ == '__main__':
    pytest.main(["-vv"])

# запуск в VSCode через командную строку
# python -m pytest selenium_5.py -vv
