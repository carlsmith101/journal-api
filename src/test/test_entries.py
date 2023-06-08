"""
"""


import json

from datetime import date


def test_add_entry(test_app, test_database):
    # Arrange
    client = test_app.test_client()

    # Act
    resp = client.post(
        '/entries',
        data=json.dumps({
            'content': 'Dear Diary. Today was an eventful day',
        }),
        content_type='application/json',
    )
    data = json.loads(resp.data.decode())

    # Assert
    assert resp.status_code == 201
    assert 'Journal entry added successfully' in data['message']


def test_add_entry_invalid_json(test_app, test_database):
    # Arrange
    client = test_app.test_client()

    # Act
    resp = client.post(
        '/entries',
        data=json.dumps({}),
        content_type='application/json',
    )
    data = json.loads(resp.data.decode())

    # Assert
    assert resp.status_code == 400
    assert 'Input payload validation failed' in data['message']


def test_add_entry_invalid_json_keys(test_app, test_database):
    # Arrange
    client = test_app.test_client()

    # Act
    resp = client.post(
        '/entries',
        data=json.dumps({
            'discontent': 'Dear Diary. Today was an eventful day',
        }),
        content_type='application/json',
    )
    data = json.loads(resp.data.decode())

    # Assert
    assert resp.status_code == 400
    assert 'Input payload validation failed' in data['message']


def test_add_entry_duplicate_date(test_app, test_database):
    # Arrange
    client = test_app.test_client()

    client.post(
        '/entries',
        data=json.dumps({
            'content': 'Dear Diary. Today was an eventful day',
        }),
        content_type='application/json',
    )

    # Act
    resp = client.post(
        '/entries',
        data=json.dumps({
            'content': 'Dear Diary. Today continued being eventful',
        }),
        content_type='application/json',
    )
    data = json.loads(resp.data.decode())

    # Assert
    assert resp.status_code == 400
    assert 'A journal entry already exists for today' in data['message']


def test_get_entry(test_app, test_database, add_entry):
    # Arrange
    entry = add_entry('Dear Diary. This was a great day')

    client = test_app.test_client()

    # Act
    resp = client.get(f'/entries/{entry.entry_date}')
    data = json.loads(resp.data.decode())

    # Assert
    assert resp.status_code == 200
    assert 'Dear Diary. This was a great day' in data['content']


def test_get_nonexistant_entry(test_app, test_database):
    # Arrange
    client = test_app.test_client()

    # Act
    resp = client.get(f'/entries/2023-01-01')
    data = json.loads(resp.data.decode())

    # Assert
    assert resp.status_code == 404
    assert 'Journal entry on date 2023-01-01 does not exist' in data['message']


def test_get_all_entries(test_app, test_database, add_entry):
    # Arrange
    add_entry('Dear diary, this is my first entry', date(2023, 1, 1))
    add_entry('Dear diary, this is my second entry', date(2023, 1, 2))
    client = test_app.test_client()

    # Act
    resp = client.get('/entries')
    data = json.loads(resp.data.decode())

    # Assert
    assert resp.status_code == 200
    assert len(data) == 2
    assert 'Dear diary, this is my first entry' in data[0]['content']
    assert '2023-01-01' in data[0]['entry_date']
    assert 'Dear diary, this is my second entry' in data[1]['content']
    assert '2023-01-02' in data[1]['entry_date']
