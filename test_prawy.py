import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_pierwszy():
    driver = webdriver.Chrome()
    driver.get("https://artoftesting.com/samplesiteforselenium")

    action = webdriver.ActionChains(driver)
    search_box = driver.find_element(By.ID, "fname")
    action.move_to_element(search_box).perform()
    search_box.send_keys("ArtOfTesting")
    action.context_click(search_box).perform()
    time.sleep(3)
    driver.quit()


def test_drugi():
    driver = webdriver.Chrome()
    driver.get("https://demo.guru99.com/test/simple_context_menu.html")

    action = webdriver.ActionChains(driver)
    link = driver.find_element(By.CSS_SELECTOR, ".context-menu-one")
    action.move_to_element(link).perform()
    action.context_click(link).perform()
    element = driver.find_element(By.CSS_SELECTOR, ".context-menu-icon-copy")
    time.sleep(1)
    element.click()
    driver.switch_to.alert.accept()
    time.sleep(2)

    driver.quit()
