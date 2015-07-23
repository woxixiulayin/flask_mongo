from flask import Flask
from flask.ext.mongoengine import MongoEngine
app = Flask(__name__)

app.config["MONGODB_SETTINGS"] = {'DB':"test"}
app.config["SECRET_KEY"] = "This_sc3r3t_my~key"

db = MongoEngine(app)

def register_blueprints(app):
    # Prevents circular imports
    from tumblelog.views import posts
    app.register_blueprint(posts)

register_blueprints(app)

if __name__ == "__main__":
    app.run()
