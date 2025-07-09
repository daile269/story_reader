from flask import Blueprint, jsonify
from ..models import Chapter
from .. import db

chapter_bp = Blueprint("chapter", __name__)

@chapter_bp.route("/chapters/<int:chapter_id>", methods=["GET"])
def get_chapter(chapter_id):
    chapter = Chapter.query.get_or_404(chapter_id)
    return jsonify({
        "id": chapter.id,
        "title": chapter.title,
        "content": chapter.content,
        "story_id": chapter.story_id
    })
