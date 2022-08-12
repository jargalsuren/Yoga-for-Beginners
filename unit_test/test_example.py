# Example taken from:
# http://flask.pocoo.org/docs/1.0/testing/
# and suitably modified.
import os
import tempfile
import unittest

# import pytest

from web import app

class FlaskTestCase(unittest.TestCase):
    #check that the flask app was set up well and can correctly display the webpage with status code 200
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type = "html/text")
        return self.assertEqual(response.status_code, 200)


# @pytest.fixture
# def client():
#     db_fd, app.config['DATABASE'] = tempfile.mkstemp()
#     app.config['TESTING'] = True
#     client = app.test_client()

#     yield client

#     os.close(db_fd)
#     os.unlink(app.config['DATABASE'])


# def test_empty_db(client):
#     """Start with a blank database."""

#     rv = client.get('/')
#     assert b'Hello World!' in rv.data

if __name__ == '__main__':
    unittest.main()