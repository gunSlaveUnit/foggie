from pydantic import BaseModel

from common.api.v1.schemas.entity import EntityDBSchema


class ReviewCreateSchema(BaseModel):
    content: str
    is_game_recommended: bool
    language_id: int


class ReviewDBSchema(ReviewCreateSchema, EntityDBSchema):
    user_id: int
    game_id: int

    class Config:
        from_attributes = True
