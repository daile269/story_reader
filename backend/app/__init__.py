from flask import Flask, request
from app.extensions import db
from app.utils.exception_handlers import register_error_handlers
from app.config.logging_config import setup_logging

app_logger, access_logger = setup_logging()


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    db.init_app(app)

    @app.before_request
    def log_request_info():
        access_logger.info(f"{request.remote_addr} {request.method} {request.path}")

    @app.after_request
    def log_response_info(response):
        access_logger.info(
            f"{request.remote_addr} {request.method} {request.path} {response.status_code} {request.user_agent}"
        )
        return response

    from .routes.story_routes import story_bp
    from .routes.chapter_routes import chapter_bp
    from .routes.category_routers import category_bp
    app.register_blueprint(story_bp)        
    app.register_blueprint(chapter_bp)
    app.register_blueprint(category_bp)
    register_error_handlers(app)
    return app