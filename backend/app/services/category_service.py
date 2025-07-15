from app.repositories.category_repository import CategoryRepository
from app.dto.category_dto import CategoryDTO, CategoryUpdateDTO
from app.config.logging_config import setup_logging
app_logger, _ = setup_logging()

class CategoryService:
    @staticmethod
    def get_all_categories():
        app_logger.info("Lấy tất cả categories")
        return CategoryRepository.get_all_categories()

    @staticmethod
    def get_category_by_id(category_id):
        app_logger.info(f"Lấy category với id={category_id}")
        return CategoryRepository.get_category_by_id(category_id)

    @staticmethod
    def create_category(category_dto: CategoryDTO):
        app_logger.info(f"Tạo category mới: {category_dto.name}")
        return CategoryRepository.create_category(category_dto)

    @staticmethod
    def update_category(category_update_dto: CategoryUpdateDTO, category_id):
        app_logger.info(f"Cập nhật category id={category_id}")
        return CategoryRepository.update_category(category_update_dto, category_id)

    @staticmethod
    def delete_category(category_id):
        app_logger.info(f"Xóa category id={category_id}")
        return CategoryRepository.delete_category(category_id)
