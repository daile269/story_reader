from .story_routes import story_bp

def register_routes(app):
    app.register_blueprint(story_bp, url_prefix="/api")
