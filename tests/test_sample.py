import pytest


def inc(x):
    return x+1

def test_inc():
    assert inc(4)==5


@pytest.fixture
def smtp():
    import smtplib
    return smtplib.SMTP("merlinux.eu")

def test_ehlo(smtp):
    response, msg = smtp.ehlo()
    assert response == 250
    assert 0 # for demo purposes