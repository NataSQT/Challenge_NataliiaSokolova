import os
import time
import unittest
from selenium import webdriver
from pages.base_page import BasePage
from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from selenium.webdriver.chrome.service import Service

class TestLoginPage(unittest.TestCase):
    driver = None
    def __init__(self, methodName: str = ...):
        super().__init__(methodName)

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts.futbolkolektyw.pl/en/')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)
        self.user_login = LoginPage(self.driver)
        self.dashboard_page = Dashboard(self.driver)
        self.base_page = BasePage(self.driver)

    def test_log_in_to_the_system(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.check_title_of_box()
        user_login.type_in_email('user07@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page()
        time.sleep(4)

    def test_empty_login(self):
        self.user_login.log_in('', 'Test-1234')
        time.sleep(4)

    def test_invalid_password_to_log_in(self):
        self.user_login.log_in('user07@getnada.com', 'Test-4444')
        time.sleep(4)

    def test_text_page_title(self):
        self.user_login.title_of_page()
        time.sleep(4)

    @classmethod
    def tearDown(self):
        self.driver.quit()


