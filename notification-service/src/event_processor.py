from faststream import FastStream
from faststream.rabbit import RabbitBroker

from config import Settings
from notification_manager import NotifictionManager


config = Settings()

broker = RabbitBroker(
    f"amqp://{config.rabbitmq_user}:{config.rabbitmq_password}"
    f"@{config.rabbitmq_host}:{config.rabbitmq_port}/"
)

app = FastStream(broker)

notification_mngr = NotifictionManager()


@broker.subscriber(queue="rabbitmq_notifications_queue")
async def notification_listener(message: str) -> None:
    print(message)
    await notification_mngr.send_message(
        message=message,
    )
