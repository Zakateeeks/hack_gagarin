from loguru import logger
from aiogram import executor
import asyncio

from TelegramBot.bot_configure import dp
from handlers import start


def main() -> None:
    start.start_handler(dp)


if __name__ == "__main__":
    main()
    logger.success('start')
    loop = asyncio.get_event_loop()

    executor.start_polling(dp, loop=dp.loop)
