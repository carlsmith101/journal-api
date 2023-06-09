"""
models

This module contains the SQLAlchemy models for the journal application.

The module includes the following models:

Entry: Represents a journal entry.

For detailed information about each model and its attributes, please refer to the individual class docstrings.

"""


import uuid

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from typing import Optional
from datetime import date

from src import db


class Entry(db.Model):
    """
    Entry Model

    Represents a journal entry in the application.

    Attributes:
    - id (UUID): The unique identifier for the entry.
    - content (str): The content of the journal entry.
    - entry_date (date): the date of the journal entry.

    """

    __tablename__ = 'entries'
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    content = db.Column(db.String(2000), nullable=False)
    entry_date = db.Column(db.Date, nullable=False, unique=True, default=func.current_date())

    def __init__(self, content: str, entry_date: Optional[date] = None):
        """
        Initialize a new journal entry.

        Args:
        - content (str): The content of the journal entry.
        - entry_date (date, optional): The date of the journal entry. Defaults to the current date if not provided.

        """

        self.content = content
        if entry_date:
            self.entry_date = entry_date
