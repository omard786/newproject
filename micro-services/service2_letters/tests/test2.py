  
from flask_testing import TestCase
from flask import Flask, url_for
from flask import Response, request
from os import getenv
import random
from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestRandomNumberGenerator(TestBase):
    def random_number(self):
        response = self.client.get(url_for('random_number'))
        self.assertEqual(len(response.data), 5)

class TestRandomNumberGen(TestBase):
    def number_gen(self):
        response = self.client.get(url_for('number_gen'))
        self.assertEqual(response.status_code, 200)