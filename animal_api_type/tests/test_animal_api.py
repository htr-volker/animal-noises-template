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
    def test_get_animal(self):
        for case in test_cases:
            with patch('random.choice') as r:
                r.return_value = case[0]
                response = self.client.get(url_for("get_animal"))
                self.assertEqual(response.status_code, 200)
                self.assertIn(case[0], response.data.decode("utf-8"))
    