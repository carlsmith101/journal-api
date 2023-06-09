"""
manage

Uses the flask CLI tool to enable running and management of the Journal Application from the command line.

Usage:

`python manage.py {command}`

Example commands:

- run the application: `python manage.py run`

- recreate the database: `python manage.py recreate_db`

- seed the database: `python manage.py seed_db`

For more information on using the Flask CLI, refer to the [Flask documentation](https://flask.palletsprojects.com/en/latest/cli/).

"""


from flask.cli import FlaskGroup
from datetime import date

from src import create_app, db
from src.api.models import Entry


cli = FlaskGroup(create_app=create_app)


@cli.command('recreate_db')
def recreate_db():
    """
    Flask CLI command to recreate the database by dropping and creating all tables.

    Usage:

    `python manage.py recreate_db`

    """

    db.drop_all()
    db.create_all()
    db.session.commit()

@cli.command('seed_db')
def seed_db():
    """
    Flask CLI command to seed the database with example data for local development.

    Usage:

    `python manage.py seed_db`

    """

    db.session.add(Entry(content='This is a journal entry', entry_date=date(2023,1,1)))
    db.session.add(Entry(content='This is another journal entry', entry_date=date(2023,1,2)))
    db.session.commit()


if __name__ == '__main__':
    cli()
