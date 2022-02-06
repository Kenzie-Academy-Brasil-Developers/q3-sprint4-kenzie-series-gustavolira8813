
from flask import Blueprint, Flask
from app.routes.serie_routes import bp

bp_api = Blueprint("api", __name__, url_prefix="/")

def init_app(app: Flask):
    bp_api.register_blueprint(bp)
    app.register_blueprint(bp_api)
