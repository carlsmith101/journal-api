"""
"""


import uuid

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from typing import Optional
from datetime import date

from src import db


class Entry(db.Model):
    """
    
    """
    __tablename__ = 'entries'
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    content = db.Column(db.String(2000), nullable=False)
    entry_date = db.Column(db.Date, nullable=False, unique=True, default=func.current_date())

    def __init__(self, content: str, entry_date: Optional[date] = None):
        self.content = content
        if entry_date:
            self.entry_date = entry_date
