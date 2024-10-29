import os
from dotenv import load_dotenv
from pydantic import PostgresDsn, ValidationError

# Load environment variables from the .env file
load_dotenv(os.path.join(os.path.dirname(__file__), '../../.env'))

class Settings:
    def __init__(self):
        # Load the DATABASE_URL from the environment variables
        self.database_url = os.getenv("DATABASE_URL")

        # Validate the database URL
        # self.validate()

    def validate(self):
        """Validate the configuration settings."""
        if not self.database_url:
            raise ValueError("DATABASE_URL environment variable is required.")

        try:
            # Validate that the database_url is a valid Postgres DSN
            PostgresDsn.validate(self.database_url)
        except ValidationError as e:
            raise ValueError(f"Invalid DATABASE_URL: {e}")

# Initialize the settings instance
settings = Settings()
