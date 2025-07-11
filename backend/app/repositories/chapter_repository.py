from app.models import Chapter
from app import db
from app.repositories.story_repository import StoryRepository

class ChapterRepository:
    @staticmethod
    def get_all_chapters():
        chapters = Chapter.query.all()
        result = []
        for c in chapters:
            result.append({
                "id": c.id,
                "title": c.title,
                "content": c.content,
                "story_id": c.story_id
            })
        return result

    @staticmethod
    def get_chapter_by_id(chapter_id):
        chapter = Chapter.query.get(chapter_id)
        if not chapter:
            return None
        return {
            "id": chapter.id,
            "title": chapter.title,
            "content": chapter.content,
            "story_id": chapter.story_id
        }

    @staticmethod
    def create_chapter(chapter: Chapter):
        story = StoryRepository.get_story_by_id(chapter.story_id)
        if not story:
            return None
        db.session.add(chapter)
        db.session.commit()
        return {
            "id": chapter.id,
            "title": chapter.title,
            "content": chapter.content,
            "story_id": chapter.story_id
        }

    @staticmethod
    def update_chapter(chapterUpdate: Chapter, chapter_id):
        chapter = Chapter.query.get(chapter_id)
        if not chapter:
            return None
        chapter.title = chapterUpdate.title
        chapter.content = chapterUpdate.content
        chapter.story_id = chapterUpdate.story_id
        db.session.commit()
        return {
            "id": chapter.id,
            "title": chapter.title,
            "content": chapter.content,
            "story_id": chapter.story_id
        }

    @staticmethod
    def delete_chapter(chapter_id):
        chapter = Chapter.query.get(chapter_id)
        if not chapter:
            return None
        deleted_chapter = {
            "id": chapter.id,
            "title": chapter.title,
            "content": chapter.content,
            "story_id": chapter.story_id
        }
        db.session.delete(chapter)
        db.session.commit()
        return deleted_chapter