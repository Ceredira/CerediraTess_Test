import pytest
from selenium import webdriver
import sys
from selenium.webdriver.common.by import By
from time import sleep


def test_lambdatest_todo_app():
    chrome_driver = webdriver.Chrome()

    chrome_driver.get('http://192.168.21.128:7801/login')
    chrome_driver.maximize_window()

    title = "Вход в систему"
    assert title == chrome_driver.title

    username = "admin"
    username_text_field = chrome_driver.find_element(By.ID, "username")
    username_text_field.send_keys(username)

    sleep(1)

    password = "admin"
    password_text_field = chrome_driver.find_element(By.ID, "password")
    password_text_field.send_keys(password)

    sleep(1)

    chrome_driver.find_element(By.ID, "submit").click()

    sleep(5)

    chrome_driver.close()
