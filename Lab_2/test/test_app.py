# http://flask.pocoo.org/docs/1.0/testing/

import os
import pytest

from main import *

# This will get called before every test and can be used to set up a testing DB
@pytest.fixture
def client():
    client = app.test_client()
    yield client


def test_title(client):
    """Verify the title"""
    rv = client.get('/')
    assert b'Prime Number Regurgitator' in rv.data

def test_multiplication_POST(client):
    """Verify prime number maker works"""
    rv = client.post('/', data={'Low':4, 'High':6}) # sends a and b as post values
    assert b'5' in rv.data

def test_multiplication_GET(client):
    """Verify prime number maker works"""
    rv = client.get('/?Low=6&High=8') # sends a and b as post values
    assert b'7' in rv.data

def test_NegHigh_Get(client):
    rv = client.get('/?Low=1&High=-9')
    assert b'"Enter positive whole numbers.  In the url (Example) ?json=1&Low=1&High=15"' in rv.data

def test_NegLow_Get(client):
    rv = client.get('/?Low=-1&High=9')
    assert b'"Enter positive whole numbers.  In the url (Example) ?json=1&Low=1&High=15"' in rv.data

def test_NegBoth_Get(client):
    rv = client.get('/?Low=-1&High=-9')
    assert b'"Enter positive whole numbers.  In the url (Example) ?json=1&Low=1&High=15"'

def test_JSON_Get(client):
    rv = client.get('')
