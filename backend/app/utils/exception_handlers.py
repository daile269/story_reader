from flask import jsonify
from app.utils.api_response import api_response 

def register_error_handlers(app):
    @app.errorhandler(404)
    def not_found_error(error):
        return jsonify(api_response(404, "Không tìm thấy tài nguyên", None)), 404

    @app.errorhandler(400)
    def bad_request_error(error):
        return jsonify(api_response(400, "Yêu cầu không hợp lệ", None)), 400

    @app.errorhandler(Exception)
    def internal_error(error):
        return jsonify(api_response(500, "Lỗi hệ thống", None)), 500