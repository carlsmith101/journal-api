"""
Uses the flask CLI tool to enable running and management of the Journal Application from the command line.
"""


from flask.cli import FlaskGroup

from src import app, db

@cli.command('recreate_db')
def recreate_db():
    """
    Recreate the database by dropping and creating all tables.
    """

    db.drop_all()
    db.create_all()
    db.session.commit()

cli = FlaskGroup(app)


if __name__ == '__main__':
    cli()
