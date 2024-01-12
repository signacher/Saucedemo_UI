
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilites.logger import Logger
import allure

class LoginPage(Base):
    url = 'https://www.saucedemo.com/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators

    user_name = "//input[@data-test='username']"
    password = "//input[@data-test='password']"
    login_button = "//input[@type='submit']"
    main_word = "//span[@class='title']"

    #Getters

    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.main_word)))


    #Actions

    def input_user_name(self, user_name):
        with allure.step('Вводим логин'):
            self.get_user_name().send_keys(user_name)


    def input_password(self, password):
        with allure.step('Вводим пароль'):
            self.get_password().send_keys(password)


    def click_login_button(self):
        with allure.step('Нажимаем кнопку Login'):
            self.get_login_button().click()


    #Methods

    def authorization_standart_user(self):
            Logger.add_start_step(method="authorization")
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.input_user_name('standard_user')
            self.input_password('secret_sauce')
            self.click_login_button()
            self.assert_word(self.get_main_word(), 'Products')
            Logger.add_end_step(url=self.driver.current_url, method="authorization")


