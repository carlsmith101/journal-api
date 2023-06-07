"""
Application Configuration

This module defines the configuration classes for different environments in the application.

- BaseConfig: The base configuration class with common settings.
- DevelopmentConfig: Configuration class for the development environment.
- TestingConfig: Configuration class for the testing environment.
- ProductionConfig: Configuration class for the production environment.

For more information and usage examples, refer to the documentation or visit the project repository at: https://github.com/yourusername/yourproject

"""


class BaseConfig:
    """
    Base Configuration

    This class represents the base configuration for the application with common settings. 
    """
    TESTING = False


class DevelopmentConfig(BaseConfig):
    """
    Development Configuration

    This class represents the configuration for the development environment.

    Inherits:
        BaseConfig: The base configuration class.

    """
    pass


class TestingConfig(BaseConfig):
    """
    Testing Configuration

    This class represents the configuration for the testing environment.

    Inherits:
        BaseConfig: The base configuration class.

    """
    TESTING = True


class ProductionConfig(BaseConfig):
    """
    Production Configuration

    This class represents the configuration for the production environment.

    Inherits:
        BaseConfig: The base configuration class.

    """
    pass