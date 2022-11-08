import time
import logging

from aiogram import Bot, Dispatcher, executor, types


TOKEN = "5600127998:AAFwwbMLuAV_ONYpV7lpKEJx2ZDyPNqq7oA"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def start_hander(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_full_name = message.from_user.full_name
    logging.info(f'{user_id=} {user_full_name=} {time.asctime()}')
    await message.reply(f"Привет, {user_full_name}! Ти - пирожок!")

    for i in range(3):
        time.sleep(5)
        await bot.send_message(user_id, "Пирожок-муржожок!")



if __name__ == '__main__':
    executor.start_polling(dp)