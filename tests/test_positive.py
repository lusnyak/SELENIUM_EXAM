import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from time import sleep
import pytest
from pages.contacts import ContactsPage
from pages.base_page import Base

@pytest.mark.usefixtures('set_up')
class TestPositiveContacts(Base):

    @pytest.mark.parametrize("name",["Lusine", "Lus 3108", "Lusine Khacha" ])
    def test_is_name_value_correct(self, name):
        driver = self.driver
        contact = ContactsPage(driver)
        contact.enter_name(name)
        contact.click_submit() 
        assert contact.is_name_input_value_correct(), 'Name cannot be empty, contain only digits or a space'

    @pytest.mark.parametrize("email",["lusine@example.com", "lusine@test.example.com", "lus.khach@exam.test"])
    def test_is_email_value_correct(self, email):
        driver = self.driver
        contact = ContactsPage(driver)
        contact.enter_email(email)
        contact.click_submit() 
        assert contact.is_email_input_value_correct(), f'{email} email address is incorrect'

    @pytest.mark.parametrize("phone",["+0987654", "09876543", "98"])
    def test_is_phone_value_correct(self, phone):
        driver = self.driver
        contact = ContactsPage(driver)
        contact.enter_phone(phone)
        contact.click_submit() 
        assert contact.is_phone_input_value_correct(), f'{phone} phone number is incorrect'
    
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