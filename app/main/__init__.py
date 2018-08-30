from flask import Blueprint
main = Blueprint('main', __name__)
from .import views, errors

def create_app(config_name):
    #.....
    from ..main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from .requests import configure_request
    configure_request(app)
    return create_app
  