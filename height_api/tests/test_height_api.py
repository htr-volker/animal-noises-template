from flask import url_for
from flask_testing import TestCase
from height_api.app import app


class TestBase(TestCase):
    def create_app(self):
        return app

class TestHome(TestBase):
    def test_get_height(self):
        for _ in range(20):
            response = self.client.get(url_for('get_height'))
            self.assertIn(response.json['height'],[0.5,0.55,0.6,0.65,0.7])