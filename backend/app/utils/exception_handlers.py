from email import message
from flask import jsonify
from app.utils.api_response import api_response 
from pydantic import ValidationError
def register_error_handlers(app):
    @app.errorhandler(404)
    def not_found_error(error):
        return jsonify(api_response(404, "Không tìm thấy tài nguyên", None)), 404

    @app.errorhandler(400)
    def bad_request_error(error):
        return jsonify(api_response(400, "Yêu cầu không hợp lệ", None)), 400

    @app.errorhandler(Exception)
    def internal_error(error):
        return jsonify(api_response(500, str(error), None)), 500
    
    @app.errorhandler(ValueError)
    def handle_value_error(error):
        return jsonify(api_response(400, str(error), None)), 400
    
    @app.errorhandler(ValidationError)
    def handle_validation_error(error):
        message = format_pydantic_error_message(error)
        return jsonify({
        "code": 400,
        "message": message,
        "result": None
        }), 400
    
    def format_pydantic_error_message(error):
        return "; ".join(
        f"{err['loc'][0]}: {err['msg']}" for err in error.errors()
    )