# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application_contacts import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contacts(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="John", middlename="Christopher", lastname="Depp",
                               mobile="89993332211", email="jcd@gmail.com"))
    app.logout()


def test_add_empty_contacts(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="", middlename="", lastname="", mobile="", email=""))
    app.logout()
