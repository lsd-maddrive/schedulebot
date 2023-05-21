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


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):

    """This handler will be called when user sends `/start` command"""

    await message.reply("Привет!\nЯ schedulebot!\nИ я очень люблю генерировать расписание!")


@dp.message_handler(commands=['help'])
async def send_command_list(message: types.Message):

    """This handler will be called when user sends `/help` command"""

    await message.reply("Вот список моих команд:\n/start\n/help\n/support")


if __name__ == '__main__':

    executor.start_polling(dp, skip_updates=True)
