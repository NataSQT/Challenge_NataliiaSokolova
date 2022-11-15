import time
from pages.base_page import BasePage


class Dashboard(BasePage):
    scouts_panel_heading_xpath = "//h6[text() = 'Scouts Panel']"
    main_page_xpath = "//*[text()='Main page']"
    main_page_button_xpath = "//ul[1]/div[1]"
    players_xpath = "//*[text()='Players']"
    players_button_xpath = "//ul[1]/div[2]"
    polski_xpath = "//*[text()='Polski']"
    polski_button_xpath = "//ul[2]/div[1]"
    sign_out_xpath = "//*[text()='Sign out']"
    sign_out_button_xpath = "//ul[2]/div[2]"
    players_count_field_xpath = "//main/div[2]/div[1]/div"
    players_count_xpath = "//div[2]/div[1]/div/div[1]"
    matches_count_field_xpath = "//main/div[2]/div[2]/div"
    matches_count_xpath = "//div[2]/div[2]/div/div[1]"
    reports_count_field_xpath = "//main/div[2]/div[3]/div"
    reports_count_xpath = "//div[2]/div[3]/div/div[1]"
    events_count_field_xpath = "//main/div[2]/div[4]/div"
    events_count_xpath = "//div[2]/div[4]/div/div[1]"
    logo_scouts_panel_xpath = "//*[contains(@title, 'Logo')]"
    dev_team_contact_hyperlink_xpath = "//a[contains(@href, 'client')]"
    add_player_button_xpath = "//*[text()='Add player']"
    shortcuts_block_xpath = "//main/div[3]/div[2]/div/div"
    activity_block_xpath = "//main/div[3]/div[3]/div/div"

    expected_title = "Scouts panel"
    dashboard_url = 'https://scouts-test.futbolkolektyw.pl/'

    def title_of_page(self):
        time.sleep(4)
        assert self.get_page_title(self.dashboard_url) == self.expected_title

    def click_on_add_player(self):
        self.click_on_the_element(self.add_player_button_xpath)

