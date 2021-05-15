from selenium import webdriver
import pytest
from faker import Faker
import time

url = 'http://127.0.0.1:8000/accounts/signup/'
url_success = 'http://127.0.0.1:8000/accounts/activate_account/'
faker = Faker()
username_selector = '#id_username'
email_selector = '#id_email'
first_name_selector = '#id_first_name'
last_name_selector = '#id_last_name'
password_selector = '#id_password'
repeat_password_selector = '#id_repeat_password'
submit_selector = '[value="Заристироваться"]'
busy_username1 = faker.name()

@pytest.fixture(scope='session')
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


def test_just_registrate(browser):
    email = faker.email()
    name = faker.name()
    password = "123456"
    browser.get(url)
    browser.find_element_by_css_selector(username_selector).send_keys(busy_username1)
    browser.find_element_by_css_selector(email_selector).send_keys(email)
    browser.find_element_by_css_selector(first_name_selector).send_keys(name)
    browser.find_element_by_css_selector(last_name_selector).send_keys(name)
    browser.find_element_by_css_selector(password_selector).send_keys(password)
    browser.find_element_by_css_selector(repeat_password_selector).send_keys(password)
    button = browser.find_element_by_css_selector(submit_selector)
    button.click()
    time.sleep(1)
    assert browser.current_url == url_success


def test_not_register_with_different_passwords(browser):
    username = faker.name()
    email = faker.email()
    name = faker.name()
    password = "123456"
    browser.get(url)
    browser.find_element_by_css_selector(username_selector).send_keys(username)
    browser.find_element_by_css_selector(email_selector).send_keys(email)
    browser.find_element_by_css_selector(first_name_selector).send_keys(name)
    browser.find_element_by_css_selector(last_name_selector).send_keys(name)
    browser.find_element_by_css_selector(password_selector).send_keys(password)
    browser.find_element_by_css_selector(repeat_password_selector).send_keys(password + "2")
    button = browser.find_element_by_css_selector(submit_selector)
    button.click()
    time.sleep(1)
    assert browser.current_url == url

def test_not_register_without_requered_fields(browser):
    button = browser.find_element_by_css_selector(submit_selector)
    button.click()
    time.sleep(1)
    assert browser.current_url == url

def test_not_register_with_non_unique_username(browser):
    email = faker.email()
    name = faker.name()
    password = "123456"
    browser.get(url)
    browser.find_element_by_css_selector(username_selector).send_keys(busy_username1)
    browser.find_element_by_css_selector(email_selector).send_keys(email)
    browser.find_element_by_css_selector(first_name_selector).send_keys(name)
    browser.find_element_by_css_selector(last_name_selector).send_keys(name)
    browser.find_element_by_css_selector(password_selector).send_keys(password)
    browser.find_element_by_css_selector(repeat_password_selector).send_keys(password)
    button = browser.find_element_by_css_selector(submit_selector)
    button.click()
    time.sleep(1)
    assert browser.current_url == url