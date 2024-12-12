from fastapi import APIRouter
from starlette import status

from models import NotificationCreateModel
from notification_manager import NotifictionManager


router = APIRouter(
    tags=["Notifications"], prefix="/api/notifications"
)

notification_mngr = NotifictionManager()


@router.post("", status_code=status.HTTP_200_OK)
async def create_notification(
    notification: NotificationCreateModel,
):
    await notification_mngr.send_message(
        message=notification.message,
    )
    return {"success": True}
