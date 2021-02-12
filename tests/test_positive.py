import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import pytest
import allure
from pages.contacts import ContactsPage
from pages.base_page import Base


@pytest.mark.usefixtures('set_up')
class TestPositiveContacts(Base):

    @allure.title("Test name positive validation")
    @allure.description("Name can contains first name and last name, or only first name")
    @pytest.mark.parametrize("name",["Lusine", "Lus 3108", "Lusine Khacha" ])
    def test_is_name_value_correct(self, name):
        driver = self.driver
        contact = ContactsPage(driver)
        contact.enter_name(name)
        contact.click_submit() 
        assert contact.is_name_input_value_correct(), 'Name cannot be empty, contain only digits or a space'

    @allure.title("Test email format validation")
    @pytest.mark.parametrize("email",["lusine@example.com", "lusine@test.example.com", "lus.khach@exam.test"])
    def test_is_email_value_correct(self, email):
        driver = self.driver
        contact = ContactsPage(driver)
        contact.enter_email(email)
        contact.click_submit() 
        assert contact.is_email_input_value_correct(), f'{email} email address is incorrect'

    @allure.title("Test phone format positive validation")
    @allure.description("Phone  can started + symbol, contains digits (0-9)")
    @pytest.mark.parametrize("phone",["+0987654", "09876543", "98"])
    def test_is_phone_value_correct(self, phone):
        driver = self.driver
        contact = ContactsPage(driver)
        contact.enter_phone(phone)
        contact.click_submit() 
        assert contact.is_phone_input_value_correct(), f'{phone} phone number is incorrect'
    
    @allure.title("Test feedback successfuly send positive validation")
    @allure.description("After success submit should be show green popup")
    @pytest.mark.feedback_popup_show
    @pytest.mark.parametrize("name, email, phone",[("Lus","lusine@example.com", "0987654321")]) #, ("Lus Khach","lus.ine@exa.mple.co", "+987654321")
    def test_is_feedback_send_popup_show(self, name, email, phone):
        driver = self.driver
        contact = ContactsPage(driver)
        contact.enter_name(name)
        contact.enter_email(email)
        contact.enter_phone(phone)
        contact.click_submit()
        el = contact.get_element_by_xpath(contact.feedback_success_popup_xpath)
        assert el is not None, 'Feedback green popup not show'


    @allure.title("Test field crear functionality")
    @allure.description("By click clear button all entered inputs should be cleared")
    @pytest.mark.clear_inputs
    @pytest.mark.parametrize("name, email, phone, country, company, message", [("Lus","lusine@example.com", "0987654321", "Armenia", "BDG", "My test")])
    def test_is_all_inputs_clear(self, name, email, phone, country, company, message):
        driver = self.driver
        contact = ContactsPage(driver)
        contact.enter_name(name)
        contact.enter_email(email)
        contact.enter_phone(phone)
        contact.enter_country(country)
        contact.enter_company(company)
        contact.enter_message(message)
        contact.click_clear()
        assert contact.is_all_inputs_empty(), 'Not all fields empty'