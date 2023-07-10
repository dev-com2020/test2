import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dragdrop():
    driver = webdriver.Chrome()
    driver.get("https://jqueryui.com/droppable/")
    driver.switch_to.frame(0)
    src = driver.find_element(By.ID, "draggable")
    dst = driver.find_element(By.ID, "droppable")
    action = webdriver.ActionChains(driver)
    action.drag_and_drop(src, dst).perform()
    time.sleep(2)
    driver.quit()


def test_exe_scr():
    driver = webdriver.Chrome()
    driver.get("https://www.tutorialspoint.com/about/about_careers.htm")
    driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
    time.sleep(2)
    driver.quit()


def test_color():
    print(Color.from_string("red").rgba)
    print(Color.from_string("rgba(255, 0, 0, 1)").hex)
    print(Color.from_string("#00fe37").rgba)


def test_windows():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/windows")
    s = driver.find_element(By.LINK_TEXT, "Click Here")
    s.click()
    m = driver.current_window_handle

    for h in driver.window_handles:
        if h != m:
            n = h

    driver.switch_to.window(n)
    print('Nowa okno: ', driver.title)
    driver.switch_to.window(m)
    print('Stare okno: ', driver.title)

    driver.quit()
