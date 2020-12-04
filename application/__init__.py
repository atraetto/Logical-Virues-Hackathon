from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['FLASK_ENV'] = 'development'
    app.config['DEBUG'] = False
    app.config['TESTING'] = True
    app.secret_key = 'super secret key'

    with app.app_context():
        from .routes import uiRoutes

        return app