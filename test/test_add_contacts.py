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
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="John", middlename="Christopher", lastname="Depp",
                               mobile="89993332211", email="jcd@gmail.com"))
    app.session.logout()


def test_add_empty_contacts(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="", middlename="", lastname="", mobile="", email=""))
    app.session.logout()
