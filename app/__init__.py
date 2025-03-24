from flask import Flask

def create_app(config_class=None):
    """
    Application factory function
    
    Args:
        config_class: Configuration class (optional)
    
    Returns:
        Flask application instance
    """
    app = Flask(__name__)
    
    # Load configuration
    from config import Config
    app.config.from_object(config_class or Config)
    
    # Register routes
    from .routes import main
    app.register_blueprint(main)
    
    return app
