"""
"""


import json


def test_ping(test_app):
    """
    """

    # Arrange
    client = test_app.test_client()

    # Act
    resp = client.get('/ping')
    data = json.loads(resp.data.decode())

    # Assert
    assert resp.status_code == 200
    assert 'pong' in data['message']
    assert 'success' in data['status']
