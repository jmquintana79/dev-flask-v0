from flask import Flask

app = Flask(__name__)


# this line is always in the end
from app import views