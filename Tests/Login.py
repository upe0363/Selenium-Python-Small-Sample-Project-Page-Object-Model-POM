import time
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.loginPage import LoginPage
from pages.homePage import HomePage

class LoginTest(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver

        driver.get("https://www.saucedemo.com/")

        login = LoginPage(driver)
        login.enter_username("standard_user")
        login.enter_password("secret_sauce")
        login.click_login()

        homepage =HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")
