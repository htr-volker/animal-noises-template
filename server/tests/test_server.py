from flask import url_for
from flask_testing import TestCase
from app import app, db
import requests_mock

class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
            DEBUG=True
        )
        return app

    def setUp(self):
        db.create_all()
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestHome(TestBase):
    def test_home_get(self):
        with requests_mock.Mocker() as m:
            m.get("http://animal_api_type:5000/get_animal", text='pig')
            m.post("http://animal_api_noise:5000/get_noise", text='oink')
            response = self.client.get(url_for("home"))
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'The pig goes oink', response.data)
    
    def test_db(self):
        with requests_mock.Mocker() as m:
            test_cases = [("pig", "oink"), ("horse", "neigh")]
            for case in test_cases:
                m.get("http://animal_api_type:5000/get_animal", text=case[0])
                m.post("http://animal_api_noise:5000/get_noise", text=case[1])
                response = self.client.get(url_for("home"))
            self.assertIn(b'The pig goes oink', response.data)
            self.assertIn(b'The horse goes neigh', response.data)
