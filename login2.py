from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    @property
    def username(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'username')))

    @property
    def password(self):
          return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'password')))

    @property
    def login_button(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[@type='submit']")))

    def login(self, username, password):
        self.username.send_keys(username)
        self.password.send_keys(password)
        self.login_button.click()