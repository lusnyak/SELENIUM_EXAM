from selenium.common.exceptions import NoSuchElementException
from locators.locators import ContactUsLocators
import re

class ContactsPage:
    def __init__(self, driver):
        self.driver = driver
        self.name_input_xpath = ContactUsLocators.name_input_xpath
        self.email_input_xpath = ContactUsLocators.email_input_xpath
        self.phone_input_xpath = ContactUsLocators.telephone_input_xpath
        self.submit_btn_xpath = ContactUsLocators.submit_btn_xpath
        self.name_input_error_xpath = ContactUsLocators.name_input_error_xpath
        self.email_input_error_xpath = ContactUsLocators.email_input_error_xpath
        self.phone_input_error_xpath = ContactUsLocators.phone_input_error_xpath
        self.feedback_success_popup_xpath = ContactUsLocators.feedback_success_popup_xpath

    def enter_name(self, name):
        name_input = self.driver.find_element_by_xpath(self.name_input_xpath)
        name_input.clear()
        name_input.send_keys(name)
    
    def get_name_input_value(self):
        return self.driver.find_element_by_xpath(self.name_input_xpath).get_attribute('value')
    
    def is_name_input_value_correct(self):
        name_input = self.driver.find_element_by_xpath(self.name_input_xpath)
        val = name_input.get_attribute('value')
        regexName = r'[A-Za-z]{2,32}( [A-Za-z]{2,32})?'
        return re.search(regexName, val)

    def enter_email(self, email):
        email_input = self.driver.find_element_by_xpath(self.email_input_xpath)
        email_input.clear()
        email_input.send_keys(email)
    
    def get_email_input_value(self):
        return self.driver.find_element_by_xpath(self.email_input_xpath).get_attribute('value')

    def is_email_input_value_correct(self):
        email_input = self.driver.find_element_by_xpath(self.email_input_xpath)
        val = email_input.get_attribute('value')
        regexName = r'([A-Za-z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)'
        return re.search(regexName, val)

    def enter_phone(self, phone):
        phone_input = self.driver.find_element_by_xpath(self.phone_input_xpath)
        phone_input.clear()
        phone_input.send_keys(phone)

    def get_phone_input_value(self):
        return self.driver.find_element_by_xpath(self.phone_input_xpath).get_attribute('value')
    
    def is_phone_input_value_correct(self):
        phone_input = self.driver.find_element_by_xpath(self.phone_input_xpath)
        val = phone_input.get_attribute('value')
        regexName = r'(\+)?[0-9]{2,15}$'
        return re.search(regexName, val)

    def click_submit(self):
        self.driver.find_element_by_xpath(self.submit_btn_xpath).click()
    
    def click_clear(self):
        self.driver.find_element_by_xpath(self.submit_btn_xpath).click()

    def get_element_by_xpath(self, xpath):
        try:
            return self.driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return None