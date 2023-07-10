from selenium import webdriver
from login_page import LoginPage

def test_login():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/")
    login = LoginPage(driver)
    login.enter_username("Admin")
    login.enter_password("admin123")
    login.click_login()
    driver.close()