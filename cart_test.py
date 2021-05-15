# изначально создаем тестового пользователя, у меня это a.d.knyazeva / 11223344
from selenium import webdriver
import pytest
from faker import Faker
import time
from selenium.webdriver.common.by import By

username = 'a.d.knyazeva'
password = '11223344'
username_selector = '#id_username'
password_selector = '#id_password'
submit_selector = '[value="Log in"]'


product_name_selector = "//div[@class='panel-heading']//a"
add_button_selector = "#add_to_cart"

@pytest.fixture(scope='session')
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()

def test_for_login_user(browser):
    browser.get('http://127.0.0.1:8000/admin')
    browser.find_element_by_css_selector(username_selector).send_keys(username)
    browser.find_element_by_css_selector(password_selector).send_keys(password)
    browser.find_element_by_css_selector(submit_selector).click()

def test_add_product(browser):
    browser.get('http://127.0.0.1:8000/')
    product_name = browser.find_elements(By.XPATH, product_name_selector)[0].text
    button = browser.find_elements_by_css_selector(add_button_selector)[0]
    button.click()
    time.sleep(2)
    browser.switch_to.alert.accept()
    browser.get('http://127.0.0.1:8000/user_cart_page')
    product_name_in_car = browser.find_elements(By.XPATH, "//p[@class='text-left']//a")[0].text
    assert product_name == product_name_in_car
