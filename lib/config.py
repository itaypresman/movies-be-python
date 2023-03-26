import os
import dotenv

dotenv.load_dotenv()


class Config:
    PORT = os.environ.get('PORT')
    OIMDB_URL = os.environ.get('OIMDB_URL')
    OIMDB_TOKEN = os.environ.get('OIMDB_TOKEN')
