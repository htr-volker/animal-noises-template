from flask import url_for
from flask_testing import TestCase
from weight_api.app import app


class TestBase(TestCase):
    def create_app(self):
        return app

class TestHome(TestBase):
    def test_get_weight(self):
        for _ in range(20):
            response = self.client.get(url_for('get_weight'))
            self.assertIn(response.json['weight'],[40,50,60,70,80,90,100])