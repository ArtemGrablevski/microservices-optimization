from datetime import datetime
from uuid import UUID, uuid4

from faststream.rabbit import RabbitBroker
from sqlalchemy.ext.asyncio import AsyncSession

from db.models import Auction
from db.repositories import AuctionRepository
from exceptions.auction import AuctionDoesNotExistError
from models.auction import AuctionUpdateModel


class AuctionService:

    def __init__(
        self,
        session: AsyncSession,
        auction_repository: AuctionRepository,
        message_broker: RabbitBroker,
    ) -> None:
        self.session = session
        self.auction_repository = auction_repository
        self.message_broker = message_broker

    async def get_all_auctions(self, skip: int, limit: int) -> list[Auction]:
        return await self.auction_repository.get_auctions(
            skip=skip,
            limit=limit,
        )

    async def get_auction_by_id(self, auction_id: UUID) -> Auction:

        auction = await self.auction_repository.get_auction_by_id(
            auction_id=auction_id,
        )
        if auction is None:
            raise AuctionDoesNotExistError()

        return auction

    async def create_auction(
        self,
        number_of_slots: int,
        entrance_ticket_price: int,
        location: str,
        date: datetime,
    ) -> None:

        auction_id = uuid4()

        await self.auction_repository.create_auction(
            auction_id=auction_id,
            number_of_slots=number_of_slots,
            entrance_ticket_price=entrance_ticket_price,
            location=location,
            date=date
        )

        message = f"New aution was created: {date=}, {number_of_slots=}, {entrance_ticket_price=}"
        # TODO: move queue name to config
        await self.message_broker.publish(
            message=message,
            queue="rabbitmq_notifications_queue",
        )

        await self.session.commit()

    async def update_auction_by_id(
        self,
        auction_id: UUID,
        auction: AuctionUpdateModel,
    ) -> None:

        values_to_update = auction.model_dump(
            exclude_none=True,
            exclude_unset=True,
        )
        if not values_to_update:
            return
        
        existing_auction = await self.auction_repository.get_auction_by_id(
            auction_id=auction_id,
        )
        if existing_auction is None:
            raise AuctionDoesNotExistError()

        await self.auction_repository.update_auction_by_id(
            auction_id=auction_id,
            **values_to_update
        )

        await self.session.commit()

    async def delete_auction_by_id(
        self,
        auction_id: UUID,
    ) -> None:

        existing_auction = await self.auction_repository.get_auction_by_id(
            auction_id=auction_id,
        )
        if existing_auction is None:
            raise AuctionDoesNotExistError()

        await self.auction_repository.delete_auction_by_id(
            auction_id=auction_id,
        )

        await self.session.commit()
