from pydantic import BaseModel

class StoryDTO(BaseModel):
    title: str
    description: str
    author: str
    category_ids: list[int]
class StoryUpdateDTO(BaseModel):
    title: str
    description: str
    author: str
    category_ids: list[int]