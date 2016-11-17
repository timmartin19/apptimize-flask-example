import random
import string
import unittest

from webtest import TestApp

from myapp.manage import app
from myapp.models import DB


class TestUser(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        app.debug = True
        with app.app_context():
            DB.create_all()
        cls.app = TestApp(app)

    def test_create_user_invalid(self):
        resp = self.app.post_json('/user', dict(first_name='blah'), expect_errors=True)
        self.assertEqual(400, resp.status_code)

    def test_create_user_valid(self):
        username = ''.join([random.choice(string.ascii_letters) for i in range(10)])  # 10 character random string
        request_data = dict(username=username, first_name='blah')
        resp = self.app.post_json('/user', request_data)
        self.assertEqual(200, resp.status_code)
        self.assertEqual(username, resp.json['username'])
        self.assertEqual('blah', resp.json['first_name'])
        self.assertIn('id', resp.json)

