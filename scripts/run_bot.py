import logging
import os

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import filters
from aiogram.types import BotCommand, KeyboardButton, ReplyKeyboardMarkup
from dotenv import load_dotenv

from scripts.color_graph import get_schedule

bot_token = 'bot_token'

load_dotenv()
API_TOKEN = os.getenv(bot_token)
if API_TOKEN is None:
    raise ValueError("API_TOKEN = None")

CURRENT_DPATH = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(CURRENT_DPATH, os.pardir))
DATA_DPATH = os.path.join(PROJECT_ROOT, "data")
CONFIG_DPATH = os.path.join(PROJECT_ROOT, "configs")
schedule_path = os.path.join(DATA_DPATH, 'timetable')
xlsx_path = os.path.join(schedule_path, 'schedule.xlsx')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Initialize keyboard
kb = ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True, resize_keyboard=True,)
yes_button = KeyboardButton(text='Да')
no_button = KeyboardButton(text='Нет')
kb.row(yes_button, no_button)


async def set_main_menu(*arg):
    main_menu_commands = [
        BotCommand(command="/start", description="Начало работы с ботом"),
        BotCommand(command="/help", description="Краткая справка про команды"),
        BotCommand(command="/generate_timetable", description="Запуск генерации расписания"),
    ]

    await bot.set_my_commands(main_menu_commands)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):

    """This handler will be called when user sends `/start` command"""

    await message.reply("Привет!\nЯ schedulebot!\nИ я очень люблю генерировать расписание!")


@dp.message_handler(commands=['help'])
async def send_command_list(message: types.Message):

    """This handler will be called when user sends `/help` command"""

    await message.reply("Вот список моих команд:\n/start\n/help\n/generate_timetable")


@dp.message_handler(commands=['generate_timetable'])
async def send_generate_timetable(message: types.Message):

    """This handler will be called when user sends `/generate_timetable` command"""

    schedule_path = os.path.join(DATA_DPATH, 'timetable')
    xlsx_path = os.path.join(schedule_path, 'schedule.xlsx')
    bool = os.path.isfile(xlsx_path)
    if bool is False:
        get_schedule()
    await message.reply("file ready")
    await message.answer("Вам нужен xlsx файл с расписанием?", reply_markup=kb)


@dp.message_handler(filters.Text(equals="Да"))
async def send_file(message: types.Message):

    """This handler will be called when user sends `/send` command"""

    with open(xlsx_path, "rb") as file:
        await message.reply_document(file)


@dp.message_handler(filters.Text(equals="Нет"))
async def dont_send_file(message: types.Message):

    """This handler will be called when user sends `/dont_send` command"""

    await message.reply('Может быть в следующий раз...')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=set_main_menu)
