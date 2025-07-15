from app.repositories.chapter_repository import ChapterRepository
from app.dto.chapter_dto import ChapterDTO
from app.models import Chapter
from app.config.logging_config import setup_logging
app_logger, _ = setup_logging()

class ChapterService:

    @staticmethod
    def get_all_chapters():
        app_logger.info("Lấy tất cả chapters")
        return ChapterRepository.get_all_chapters()
    
    @staticmethod
    def get_chapter_by_id(chapter_id):
        app_logger.info(f"Lấy chapter với id={chapter_id}")
        return ChapterRepository.get_chapter_by_id(chapter_id)

    @staticmethod
    def create_chapter(chapter_dto: ChapterDTO):
        app_logger.info(f"Tạo chapter mới: {chapter_dto.title}")
        chapter = Chapter(
            title=chapter_dto.title,
            content=chapter_dto.content,
            story_id=chapter_dto.story_id
        )
        return ChapterRepository.create_chapter(chapter)
    
    @staticmethod
    def update_chapter(chapter_dto: ChapterDTO, chapter_id):
        app_logger.info(f"Cập nhật chapter id={chapter_id}")
        chapter = Chapter(
            title=chapter_dto.title,
            content=chapter_dto.content,
            story_id=chapter_dto.story_id
        )
        return ChapterRepository.update_chapter(chapter, chapter_id)
    
    @staticmethod
    def delete_chapter(chapter_id):
        app_logger.info(f"Xóa chapter id={chapter_id}")
        return ChapterRepository.delete_chapter(chapter_id)