import pytest
import smtplib

"""connection checking/testing"""

"""return ends the function"""
# @pytest.fixture
# def smtp_connection():
#     return smtplib.SMTP("smtp.gmail.com", 587, timeout=5)

"""yeild allows subsequent code to run later"""
@pytest.fixture
def smtp_connection():
    smtp_connection = smtplib.SMTP("smtp.gmail.com",587, timeout=5)
    yield smtp_connection
    smtp_connection.close()

def test_ehlo(smtp_connection):
    response, msg = smtp_connection.ehlo()
    print("resposn", response)
    print("message", msg)
    assert response == 250
def test_helo(smtp_connection):
    response, msg = smtp_connection.helo()
    assert response == 250