from flask import Flask
from indigc.config import Config

app = Flask(__name__)
app.config.from_object(Config)

from indigc import routers
