from flask_app import app
from flask_app.controllers import users
from flask_app.controllers import posts
from flask_app.controllers import user_profiles

if __name__ == '__main__':
    app.run(debug = True)