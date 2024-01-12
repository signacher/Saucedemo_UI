from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from termcolor import colored
from base.base_class import Base
from utilites.logger import Logger
import allure

class MainPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #Locators

    select_product_1 = "//button[@id='add-to-cart-sauce-labs-backpack']"
    select_product_2 = "//button[@id='add-to-cart-sauce-labs-bike-light']"
    cart = "//div[@id='shopping_cart_container']"
    menu = "//button[@id='react-burger-menu-btn']"
    link_about = "//a[@id='about_sidebar_link']"
    name_product1 = "//div[@class='inventory_item_name ']"
    name_product2 = "//a[@id='item_0_title_link']"


    #Getters

    def get_name_product_1(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.name_product1)))

    def get_name_product_2(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.name_product2)))

    def get_name_product_3(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.name_product3)))


    def get_select_product_1(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.select_product_1)))

    def get_select_product_2(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.select_product_2)))

    def get_select_product_3(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.select_product_3)))

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.cart)))

    def get_menu(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.menu)))

    def get_link_about(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.link_about)))


    #Actions


    def text_select_product_1(self):
        product = self.get_name_product_1()
        name_product = product.text
        print(colored('ADD PRODUCT: ' + name_product, 'magenta'))

    def text_select_product_2(self):
        product = self.get_name_product_2()
        name_product = product.text
        print(colored('ADD PRODUCT: ' + name_product, 'magenta'))

    def text_select_product_3(self):
        product = self.get_name_product_3()
        name_product = product.text
        print(colored('ADD PRODUCT: ' + name_product, 'magenta'))

    def click_select_product_1(self):
        self.get_select_product_1().click()
        print("Click  Select_product_1")

    def click_select_product_2(self):
        self.get_select_product_2().click()
        print("Click  Select_product_2")

    def click_select_product_3(self):
        self.get_select_product_3().click()
        print("Click  Select_product_3")

    def click_cart(self):
        self.get_cart().click()
        print("Click  cart")

    def click_menu(self):
        self.get_menu().click()
        print("Click  menu")

    def click_link_about(self):
        self.get_link_about().click()
        print("Click  link about")


    #Methods

    def select_product1(self):
        Logger.add_start_step(method="select_product1")
        self.get_current_url()
        self.click_select_product_1()
        self.text_select_product_1()
        self.assert_url('https://www.saucedemo.com/inventory.html')
        self.click_cart()
        Logger.add_end_step(url=self.driver.current_url, method="select_product1")


    def select_product2(self):
        with allure.step('Select_product Sauce Labs Bike Light'):
            Logger.add_start_step(method="select_product2")
            self.get_current_url()
            self.text_select_product_2()
            self.click_select_product_2()
            self.assert_url('https://www.saucedemo.com/inventory.html')
            self.click_cart()
            Logger.add_end_step(url=self.driver.current_url, method="select_product2")


    def select_menu_about(self):
        with allure.step('Select menu About'):
            Logger.add_start_step(method="select_menu_about")
            self.get_current_url()
            self.click_menu()
            self.click_link_about()
            self.assert_url('https://saucelabs.com/')
            Logger.add_end_step(url=self.driver.current_url, method="select_menu_about")


