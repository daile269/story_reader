from flask import Blueprint, jsonify, request

from app.utils.api_response import api_response
from app.dto.category_dto import CategoryDTO, CategoryUpdateDTO
from app.services.category_service import CategoryService

category_bp = Blueprint("category", __name__)

@category_bp.route("/categories", methods=["GET"])
def get_categories():
    categories = CategoryService.get_all_categories()
    return jsonify(api_response(200, "Danh sách thể loại", categories)), 200

@category_bp.route("/categories/<int:category_id>", methods=["GET"])
def get_category_detail(category_id):
    category = CategoryService.get_category_by_id(category_id)
    if not category:
        return jsonify(api_response(404, "Không tìm thấy thể loại", None)), 404
    return jsonify(api_response(200, "Chi tiết thể loại", category)), 200

# Thêm thể loại
@category_bp.route("/categories", methods=["POST"])
def add_category():
    data = request.get_json()
    if not data or not data.get("name"):
        return jsonify(api_response(400, "Thiếu thông tin thể loại")), 400
    category_dto = CategoryDTO(**data)
    created_category = CategoryService.create_category(category_dto)
    return jsonify(api_response(200, "Thể loại đã được thêm thành công", created_category)), 200

# Sửa thể loại
@category_bp.route("/categories/<int:category_id>", methods=["PUT"])
def update_category(category_id):
    data = request.get_json()
    if not data or not data.get("name"):
        return jsonify(api_response(400, "Thiếu thông tin thể loại")), 400
    category_update_dto = CategoryUpdateDTO(**data)
    updated_category = CategoryService.update_category(category_update_dto, category_id)
    if not updated_category:
        return jsonify(api_response(404, "Không tìm thấy thể loại")), 404
    return jsonify(api_response(200, "Thể loại đã được sửa thành công", updated_category)), 200

# Xóa thể loại
@category_bp.route("/categories/<int:category_id>", methods=["DELETE"])
def delete_category(category_id):
    deleted_category = CategoryService.delete_category(category_id)
    if not deleted_category:
        return jsonify(api_response(404, "Không tìm thấy thể loại")), 404
    return jsonify(api_response(200, "Thể loại đã được xóa thành công", deleted_category)), 200
