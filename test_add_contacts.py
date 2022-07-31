# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
from contact import Contact
from application_contacts import Application


class TestAddContacts(unittest.TestCase):
    def setUp(self):
        self.app = Application()

    def test_add_contacts(self):
        self.app.login(username="admin", password="secret")
        self.app.create_contact(Contact(firstname="John", middlename="Christopher", lastname="Depp",
                                        mobile="89993332211", email="jcd@gmail.com"))
        self.app.logout()

    def test_add_empty_contacts(self):
        self.app.login(username="admin", password="secret")
        self.app.create_contact(Contact(firstname="", middlename="", lastname="", mobile="", email=""))
        self.app.logout()

    def tearDown(self):
        self.app.destroy()


if __name__ == "__main__":
    unittest.main()
