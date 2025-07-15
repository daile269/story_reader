from pydantic import BaseModel

class CategoryDTO(BaseModel):
    name: str

class CategoryUpdateDTO(BaseModel):
    name: str