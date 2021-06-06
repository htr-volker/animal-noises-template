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
            self.assertIn(response.json['height'],[1.524,1.626,1.7272,1.8034,1.880,1.93,2.007])