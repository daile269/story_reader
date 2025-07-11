from pydantic import BaseModel

class StoryDTO(BaseModel):
    title: str
    description: str
    author: str

class StoryUpdateDTO(BaseModel):
    title: str
    description: str
    author: str 