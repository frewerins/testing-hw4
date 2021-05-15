# изначально создаем тестового пользователя, у меня это a.d.knyazeva / 11223344
from selenium import webdriver
import pytest
from faker import Faker
import time

username = 'a.d.knyazeva'
password = '11223344'
username_selector = '#id_username'
password_selector = '#id_password'
submit_selector = '[value="Log in"]'

@pytest.fixture(scope='session')
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


def test_not_login_user(browser):
    history_orders = 'http://127.0.0.1:8000/history_orders'
    browser.get(history_orders)
    time.sleep(2)
    assert browser.current_url == 'http://127.0.0.1:8000/'
    history_orders = 'http://127.0.0.1:8000/user_cart_page'
    browser.get(history_orders)
    time.sleep(2)
    assert browser.current_url == 'http://127.0.0.1:8000/'

def test_login_user(browser):
    browser.get('http://127.0.0.1:8000/admin')
    browser.find_element_by_css_selector(username_selector).send_keys(username)
    browser.find_element_by_css_selector(password_selector).send_keys(password)
    browser.find_element_by_css_selector(submit_selector).click()
    time.sleep(4)
    browser.get('http://127.0.0.1:8000/accounts/signup/')
    time.sleep(2)
    assert browser.current_url == 'http://127.0.0.1:8000/'
    browser.get('http://127.0.0.1:8000/accounts/login/')
    time.sleep(2)
    assert browser.current_url == 'http://127.0.0.1:8000/'
    history_orders = 'http://127.0.0.1:8000/history_orders'
    browser.get(history_orders)
    time.sleep(2)
    assert browser.current_url == 'http://127.0.0.1:8000/history_orders'
