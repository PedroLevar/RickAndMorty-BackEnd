import os
from flask import Flask
from flask_cors import CORS
from src.models import db, ma
from config.settings import DATABASE_URI, front_end_url, environment
from src.routes.character_route import character_bp 
from src.utils.constants import ENVIRONMENTS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)
ma.init_app(app)

origins_map = {
    ENVIRONMENTS.LOCAL.value: ["*"],
    ENVIRONMENTS.PRODUCTION.value: [front_end_url],
}

allowed_origin = origins_map.get(environment, origins_map[ENVIRONMENTS.PRODUCTION.value])

CORS(app, origins = allowed_origin)

app.register_blueprint(character_bp, url_prefix='/character')

if __name__ == "__main__":
    app.run(debug=True)