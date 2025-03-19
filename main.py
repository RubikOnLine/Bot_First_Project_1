import config
import  logging

from aiogram import Bot, Dispatcher, F

import asyncio

from handlers import common

# Запуск процесса поллинга новых апдейтов
async def main():
    TOKEN_API = config.TOKEN_TG

    # Включаем логирование
    logging.basicConfig(level=logging.INFO)

    # Инициализируем бота и диспетчера
    bot = Bot(token=TOKEN_API)
    # Диспетчер
    dp = Dispatcher()

    # Регистрируем хендлеры
    dp.include_router(common.router)

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
