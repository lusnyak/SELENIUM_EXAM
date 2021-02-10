from selenium.common.exceptions import NoSuchElementException
from locators.locators import ContactUsLocators
import re

class ContactsPage:
    def __init__(self, driver):
        self.driver = driver
        self.name_input_xpath = ContactUsLocators.name_input_xpath
        self.email_input_xpath = ContactUsLocators.email_input_xpath
        self.phone_input_xpath = ContactUsLocators.telephone_input_xpath
        self.country_input_xpath = ContactUsLocators.country_input_xpath
        self.company_input_xpath = ContactUsLocators.company_input_xpath
        self.message_input_xpath = ContactUsLocators.message_input_xpath
        self.submit_btn_xpath = ContactUsLocators.submit_btn_xpath
        self.name_input_error_xpath = ContactUsLocators.name_input_error_xpath
        self.email_input_error_xpath = ContactUsLocators.email_input_error_xpath
        self.phone_input_error_xpath = ContactUsLocators.phone_input_error_xpath
        self.feedback_success_popup_xpath = ContactUsLocators.feedback_success_popup_xpath
        self.clear_btn_xpath = ContactUsLocators.clear_btn_xpath

    # name field methods
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

    # email field methods
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

    # phone field methods
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

    # country field methods
    def enter_country(self, country):
        country_input = self.driver.find_element_by_xpath(self.country_input_xpath)
        country_input.clear()
        country_input.send_keys(country)

    # country field methods
    def enter_company(self, company):
        company_input = self.driver.find_element_by_xpath(self.company_input_xpath)
        company_input.clear()
        company_input.send_keys(company)

    # country field methods
    def enter_message(self, message):
        message_input = self.driver.find_element_by_xpath(self.message_input_xpath)
        message_input.clear()
        message_input.send_keys(message)

    # buttons click methods
    def click_submit(self):
        self.driver.find_element_by_xpath(self.submit_btn_xpath).click()
    
    def click_clear(self):
        self.driver.find_element_by_xpath(self.clear_btn_xpath).click()

    # common methods
    def get_element_by_xpath(self, xpath):
        try:
            return self.driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return None
    
    def is_all_inputs_empty(self):
        name = self.driver.find_element_by_xpath(self.name_input_xpath).get_attribute('value')
        email = self.driver.find_element_by_xpath(self.email_input_xpath).get_attribute('value')
        phone = self.driver.find_element_by_xpath(self.phone_input_xpath).get_attribute('value')
        country = self.driver.find_element_by_xpath(self.country_input_xpath).get_attribute('value')
        company = self.driver.find_element_by_xpath(self.company_input_xpath).get_attribute('value')
        message = self.driver.find_element_by_xpath(self.message_input_xpath).get_attribute('value')

        return name == "" and email == "" and phone == "" and country == "" and company == "" and message == ""