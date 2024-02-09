from app import app
from model.user_model import User_model
obj = User_model()

@app.route("/signup")
def signup():
    return obj.user_signup_model()

