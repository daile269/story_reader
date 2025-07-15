from app.repositories.category_repository import CategoryRepository
from app.dto.category_dto import CategoryDTO, CategoryUpdateDTO

class CategoryService:
    @staticmethod
    def get_all_categories():
        return CategoryRepository.get_all_categories()

    @staticmethod
    def get_category_by_id(category_id):
        return CategoryRepository.get_category_by_id(category_id)

    @staticmethod
    def create_category(category_dto: CategoryDTO):
        return CategoryRepository.create_category(category_dto)

    @staticmethod
    def update_category(category_update_dto: CategoryUpdateDTO, category_id):
        return CategoryRepository.update_category(category_update_dto, category_id)

    @staticmethod
    def delete_category(category_id):
        return CategoryRepository.delete_category(category_id)
