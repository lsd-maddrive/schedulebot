import logging
import os

from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv

bot_token = 'bot_token'

load_dotenv()
API_TOKEN = os.getenv(bot_token)
if API_TOKEN is None:
    raise ValueError("API_TOKEN = None")

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['support', 'help'])
async def send_welcome(message: types.Message):

    """This handler will be called when user sends `/support` or `/help` command"""

    await message.reply("Привет!\nЯ schedulebot!\nИ я очень люблю генерировать расписание!")


if __name__ == '__main__':

    executor.start_polling(dp, skip_updates=True)
