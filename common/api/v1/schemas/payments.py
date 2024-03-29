from pydantic import BaseModel

from common.api.v1.schemas.entity import EntityDBSchema


class PaymentCreateSchema(BaseModel):
    card_number: str
    validity_month: int
    validity_year: int
    cvv_cvc: int
    amount: float


class PaymentDBSchema(PaymentCreateSchema, EntityDBSchema):
    user_id: int

    class Config:
        from_attributes = True
