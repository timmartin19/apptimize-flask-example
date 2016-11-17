import unittest

from myapp.models import User


class TestToJson(unittest.TestCase):
    def test_user_to_json(self):
        # No database dependencies here :)
        user = User(first_name='blah', username='something', id='blah')
        json_dict = user.to_json()
        self.assertEqual(user.first_name, json_dict['first_name'])
        self.assertEqual(user.username, json_dict['username'])
        self.assertEqual(user.id, json_dict['id'])
