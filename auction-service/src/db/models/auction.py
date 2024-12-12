import datetime
import uuid

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy.dialects.postgresql import UUID, SMALLINT

from db.models import Base


class Auction(Base):

    __tablename__ = "auctions"

    auction_id: Mapped[uuid.UUID] = mapped_column(
        UUID, primary_key=True, index=True,
    )
    number_of_slots: Mapped[int]
    entrance_ticket_price: Mapped[int] = mapped_column(
        SMALLINT,
    )
    location: Mapped[str]
    date: Mapped[datetime.datetime]
