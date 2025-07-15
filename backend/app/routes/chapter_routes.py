from flask import Blueprint, jsonify, request

from app.utils.api_response import api_response
from app.dto.chapter_dto import ChapterDTO
from app.services.chapter_service import ChapterService

chapter_bp = Blueprint("chapter", __name__)

@chapter_bp.route("/chapters", methods=["GET"])
def get_chapters():
    chapters = ChapterService.get_all_chapters()
    return jsonify(api_response(200, "Danh sách chương", chapters)), 200

@chapter_bp.route("/chapters/<int:chapter_id>", methods=["GET"])
def get_chapter_detail(chapter_id):
    chapter = ChapterService.get_chapter_by_id(chapter_id)
    if not chapter:
        return jsonify(api_response(404, "Không tìm thấy chương", None)), 404
    return jsonify(api_response(200, "Chi tiết chương", chapter)), 200

# Thêm chương
@chapter_bp.route("/chapters", methods=["POST"])
def add_chapter():
    data = request.get_json()
    if not data:
        return jsonify(api_response(400, "Thiếu thông tin chương")), 400
    chapter_dto = ChapterDTO(**data)
    created_chap= ChapterService.create_chapter(chapter_dto)
    if not created_chap:
        return jsonify(api_response(404, "Tạo mới thất bại, truyện không tồn tại")), 404
    return jsonify(api_response(200, "Chương đã được thêm thành công", data)), 200

# Sửa chương
@chapter_bp.route("/chapters/<int:chapter_id>", methods=["PUT"])
def update_chapter(chapter_id):
    data = request.get_json()
    if not data:
        return jsonify(api_response(400, "Thiếu thông tin chương")), 400
    chapter_dto = ChapterDTO(**data)
    ChapterService.update_chapter(chapter_dto, chapter_id)
    return jsonify(api_response(200, "Chương đã được sửa thành công", data)), 200

# Xóa chương
@chapter_bp.route("/chapters/<int:chapter_id>", methods=["DELETE"])
def delete_chapter(chapter_id):
    deleted_chapter = ChapterService.delete_chapter(chapter_id)
    if not deleted_chapter:
        return jsonify(api_response(404, "Không tìm thấy chương")), 404
    return jsonify(api_response(200, "Chương đã được xóa thành công", deleted_chapter)), 200
