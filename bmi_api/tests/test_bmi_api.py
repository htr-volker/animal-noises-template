from flask import url_for
from flask_testing import TestCase
from bmi_api.app import app


class TestBase(TestCase):
    def create_app(self):
        return app

class TestHome(TestBase):
    def test_get_bmi(self):
        response = self.client.post(url_for('get_bmi'), json={
            'height':1.524,
            'weight':100
        })
        self.assertEqual(response.data.decode("utf-8"),"overweight")
