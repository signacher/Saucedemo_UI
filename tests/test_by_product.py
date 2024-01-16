import pytest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.common import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from pages.cart_page import CartPage
from pages.client_information_page import Client_infomation_page
from pages.finish_page import Finish_page
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.paymeint_page import Payment_page
import allure


def setup_driver():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument('--headless')
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=options)
    wait = WebDriverWait(driver, timeout=2, ignored_exceptions=(WebDriverException,))
    driver.maximize_window()
    return driver


@allure.tag('buy')
@allure.label('owner', 'Telnov')
@allure.epic('UI')
@allure.feature('Покупки')
@allure.story('Покупка товара "Sauce Labs Backpack"')
@pytest.mark.run(order=2)
@pytest.mark.buy
def test_buy_product1(set_up, set_group):
    with allure.step('Открываем браузер'):
        driver = setup_driver()

    with allure.step('Авторизуемся под пользователем "standart user"'):
        login = LoginPage(driver)
        login.authorization_standart_user()

    with allure.step('Добавляем в корзину товар "Sauce Labs Backpack"'):
        mp = MainPage(driver)
        mp.select_product1()
    with allure.step('Нажимаем Checkout'):
        cp = CartPage(driver)
        cp.product_confirmation()
    with allure.step('Заполняем информацию о заказчике'):
        cip = Client_infomation_page(driver)
        cip.input_information()
    with allure.step('Проверяем информацию о стоймости заказа'):
        p = Payment_page(driver)
        p.payment()
    with allure.step('Завершаем заказ'):
        f = Finish_page(driver)
        f.finish()
    driver.quit()


@allure.tag('buy')
@allure.label('owner', 'Telnov')
@allure.epic('UI')
@allure.feature('Покупки')
@allure.story('Покупка товара "Sauce Labs Bike Light"')
@pytest.mark.run(order=1)
@pytest.mark.buy
def test_buy_product2(set_up, set_group):
    with allure.step('Открываем браузер'):
        driver = setup_driver()
    with allure.step('Авторизуемся под пользователем "standart user"'):
        login = LoginPage(driver)
        login.authorization_standart_user()
    with allure.step('Добавляем товар Sauce Labs Bike Light в корзину'):
        mp = MainPage(driver)
        mp.select_product2()
    with allure.step('Нажимаем Checkout'):
        cp = CartPage(driver)
        cp.product_confirmation()
    with allure.step('Заполняем информацию о заказчике'):
        cip = Client_infomation_page(driver)
        cip.input_information()
    with allure.step('Проверяем информацию о стоймости заказа'):
        p = Payment_page(driver)
        p.payment()
    with allure.step('Завершаем заказ'):
        f = Finish_page(driver)
        f.finish()
    driver.quit()


@allure.tag('menu')
@allure.epic('UI')
@allure.feature('Меню')
@allure.story('Проверка пункта меню About')
@pytest.mark.menu
def test_link_about(set_up):
    with allure.step('Открываем браузер'):
        driver = setup_driver()
    with allure.step('Авторизуемся под пользователем "standart user"'):
        login = LoginPage(driver)
        login.authorization_standart_user()
    with allure.step('Проверяем переход в пункт меню About"'):
        mp = MainPage(driver)
        mp.select_menu_about()
    driver.quit()

@allure.epic('Others')
@allure.story('Падающий тест для красивого отчета')
def test_failed():
    with allure.step('Проверяем что 3 равно 2'):
        assert 3 == 2


@allure.epic('Others')
@allure.story('Пропущенный тест для красивого отчета')
@pytest.mark.skip
def test_failed():
    with allure.step('Проверяем что 2 равно 2'):
        assert 2 == 2
