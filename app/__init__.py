from flask import Flask

def create_app():
    app = Flask(__name__)

    # Register Blueprints or Import routes directly
    from .routes import main as main_routes
    app.register_blueprint(main_routes)

    return app
