import os
from dotenv import load_dotenv

load_dotenv()


class SetupClass:

    @staticmethod
    def base_url():
        return os.getenv("BASE_URL")
