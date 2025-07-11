from app.repositories.chapter_repository import ChapterRepository
from app.dto.chapter_dto import ChapterDTO
from app.models import Chapter

class ChapterService:

    @staticmethod
    def get_all_chapters():
        return ChapterRepository.get_all_chapters()
    
    @staticmethod
    def get_chapter_by_id(chapter_id):
        return ChapterRepository.get_chapter_by_id(chapter_id)

    @staticmethod
    def create_chapter(chapter_dto: ChapterDTO):
        chapter = Chapter(
            title=chapter_dto.title,
            content=chapter_dto.content,
            story_id=chapter_dto.story_id
        )
        return ChapterRepository.create_chapter(chapter)
    
    @staticmethod
    def update_chapter(chapter_dto: ChapterDTO, chapter_id):
        chapter = Chapter(
            title=chapter_dto.title,
            content=chapter_dto.content,
            story_id=chapter_dto.story_id
        )
        return ChapterRepository.update_chapter(chapter, chapter_id)
    
    @staticmethod
    def delete_chapter(chapter_id):
        return ChapterRepository.delete_chapter(chapter_id)