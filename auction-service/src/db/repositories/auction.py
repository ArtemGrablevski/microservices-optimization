from datetime import datetime
from uuid import UUID

from sqlalchemy import select, insert, delete, update

from db.repositories.base import BaseDbRepository
from db.models import Auction


class AuctionRepository(BaseDbRepository):

    async def get_auction_by_id(self, auction_id: UUID) -> Auction | None:
        return await self.session.scalar(
            select(Auction)
            .where(Auction.auction_id == auction_id)
        )

    async def get_auctions(self, skip: int, limit: int) -> list[Auction]:
        auctions = await self.session.scalars(
            select(Auction)
            .offset(skip)
            .limit(limit)
        )
        return auctions.all()

    async def create_auction(
        self,
        auction_id: UUID,
        number_of_slots: int,
        entrance_ticket_price: int,
        location: str,
        date: datetime,
    ) -> Auction:
        return await self.session.scalar(
            insert(Auction)
            .values(
                auction_id=auction_id,
                number_of_slots=number_of_slots,
                entrance_ticket_price=entrance_ticket_price,
                location=location,
                date=date,
            )
            .returning(Auction)
        )

    async def update_auction_by_id(self, auction_id: UUID, **values_to_update) -> None:
        await self.session.execute(
            update(Auction)
            .where(Auction.auction_id == auction_id)
            .values(values_to_update)
        )

    async def delete_auction_by_id(
        self,
        auction_id: UUID,
    ) -> None:
        await self.session.execute(
            delete(Auction)
            .where(Auction.auction_id == auction_id)
        )
