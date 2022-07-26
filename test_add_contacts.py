# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from contact import Contact


def open_home_page(wd):
    wd.get("http://localhost/addressbook/")


def login(wd, username, password):
    wd.find_element_by_name("user").click()
    wd.find_element_by_name("user").clear()
    wd.find_element_by_name("user").send_keys(username)
    wd.find_element_by_name("pass").click()
    wd.find_element_by_name("pass").clear()
    wd.find_element_by_name("pass").send_keys(password)
    wd.find_element_by_xpath("//input[@value='Login']").click()


def open_add_new_page(wd):
    wd.find_element_by_link_text("add new").click()


def create_contact(wd, contact):
    wd.find_element_by_name("firstname").click()
    wd.find_element_by_name("firstname").clear()
    wd.find_element_by_name("firstname").send_keys(contact.firstname)
    wd.find_element_by_name("middlename").click()
    wd.find_element_by_name("middlename").clear()
    wd.find_element_by_name("middlename").send_keys(contact.middlename)
    wd.find_element_by_name("lastname").click()
    wd.find_element_by_name("lastname").clear()
    wd.find_element_by_name("lastname").send_keys(contact.lastname)
    wd.find_element_by_name("mobile").click()
    wd.find_element_by_name("mobile").clear()
    wd.find_element_by_name("mobile").send_keys(contact.mobile)
    wd.find_element_by_name("email").click()
    wd.find_element_by_name("email").clear()
    wd.find_element_by_name("email").send_keys(contact.email)
    # enter contact
    wd.find_element_by_name("theform").click()
    wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()


def logout(wd):
    wd.find_element_by_link_text("Logout").click()


class TestAddContacts(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(30)

    def test_add_contacts(self):
        wd = self.wd
        open_home_page(wd)
        login(wd, username="admin", password="secret")
        open_add_new_page(wd)
        create_contact(wd, Contact(firstname="John", middlename="Christopher", lastname="Depp", mobile="89993332211",
                       email="jcd@gmail.com"))
        logout(wd)

    def test_add_empty_contacts(self):
        wd = self.wd
        open_home_page(wd)
        login(wd, username="admin", password="secret")
        open_add_new_page(wd)
        create_contact(wd, Contact(firstname="", middlename="", lastname="", mobile="", email=""))
        logout(wd)

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
