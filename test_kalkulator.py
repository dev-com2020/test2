import unittest
from appium import webdriver


class SimpleCalculatorTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # set up appium
        desired_caps = {}
        # desired_caps['platformName'] = 'Android'
        # desired_caps['platformVersion'] = '4.4.2'
        # desired_caps['deviceName'] = 'Android Emulator'
        # desired_caps['appPackage'] = 'com.android.calculator2'
        # desired_caps['appActivity'] = '.Calculator'
        # cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        desired_caps["app"] = "Microsoft.WindowsCalculator_8wekyb3d8bbwe!App"
        cls.driver = webdriver.Remote(
            command_executor='http://localhost:4723',
            desired_capabilities=desired_caps)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def getresults(self):
        displaytext = self.driver.find_element_by_accessibility_id("CalculatorResults").text
        displaytext = displaytext.strip("Wyświetlana wartość to ")
        displaytext = displaytext.rstrip(' ')
        displaytext = displaytext.lstrip(' ')
        return displaytext

    def test_initilize(self):
        # test initilize
        self.driver.find_element_by_name("Siedem").click()
        self.assertEqual(self.getresults(), "7")
        self.driver.find_element_by_name("Wyczyść").click()
        self.assertEqual(self.getresults(), "0")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleCalculatorTests)
    unittest.TextTestRunner(verbosity=2).run(suite)