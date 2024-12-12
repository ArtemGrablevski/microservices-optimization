import asyncio


class NotifictionManager:

    async def send_message(self, message: str) -> None:
        print(message)
        await asyncio.sleep(0.25)
