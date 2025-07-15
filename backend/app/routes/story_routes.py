from flask import Blueprint, jsonify, request

from app.utils.api_response import api_response
from app.dto.story_dto import StoryDTO, StoryUpdateDTO


from ..models import Story
from app.services.story_service import StoryService 
from .. import db

story_bp = Blueprint("story", __name__)

@story_bp.route("/stories", methods=["GET"])
def get_stories():
    stories = StoryService.get_all_stories()    
    return jsonify(api_response(200,"Danh sách truyện",stories)), 200

@story_bp.route("/stories/<int:story_id>", methods=["GET"])
def get_story_detail(story_id):
    story = StoryService.get_story_by_id(story_id)
    if not story:
        return jsonify(api_response(404, "Không tìm thấy truyện", None)), 404
    return jsonify(api_response(200,"Danh sách truyện",story)), 200

# Thêm truyện
@story_bp.route("/stories", methods=["POST"])
def add_story():
    data = request.get_json()
    if not data:
        return jsonify(api_response(400, "Thiếu thông tin truyện")), 400
    story_dto = StoryDTO(**data)  
    StoryService.create_story(story_dto)
    return jsonify(api_response(200,"Truyện đã được thêm thành công",data)), 200    

# Sửa truyện
@story_bp.route("/stories/<int:story_id>", methods=["PUT"])
def update_story(story_id):
    data = request.get_json()
    if not data:
        return jsonify(api_response(400, "Thiếu thông tin truyện")), 400
    story_dto = StoryUpdateDTO(**data) 
    StoryService.update_story(story_dto,story_id)
    return jsonify(api_response(200,"Truyện đã được sửa thành công",data)), 200    


# Xóa truyện
@story_bp.route("/stories/<int:story_id>", methods=["DELETE"])
def delete_story(story_id):
    deleted_story = StoryService.delete_story(story_id)
    print(f"Đã xóa truyện: {deleted_story}")
    if not deleted_story:
        return jsonify(api_response(404, "Không tìm thấy truyện")), 404
    return jsonify(api_response(200, "Truyện đã được xóa thành công",deleted_story)), 200
