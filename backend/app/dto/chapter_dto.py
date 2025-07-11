from pydantic import BaseModel

class ChapterDTO(BaseModel):
    title: str
    content: str
    story_id: int

class ChapterUpdateDTO(BaseModel):
    title: str
    content: str
    story_id: int
