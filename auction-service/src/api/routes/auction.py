from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Query
from starlette import status

from api.dependencies.db import get_auction_service
from exceptions.auction import AuctionDoesNotExistError
from models.auction import AuctionCreateModel, AuctionUpdateModel
from services.auction import AuctionService


router = APIRouter(
    tags=["Auctions"], prefix="/api/auctions"
)


@router.get("", status_code=status.HTTP_200_OK)
async def get_all_auctions(
    skip: int = Query(0),
    limit: int = Query(30),
    auction_service: AuctionService = Depends(get_auction_service),
):
    return await auction_service.get_all_auctions(
        skip=skip,
        limit=limit,
    )


@router.get("/{auction_id}", status_code=status.HTTP_200_OK)
async def get_auction_by_id(
    auction_id: UUID,
    auction_service: AuctionService = Depends(get_auction_service),
):
    try:
        return await auction_service.get_auction_by_id(
            auction_id=auction_id,
        )
    except AuctionDoesNotExistError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Auction with id = {str(auction_id)} does not exist"
        )


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_auction(
    auction: AuctionCreateModel,
    auction_service: AuctionService = Depends(get_auction_service),
):
    await auction_service.create_auction(
        number_of_slots=auction.number_of_slots,
        entrance_ticket_price=auction.entrance_ticket_price,
        location=auction.location,
        date=auction.date,
    )
    return {"success": True}


@router.put("/{auction_id}", status_code=status.HTTP_200_OK)
async def update_auction_by_id(
    auction_id: UUID,
    auction: AuctionUpdateModel,
    auction_service: AuctionService = Depends(get_auction_service),
):
    try:
        await auction_service.update_auction_by_id(
            auction_id=auction_id,
            auction=auction,
        )
    except AuctionDoesNotExistError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Auction with id = {str(auction_id)} does not exist"
        )
    return {"success": True}


@router.delete("/{auction_id}", status_code=status.HTTP_200_OK)
async def delete_auction_by_id(
    auction_id: UUID,
    auction_service: AuctionService = Depends(get_auction_service),
):
    try:
        await auction_service.delete_auction_by_id(
            auction_id=auction_id,
        )
    except AuctionDoesNotExistError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Auction with id = {str(auction_id)} does not exist"
        )
    return {"success": True}
