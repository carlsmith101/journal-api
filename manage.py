"""
This module uses the flask CLI tool to enable running and management of a flask app from the command line.
"""


from flask.cli import FlaskGroup

from src import app


cli = FlaskGroup(app)


if __name__ == '__main__':
    cli()