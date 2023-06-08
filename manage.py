"""
Uses the flask CLI tool to enable running and management of the Journal Application from the command line.
"""


import sys

from flask.cli import FlaskGroup
from datetime import date

from src import create_app, db
from src.api.models import Entry


cli = FlaskGroup(create_app=create_app)


@cli.command('recreate_db')
def recreate_db():
    """
    Recreate the database by dropping and creating all tables.
    """

    db.drop_all()
    db.create_all()
    db.session.commit()

@cli.command('seed_db')
def seed_db():
    db.session.add(Entry(content='This is a journal entry', entry_date=date(2023,1,1)))
    db.session.add(Entry(content='This is another journal entry', entry_date=date(2023,1,2)))
    db.session.commit()


if __name__ == '__main__':
    cli()
