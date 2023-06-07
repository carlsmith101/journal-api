"""
Application Configuration

This module defines the configuration classes for different environments in the application.

- BaseConfig: The base configuration class with common settings.
- DevelopmentConfig: Configuration class for the development environment.
- TestingConfig: Configuration class for the testing environment.
- ProductionConfig: Configuration class for the production environment.

For more information and usage examples, refer to the documentation or visit the project repository at: https://github.com/yourusername/yourproject

"""


import os


class BaseConfig:
    """
    Base Configuration

    Represents the base configuration for the application. Includes common settings. 
    """
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'my_precious'


class DevelopmentConfig(BaseConfig):
    """
    Development Configuration

    Represents the configuration for the development environment.

    Inherits:
        BaseConfig: The base configuration class.

    """
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


class TestingConfig(BaseConfig):
    """
    Testing Configuration

    Represents the configuration for the testing environment.

    Inherits:
        BaseConfig: The base configuration class.

    """
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_TEST_URL')


class ProductionConfig(BaseConfig):
    """
    Production Configuration

    This class represents the configuration for the production environment.

    Inherits:
        BaseConfig: The base configuration class.

    """
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
