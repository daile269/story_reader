from app.models import Story, Category  
from app.dto.story_dto import StoryDTO, StoryUpdateDTO
from app import db
from app.repositories.category_repository import CategoryRepository 
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
            "url_image": s.url_image,
            "view_count": s.view_count,
            "created_at": s.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            "chapters": [
                {
                    "id": c.id,
                    "title": c.title,
                    "content": c.content
                } for c in s.chapters
            ],
            "categories": [
                {
                    "id": c.id,
                    "name": c.name
                } for c in s.categories 
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
        "url_image": story.url_image,
        "view_count": story.view_count,
        "created_at": story.created_at.strftime("%Y-%m-%d %H:%M:%S"),
        "chapters": [
            {
                "id": c.id,
                "title": c.title,
                "content": c.content
            } for c in story.chapters
        ],
        "categories": [
            {
                "id": c.id,
                "name": c.name
            } for c in story.categories # type: ignore  
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
        "view_count": story.view_count,
        "created_at": story.created_at.strftime("%Y-%m-%d %H:%M:%S"),
        "chapters": [],
        "categories": [
            {
                "id": c.id,
                "name": c.name
            } for c in story.categories # type: ignore
        ]
    }
    
    @staticmethod
    def update_story(storyUpdate: Story, story_id):
        story = Story.query.get(story_id)
        if not story: 
             return None
        story.title = storyUpdate.title
        story.description = storyUpdate.description
        story.author = storyUpdate.author   
        story.categories = storyUpdate.categories # type: ignore
        db.session.commit()
        return {
        "id": story.id,
        "title": story.title,
        "description": story.description,
        "author": story.author,
        "view_count": story.view_count,
        "created_at": story.created_at.strftime("%Y-%m-%d %H:%M:%S"),
        "chapters": [
            {
                "id": c.id,
                "title": c.title,
                "content": c.content
            } for c in story.chapters
        ],
        "categories": [
            {
                "id": c.id,
                "name": c.name
            } for c in story.categories # type: ignore
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
            "view_count": story.view_count,
            "created_at": story.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            "chapters": [
                {
                    "id": c.id,
                    "title": c.title,
                    "content": c.content
                } for c in story.chapters
            ],
            "categories": [
                {
                    "id": c.id,
                    "name": c.name
                } for c in story.categories # type: ignore
            ]
        }
        db.session.delete(story)
        db.session.commit()
        return deleted_story
        

# Get 16 stories with the most view_count
    @staticmethod
    def get_16_stories_with_most_view_count():
        stories = Story.query.order_by(Story.view_count.desc()).limit(16).all()
        result = []
        for s in stories:
            result.append({
            "id": s.id,
            "title": s.title,
            "description": s.description,
            "author": s.author,
            "url_image": s.url_image,
            "view_count": s.view_count,
            "created_at": s.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            "chapters": [
                {
                    "id": c.id,
                    "title": c.title,
                    "content": c.content
                } for c in s.chapters
            ],
            "categories": [
                {
                    "id": c.id,
                    "name": c.name
                } for c in s.categories 
            ]
        })
        return result

# Get 16 stories with the created_at most recent
    @staticmethod
    def get_16_stories_with_created_at_most_recent():
        stories = Story.query.order_by(Story.created_at.desc()).limit(16).all()
        result = []
        for s in stories:
            result.append({
                "id": s.id,
                "title": s.title,
                "description": s.description,
                "author": s.author,
                "url_image": s.url_image,
                "view_count": s.view_count,
                "created_at": s.created_at.strftime("%Y-%m-%d %H:%M:%S"),
                "chapters": [
                    {
                        "id": c.id,
                        "title": c.title,
                        "content": c.content
                    } for c in s.chapters
                ],
                "categories": [
                    {
                        "id": c.id,
                        "name": c.name
                    } for c in s.categories
                ]
            })
        return result
#Top 16 stories translate
    @staticmethod
    def get_16_stories_with_translate():
        stories = Story.query.filter(Story.categories.any(name="Dịch")).order_by(Story.view_count.desc()).limit(16).all()
        result = []
        for s in stories:
            result.append({
                "id": s.id,
                "title": s.title,   
                "description": s.description,
                "author": s.author,
                "url_image": s.url_image,
                "view_count": s.view_count,
                "created_at": s.created_at.strftime("%Y-%m-%d %H:%M:%S"),
                "chapters": [
                    {
                        "id": c.id,
                        "title": c.title,
                        "content": c.content
                    } for c in s.chapters
                ],
                "categories": [
                    {
                        "id": c.id,
                        "name": c.name
                    } for c in s.categories
                ]
            })
        return result

