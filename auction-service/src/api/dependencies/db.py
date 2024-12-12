from fastapi import Depends
from faststream.rabbit import RabbitBroker
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

from api.dependencies.stubs import get_sessionmaker, get_message_broker
from db.repositories import AuctionRepository
from services.auction import AuctionService


async def get_auction_service(
    sessionmaker: async_sessionmaker[AsyncSession] = Depends(get_sessionmaker),
    message_broker: RabbitBroker = Depends(get_message_broker),
):
    async with sessionmaker() as session:
        yield AuctionService(
            session=session,
            auction_repository=AuctionRepository(session),
            message_broker=message_broker,
        )
