from datetime import datetime

from pydantic import BaseModel, Field


class AuctionUpdateModel(BaseModel):
    number_of_slots: int | None = None
    entrance_ticket_price: int | None = None
    location: str | None = None


class AuctionCreateModel(BaseModel):
    number_of_slots: int = Field(..., ge=1)
    entrance_ticket_price: int = Field(..., ge=1)
    location: str = Field(..., max_length=255)
    date: datetime
