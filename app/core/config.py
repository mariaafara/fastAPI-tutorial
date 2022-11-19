'''
Here, we defined a Settings class with a db_url attribute. BaseSettings, from pydantic, validates the data so that when we create an instance of Settings, db_url will be automatically loaded from the environment variable.

We could have used os.getenv(), but as the number of environment variables increases, this becomes very repetitive. By using a BaseSettings, you can specify the environment variable name and it will automatically be loaded.
'''

import os

# we use the pydantic.BaseSettings to load variables from the environment.
from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    db_url: str = Field(env='DB_CONN')


settings = Settings()
