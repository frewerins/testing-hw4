from selenium import webdriver
import pytest
from faker import Faker
import time

username_selector = '#id_username'
email_selector = '#id_email'
first_name_selector = '#id_first_name'
last_name_selector = '#id_last_name'
password_selector = '#id_password'
repeat_password_selector = '#id_repeat_password'
submit_selector = '[value="Заристироваться"]'

url = 'http://127.0.0.1:8000/accounts/password_reset/'
url_success = 'http://127.0.0.1:8000/accounts/password_reset/done/'
url_reg = 'http://127.0.0.1:8000/accounts/signup/'
faker = Faker()
old_password_selector = '#id_old_password'
new_password_selector = '#new_password'
submit_reset_selector = '.btn-primary'
busy_email = faker.email()
old_password = "123456"

@pytest.fixture(scope='session')
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


def test_for_registrate_user(browser):
    username = faker.name()
    name = faker.name()
    password = "123456"
    browser.get(url_reg)
    browser.find_element_by_css_selector(username_selector).send_keys(username)
    browser.find_element_by_css_selector(email_selector).send_keys(busy_email)
    browser.find_element_by_css_selector(first_name_selector).send_keys(name)
    browser.find_element_by_css_selector(last_name_selector).send_keys(name)
    browser.find_element_by_css_selector(password_selector).send_keys(password)
    browser.find_element_by_css_selector(repeat_password_selector).send_keys(password)
    button = browser.find_element_by_css_selector(submit_selector)
    button.click()


def test_just_reset(browser):
    browser.get(url)
    browser.find_element_by_css_selector(email_selector).send_keys(busy_email)
    button = browser.find_element_by_css_selector(submit_reset_selector)
    button.click()
    time.sleep(2)
    assert browser.current_url == url_success
    browser.find_element_by_css_selector(submit_reset_selector).click()
    time.sleep(2)
    assert browser.current_url == "http://127.0.0.1:8000/accounts/login/"

def test_email_not_exists(browser):
    browser.get(url)
    browser.find_element_by_css_selector(email_selector).send_keys(faker.email())
    button = browser.find_element_by_css_selector(submit_reset_selector)
    button.click()
    time.sleep(2)
    assert browser.current_url == url

def test_not_email(browser):
    browser.get(url)
    browser.find_element_by_css_selector(email_selector).send_keys(faker.name())
    button = browser.find_element_by_css_selector(submit_reset_selector)
    button.click()
    time.sleep(2)
    assert browser.current_url == url