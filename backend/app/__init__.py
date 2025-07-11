from flask import Flask
from app.extensions import db
from app.utils.exception_handlers import register_error_handlers

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    db.init_app(app)

    from .routes.story_routes import story_bp
    from .routes.chapter_routes import chapter_bp
    app.register_blueprint(story_bp)
    app.register_blueprint(chapter_bp)
    # register_error_handlers(app)
    return app