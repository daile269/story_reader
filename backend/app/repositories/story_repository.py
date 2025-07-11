from app.models import Story
from app.dto.story_dto import StoryDTO, StoryUpdateDTO
from app import db

class StoryRepository:
    @staticmethod
    def get_all_stories():
        stories = Story.query.all()
        result = []
        for s in stories:
            result.append({
            "id": s.id,
            "title": s.title,
            "description": s.description,
            "author": s.author,
            "chapters": [
                {
                    "id": c.id,
                    "title": c.title,
                    "content": c.content
                } for c in s.chapters
            ]
        })
        return result
    
    @staticmethod
    def get_story_by_id(story_id):
        story = Story.query.get(story_id)
        if not story: 
             return None 
        result = {
        "id": story.id,
        "title": story.title,
        "description": story.description,
        "author": story.author,
        "chapters": [
            {
                "id": c.id,
                "title": c.title,
                "content": c.content
            } for c in story.chapters
        ]
        
    }
        return result
    
    @staticmethod
    def create_story(story: Story):
        db.session.add(story)
        db.session.commit()
        return {
        "id": story.id,
        "title": story.title,
        "description": story.description,
        "author": story.author,
        "chapters": []
    }
    
    @staticmethod
    def update_story(storyUpdate: Story, story_id):
        story = Story.query.get(story_id)
        if not story: 
             return None
        story.title = storyUpdate.title
        story.description = storyUpdate.description
        story.author = storyUpdate.author
        db.session.commit()
        return {
        "id": story.id,
        "title": story.title,
        "description": story.description,
        "author": story.author,
        "chapters": [
            {
                "id": c.id,
                "title": c.title,
                "content": c.content
            } for c in story.chapters
        ]
    }
    
    @staticmethod
    def delete_story(story_id):
        story = Story.query.get(story_id)
        if not story: 
            return None
        # Lưu thông tin truyện trước khi xóa
        deleted_story = {
            "id": story.id,
            "title": story.title,
            "description": story.description,
            "author": story.author,
            "chapters": [
                {
                    "id": c.id,
                    "title": c.title,
                    "content": c.content
                } for c in story.chapters
            ]
        }
        db.session.delete(story)
        db.session.commit()
        return deleted_story
        