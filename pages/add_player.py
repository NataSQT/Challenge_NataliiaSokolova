from pages.base_page import BasePage


class AddPlayer(BasePage):
    player_email_field_xpath = "//input[@name='email']"
    player_name_field_xpath = "//input[@name='name']"
    player_surname_field_xpath = "//input[@name='surname']"
    player_phone_field_xpath = "//input[@name='phone']"
    player_weight_field_xpath = "//input[@name='weight']"
    player_height_field_xpath = "//input[@name='height']"
    player_age_field_xpath = "//input[@name='age']"
    leg_dropdown_xpath = "//*[@id='mui-component-select-leg']"
    right_leg_xpath = "//li[@data-value='right']"
    left_leg_xpath = "//li[@data-value='left']"
    main_position_field_xpath = "//input[@name='mainPosition']"
    submit_button_xpath = "//button[@type='submit']/span[1]"
    edit_player_header_xpath = "//span[contains(@class, 'MuiTypography-h5')]"

    def type_in_email(self, email):
        self.field_send_keys(self.player_email_field_xpath, email)

    def type_in_name(self, name):
        self.field_send_keys(self.player_name_field_xpath, name)

    def type_in_surname(self, surname):
        self.field_send_keys(self.player_surname_field_xpath, surname)

    def type_in_phone(self, phone):
        self.field_send_keys(self.player_phone_field_xpath, phone)

    def type_in_weight(self, weight):
        self.field_send_keys(self.player_weight_field_xpath, weight)

    def type_in_height(self, height):
        self.field_send_keys(self.player_height_field_xpath, height)

    def type_in_age(self, age):
        self.field_send_keys(self.player_age_field_xpath, age)

    def select_leg(self, leg):
        self.click_on_the_element(self.leg_dropdown_xpath)
        if leg == "right":
            self.click_on_the_element(self.right_leg_xpath)
        else:
            self.click_on_the_element(self.left_leg_xpath)

    def type_in_main_position(self, position):
        self.field_send_keys(self.main_position_field_xpath, position)

    def click_on_the_submit_button(self):
        self.click_on_the_element(self.submit_button_xpath)

