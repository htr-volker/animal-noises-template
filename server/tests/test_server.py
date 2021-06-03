from flask import url_for
from flask_testing import TestCase
import requests_mock

from app import app, db

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
            DEBUG=True,
        )
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.drop_all()


class TestHome(TestBase):
    def test_home(self):
        with requests_mock.Mocker() as mocker:
            mocker.get('http://height_api:5000/get_height', json={'height':2.007})
            mocker.get('http://weight_api:5000/get_weight', json={'weight':40})
            mocker.post('http://bmi_api:5000/get_bmi',text='underweight')
            response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code,200)
        self.assertIn(b'The humans height in metres is 2.007 and weight in kilograms is 40 so you are underweight',response.data)
    
    