import logging

def setup_logging():
    # Application logger
    app_logger = logging.getLogger("app")
    app_logger.setLevel(logging.INFO)
    app_handler = logging.FileHandler("app.log", encoding="utf-8")
    app_handler.setFormatter(logging.Formatter('[%(asctime)s] %(levelname)s in %(module)s: %(message)s'))
    app_logger.addHandler(app_handler)

    # Access logger
    access_logger = logging.getLogger("access")
    access_logger.setLevel(logging.INFO)
    access_handler = logging.FileHandler("access.log", encoding="utf-8")
    access_handler.setFormatter(logging.Formatter('%(asctime)s %(message)s'))
    access_logger.addHandler(access_handler)

    # Optional: log to console as well
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(logging.Formatter('[%(asctime)s] %(levelname)s in %(module)s: %(message)s'))
    app_logger.addHandler(console_handler)
    access_logger.addHandler(console_handler)

    return app_logger, access_logger