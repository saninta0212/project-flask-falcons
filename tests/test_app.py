# test/test_app.py

import unittest
import os

os.environ['TESTING'] = 'true'

from app.app import app


class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>MLH Fellow</title>" in html

        # home contains menu bar
        assert '<nav class="menu-bar">' in html
        assert '</nav>' in html
        # home has image
        assert '<img ' in html

    def test_timeline(self):
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json

        json = response.get_json()
        assert "timeline_post" in json
        assert len(json["timeline_post"]) == 0

        # Correct post request
        response = self.client.post("/api/timeline_post", data={
            "email": "testpost@example.com",
            "content": "This is a post from test_app.py test",
            "name": "John Doe"
        })
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "This is a post from test_app.py test" in html

    def test_malformed_timeline_post(self):
        # POST request missing name
        response = self.client.post("/api/timeline_post", data={
            "email": "john@example.com",
            "content": "Hello world, I'm John!",
        })
        assert response.status_code == 400
        res_message = response.get_data(as_text=True)
        assert "Invalid name" in res_message

        # POST request with empty content
        response = self.client.post("/api/timeline_post", data={
            "email": "john@example.com",
            "content": "",
            "name": "John Doe"
        })
        assert response.status_code == 400
        res_message = response.get_data(as_text=True)
        assert "Invalid content" in res_message

        # POST request with malformed email
        response = self.client.post("/api/timeline_post", data={
            "email": "not-an-email",
            "content": "Hello world, I'm John!",
            "name": "John Doe"
        })
        assert response.status_code == 400
        res_message = response.get_data(as_text=True)
        assert "Invalid email" in res_message
