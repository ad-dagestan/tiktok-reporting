import os

class Config:
    """
    Configuration class to manage all settings and environment variables.
    """

    @staticmethod
    def get(key, default=None):
        return os.getenv(key, default)

    @staticmethod
    def load_config():
        """
        Load configuration from environment variables or provide defaults.
        """
        return {
            'API_KEY': Config.get('API_KEY'),
            'DB_URL': Config.get('DB_URL'),
            'LOG_LEVEL': Config.get('LOG_LEVEL', 'INFO'),
        }

# Usage example:
# config = Config.load_config()