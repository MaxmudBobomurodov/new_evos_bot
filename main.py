from asyncio import run
import logging
from aiogram import Bot,Dispatcher
from aiogram.client.default import DefaultBotProperties

from core.config import TOKEN
from core.table_queries import initializing_tables
from utils.commands import set_my_commands
from routers import register, feedback

async def startup_answer(bot : Bot):
    initializing_tables()
    await set_my_commands(bot)
    await bot.send_message(5894214924 , "bot ishga tushdi✅")

async def ending_answer(bot : Bot):
    await bot.send_message(5894214924, "bot ishdan tuxtadi❌")




async def main():
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
    dp = Dispatcher()
    dp.include_router(router=register.router)
    dp.include_router(router=feedback.router)


    dp.startup.register(startup_answer)
    dp.shutdown.register(ending_answer)



    await dp.start_polling(bot, polling_timeout=0)



if __name__ == '__main__':
    logging.basicConfig(
        format="[%(asctime)s] - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.INFO
    )
    logging.getLogger("aiogram.event").setLevel(logging.WARNING)
    run(main())