from flask import Flask

def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config['FLASK_ENV'] = 'development'
    app.config['DEBUG'] = False
    app.config['TESTING'] = True

    with app.app_context():
        from .routes import uiRoutes

        return app