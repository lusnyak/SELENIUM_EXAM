import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import pytest
from pages.contacts import ContactsPage
from pages.base_page import Base

@pytest.mark.usefixtures('set_up')
class TestNegativeContacts(Base):

    @pytest.mark.name_error
    @pytest.mark.parametrize("name, email, phone",[("","lusine@example.com", "0987654321"), ("  ","lusine@example.com", "0987654321")])
    def test_name_error_elemenet_exists(self, name, email, phone):
        driver = self.driver
        contact = ContactsPage(driver)
        contact.enter_name(name)
        contact.enter_email(email)
        contact.enter_phone(phone)
        contact.click_submit() 
        el = contact.get_element_by_xpath(contact.name_input_error_xpath)
        assert el is not None, 'Name error element does not exist'
    
    @pytest.mark.email_error
    @pytest.mark.parametrize("name, email, phone",[("Lusine","", "0987654321"),("Luso","lusineexample.com", "0987654321")])
    def test_email_error_elemenet_exists(self, name, email, phone):
        driver = self.driver
        contact = ContactsPage(driver)
        contact.enter_name(name)
        contact.enter_email(email)
        contact.enter_phone(phone)
        contact.click_submit()
        el = contact.get_element_by_xpath(contact.email_input_error_xpath)
        assert el is not None, 'Email error element does not exist'

    @pytest.mark.parametrize("name, email, phone",[("Lusine","lusine@example.com", ""),("Lusine","lusine@example.com", "sdfghj")])
    def test_phone_error_elemenet_exists(self, name, email, phone):
        driver = self.driver
        contact = ContactsPage(driver)
        contact.enter_name(name)
        contact.enter_email(email)
        contact.enter_phone(phone)
        contact.click_submit()
        el = contact.get_element_by_xpath(contact.phone_input_error_xpath)
        assert el is not None, 'Phone error element does not exist'