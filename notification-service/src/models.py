from pydantic import BaseModel


class NotificationCreateModel(BaseModel):
    message: str
