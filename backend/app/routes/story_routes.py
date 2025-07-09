from flask import Blueprint, jsonify, request   
from ..models import Story
from .. import db

story_bp = Blueprint("story", __name__)

@story_bp.route("/stories", methods=["GET"])
def get_stories():
    stories = Story.query.all()
    result = []
    for s in stories:
        result.append({
            "id": s.id,
            "title": s.title,
            "description": s.description,
            "author": s.author
        })
    return jsonify(result)

@story_bp.route("/stories/<int:story_id>", methods=["GET"])
def get_story_detail(story_id):
    story = Story.query.get_or_404(story_id)
    chapters = [{"id": c.id, "title": c.title} for c in story.chapters]
    return jsonify({
        "id": story.id,
        "title": story.title,
        "description": story.description,
        "author": story.author,
        "chapters": chapters
    })

# Thêm truyện
@story_bp.route("/stories", methods=["POST"])
def add_story():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Missing or invalid JSON body"}), 400
    new_story = Story(
        title=data.get("title"),
        description=data.get("description"),
        author=data.get("author")
    )
    db.session.add(new_story)
    db.session.commit()
    return jsonify({"message": "Truyện đã được thêm thành công"}), 201

# Sửa truyện
@story_bp.route("/stories/<int:story_id>", methods=["PUT"])
def update_story(story_id):
    data = request.get_json()
    if not data:
        return jsonify({"error": "Missing or invalid JSON body"}), 400
    story = Story.query.get_or_404(story_id)
    story.title = data.get("title")
    story.description = data.get("description")
    story.author = data.get("author")
    db.session.commit()
    return jsonify({"message": "Truyện đã được cập nhật thành công"}), 200

# Xóa truyện
@story_bp.route("/stories/<int:story_id>", methods=["DELETE"])
def delete_story(story_id):
    story = Story.query.get_or_404(story_id)
    db.session.delete(story)
    db.session.commit()
    return jsonify({"message": "Truyện đã được xóa thành công"}), 200


# Sửa truyện    