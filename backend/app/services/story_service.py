
from unicodedata import category
from app.repositories.story_repository import StoryRepository
from app.dto.story_dto import StoryDTO, StoryUpdateDTO
from app.models import Story      
from app.repositories.category_repository import CategoryRepository
from app.services.s3_service import upload_file_to_s3
from app.config.logging_config import setup_logging
app_logger, _ = setup_logging()


class StoryService():

    @staticmethod
    def get_all_stories():
        app_logger.info("Lấy tất cả stories")
        return StoryRepository.get_all_stories()
    
    @staticmethod
    def get_story_by_id(story_id):
        app_logger.info(f"Lấy story với id={story_id}")
        return StoryRepository.get_story_by_id(story_id)    

    @staticmethod
    def create_story(story_dto: StoryDTO):
        app_logger.info(f"Tạo story mới: {story_dto.title}")
        story = Story(
            title=story_dto.title,
            description=story_dto.description,
            author=story_dto.author,
        )
        story.categories = CategoryRepository.get_category_objs_by_ids(story_dto.category_ids) # type: ignore
        return StoryRepository.create_story(story)
    
    @staticmethod
    def update_story(story_dto: StoryUpdateDTO,story_id):
        app_logger.info(f"Cập nhật story id={story_id}")
        story = Story(
            title=story_dto.title,
            description=story_dto.description,
            author=story_dto.author,
        )
        story.categories = CategoryRepository.get_category_objs_by_ids(story_dto.category_ids) # type: ignore
        return StoryRepository.update_story(story,story_id)
    
    @staticmethod
    def delete_story(story_id):
        app_logger.info(f"Xóa story id={story_id}")
        return StoryRepository.delete_story(story_id)

    @staticmethod
    def upload_image(file, story_id):
        if not file:
            app_logger.error("Không có file để upload")
            return None
        story = Story.query.get(story_id)
        if not story:   
            app_logger.error(f"Không tìm thấy story id={story_id}")
            return None
        app_logger.info(f"Bắt đầu upload ảnh cho story id={story_id}, filename={file.filename}")
        url = upload_file_to_s3(file, file.filename)
        if not url:
            app_logger.error(f"Upload ảnh thất bại cho story id={story_id}, filename={file.filename}")
            return None
        story.url_image = url  # type: ignore
        StoryRepository.update_story(story, story_id)  # type: ignore
        app_logger.info(f"Upload ảnh thành công cho story id={story_id}, url={url}")
        return url
