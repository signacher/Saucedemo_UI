import time
from termcolor import colored, cprint
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture()
def set_up():
    print(colored("\nSTART TEST",'yellow',))
    yield
    print(colored('\nFINISH TEST','yellow'))

@pytest.fixture(scope='module')
def set_group():
    print(colored("\nENTER SYSTEM", 'green'))
    yield
    print(colored('\nEXIT SYSTEM', 'green'))
