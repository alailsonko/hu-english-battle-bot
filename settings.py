import os
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv('TOKEN')
URL = os.getenv('APP_URL')
MONGO_URI = os.getenv("MONGO_URI")