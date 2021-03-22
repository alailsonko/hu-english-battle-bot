from flask import Flask
from flask_pymongo import PyMongo
from settings import MONGO_URI, TOKEN
import telegram

bot = telegram.Bot(token=TOKEN)

app = Flask(__name__)

app.config["MONGO_URI"] = MONGO_URI

mongo = PyMongo(app)
