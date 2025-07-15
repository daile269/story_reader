
from unicodedata import category
from app.repositories.story_repository import StoryRepository
from app.dto.story_dto import StoryDTO, StoryUpdateDTO
from app.models import Story      
from app.repositories.category_repository import CategoryRepository

class StoryService():

    @staticmethod
    def get_all_stories():
        return StoryRepository.get_all_stories()
    
    @staticmethod
    def get_story_by_id(story_id):
        return StoryRepository.get_story_by_id(story_id)    

    @staticmethod
    def create_story(story_dto: StoryDTO):
        story = Story(
            title=story_dto.title,
            description=story_dto.description,
            author=story_dto.author,
        )
        story.categories = CategoryRepository.get_category_objs_by_ids(story_dto.category_ids) # type: ignore
        return StoryRepository.create_story(story)
    
    @staticmethod
    def update_story(story_dto: StoryUpdateDTO,story_id):
        story = Story(
            title=story_dto.title,
            description=story_dto.description,
            author=story_dto.author,
        )
        story.categories = CategoryRepository.get_category_objs_by_ids(story_dto.category_ids) # type: ignore
        return StoryRepository.update_story(story,story_id)
    
    @staticmethod
    def delete_story(story_id):
        return StoryRepository.delete_story(story_id)
