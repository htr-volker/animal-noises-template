from flask import url_for
from flask_testing import TestCase
from app import app
from unittest.mock import patch

class TestBase(TestCase):
    def create_app(self):
        app.config.update(DEBUG=True)
        return app

test_cases = [("pig","oink"),("cow","moo"),("horse","neigh")]

class TestHome(TestBase):  
    def test_get_noise(self):
        for case in test_cases:
            response = self.client.post(url_for("get_noise"), data=case[0])
            self.assertEqual(response.status_code, 200)
            self.assertIn(case[1], response.data.decode("utf-8"))
    