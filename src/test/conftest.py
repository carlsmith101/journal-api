"""
"""

import os
import pytest

from typing import Optional
from datetime import date

from src import create_app, db
from src.api.models import Entry


@pytest.fixture(scope='module')
def test_app():
    # setup
    os.environ['APP_SETTINGS'] = 'src.config.TestingConfig'
    app = create_app()

    # usage
    with app.app_context():
        yield app


@pytest.fixture(scope='function')
def test_database():
    # setup
    db.create_all()

    # usage
    yield db

    # teardown
    db.session.remove()
    db.drop_all()

@pytest.fixture(scope='function')
def add_entry():
    """
    Test fixture that adds a new Journal entry.

    This fixture follows the 'factory as fixture' pattern, as described in the PyTest documentation:

    https://docs.pytest.org/en/latest/how-to/fixtures.html#factories-as-fixtures
    """

    def _add_entry(content: str, entry_date: Optional[date] = None) -> Entry:
            entry = Entry(content, entry_date)
            db.session.add(entry)
            db.session.commit()
            return entry
    return _add_entry
