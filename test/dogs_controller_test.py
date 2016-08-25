import json

from dogs.server import app


class TestDogsController(object):

    def test_homepage(self):
        """
        Send a GET request to the homepage "/" and maek sure we see "Hello World!"
        """
        client = app.test_client()
        response = client.get('/')
        assert "Hello World!" == response.data

    def test_addmoredogs_simple(self):
        client = app.test_client()
        response = client.post(
            '/addmoredogs',
            data=json.dumps({
                "dogs": [
                    {
                        "name": "Fido",
                        "size": "medium"
                    }
                ]
            }),
            headers={
                'Content-Type': 'application/json'
            }
        )
        response_data = json.loads(response.data)
        assert {
            "total": 1,
            "medium": 1
        } == response_data

    def test_addmoredogs_complex(self):
        client = app.test_client()
        response = client.post(
            '/addmoredogs',
            data=json.dumps({"dogs": [
                    {
                        "name": "Fido",
                        "size": "medium"
                    },
                    {
                        "name": "Jack",
                        "size" : "small"
                    },
                    {
                        "name": "Odie",
                        "size": "medium"
                    }
                ]
            }),
            headers={
                'Content-Type': 'application/json'
            }
        )
        response_data = json.loads(response.data)
        assert {
            "total": 3,
            "medium": 2,
            "small": 1
        } == response_data
