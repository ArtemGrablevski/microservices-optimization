from fastapi import Depends
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

from api.dependencies.stubs import get_sessionmaker
from db.repositories import AuctionRepository
from services.auction import AuctionService


async def get_auction_service(
    sessionmaker: async_sessionmaker[AsyncSession] = Depends(get_sessionmaker),
):
    async with sessionmaker() as session:
        yield AuctionService(
            session=session,
            auction_repository=AuctionRepository(session),
        )
