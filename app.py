from flask import Flask

app = Flask(__name__)

from controller import *

@app.route("/")
def home():
    return 'Thsi is a home'


@app.route("/contact")
def contact():
    return 'This is a contact page for the testing'



