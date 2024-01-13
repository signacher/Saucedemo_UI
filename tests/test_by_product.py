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


@pytest.mark.run(order=2)
@allure.tag('buy')
@allure.label('owner', 'Telnov')
@allure.epic('UI')
@allure.feature('Покупки')
@allure.story('Покупка товара "Sauce Labs Backpack"')
def test_buy_product1(set_up, set_group):
    with allure.step('Открываем браузер'):
        driver = setup_driver()

    with allure.step('Авторизуемся под пользователем "standart user"'):
        login = LoginPage(driver)
        login.authorization_standart_user()

    with allure.step('Добавляем в корзину товар "Sauce Labs Backpack"'):
        mp = MainPage(driver)
        mp.select_product1()

    cp = CartPage(driver)
    cp.product_confirmation()

    cip = Client_infomation_page(driver)
    cip.input_information()

    p = Payment_page(driver)
    p.payment()

    f = Finish_page(driver)
    f.finish()

    print('Finish test 1')
    driver.quit()

@pytest.mark.run(order=1)
@allure.tag('buy')
@allure.label('owner', 'Telnov')
@allure.epic('UI')
@allure.feature('Покупки')
@allure.story('Покупка товара "2"')
def test_buy_product2(set_up, set_group):
    driver = setup_driver()
    print('\nStart test 2')

    login = LoginPage(driver)
    login.authorization_standart_user()

    mp = MainPage(driver)
    mp.select_product2()

    cp = CartPage(driver)
    cp.product_confirmation()

    cip = Client_infomation_page(driver)
    cip.input_information()

    p = Payment_page(driver)
    p.payment()

    f = Finish_page(driver)
    f.finish()

    print('Finish test 2')
    time.sleep(2)
    driver.quit()


@allure.tag('menu')
@allure.label('owner', 'Telnov')
@allure.epic('UI')
@allure.feature('Меню')
@allure.story('Проверка пункта меню About')
def test_link_about(set_up):
    driver = setup_driver()

    print('\nStart test')

    login = LoginPage(driver)
    login.authorization_standart_user()

    mp = MainPage(driver)
    mp.select_menu_about()

    print('Finish test')
    driver.quit()


