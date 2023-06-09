"""
test_ping

This module contains functional tests for the 'ping' resource of the API.

"""


import json


def test_ping(test_app):
    """
    This test ensures that the 'ping' resource returns a successful response with the expected message and status.

    """

    # Arrange
    client = test_app.test_client()

    # Act
    resp = client.get('/health/ping')
    data = json.loads(resp.data.decode())

    # Assert
    assert resp.status_code == 200
    assert 'pong' in data['message']
    assert 'success' in data['status']
