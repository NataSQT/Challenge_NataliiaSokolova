import os
import time
import unittest
from selenium import webdriver
from pages.base_page import BasePage
from pages.add_player import AddPlayer
from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from selenium.webdriver.chrome.service import Service


class TestAddPlayerPage(unittest.TestCase):
    driver = None

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_add_player_on_dashboard(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.type_in_email('user07@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_sign_in_button()
        time.sleep(2)
        dashboard_page = Dashboard(self.driver)
        dashboard_page.click_on_add_player()
        add_player = AddPlayer(self.driver)
        add_player.type_in_email("j.kowalski@gmail.com")
        add_player.type_in_name("Jan")
        add_player.type_in_surname("Kowalski")
        add_player.type_in_phone("+48222222111")
        add_player.type_in_weight("86")
        add_player.type_in_height("186")
        add_player.type_in_age("08/11/1981")
        add_player.type_in_main_position("stricker")
        add_player.select_leg("right")
        add_player.click_on_the_submit_button()
        time.sleep(4)

    @classmethod
    def tearDown(self):
        self.driver.quit()


