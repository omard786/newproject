from app import app
from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
import random


class TestBase(TestCase):
    def create_app(self):
        return app

class testnumbers(TestBase):
    def test_numbers(self):
        response = self.client.get(url_for('numbers'))
        self.assertEqual(response.status_code, 200)

    def test_letters(self):         
        with patch('random.randint') as a:
            a.return_value = '5'
            response = self.client.get(url_for('numbers'))
            self.assertIn(b'333333', response.data)