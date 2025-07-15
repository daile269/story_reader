from app.models import Category
from app import db
from app.dto.category_dto import CategoryDTO, CategoryUpdateDTO
    
class CategoryRepository:
    @staticmethod
    def get_all_categories():
        categories = Category.query.all()
        result = []
        for c in categories:
            result.append({
                "id": c.id,
                "name": c.name
            })
        return result

    @staticmethod
    def get_category_by_id(category_id):
        category = Category.query.get(category_id)
        if not category:
            return None
        return {
            "id": category.id,
            "name": category.name
        }

    @staticmethod
    def create_category(category_dto: CategoryDTO):
        category = Category(name=category_dto.name)
        db.session.add(category)
        db.session.commit()
        return {
            "id": category.id,
            "name": category.name
        }

    @staticmethod
    def update_category(category_update_dto: CategoryUpdateDTO, category_id):
        category = Category.query.get(category_id)
        if not category:
            return None
        category.name = category_update_dto.name
        db.session.commit()
        return {
            "id": category.id,
            "name": category.name
        }

    @staticmethod
    def delete_category(category_id):
        category = Category.query.get(category_id)
        if not category:
            return None
        deleted_category = {
            "id": category.id,
            "name": category.name
        }
        db.session.delete(category)
        db.session.commit()
        return deleted_category
    
    @staticmethod
    def get_category_objs_by_ids(category_ids: list[int]) -> list[Category]:
        categories = Category.query.filter(Category.id.in_(category_ids)).all()
        if len(categories) != len(category_ids):
            raise ValueError("Một hoặc nhiều category không tồn tại")
        return categories