import logging

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

from config import TOKEN

# Настройка параметров
storage = MemoryStorage()
bot = Bot(token=TOKEN)
dp = Dispatcher(storage=storage)

# Ввод данных для кнопок
sites = [
    ("Google", "https://www.google.com/"),
]

# Клавиатура
keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text=name, web_app=WebAppInfo(url=url))] for name, url in sites
    ]
)


# Обработчик команды /start1
@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("Текст", reply_markup=keyboard)


# Основной блок
if __name__ == "__main__":
    # Настройка логирования
    logging.basicConfig(level=logging.INFO)

    # Запуск бота
    dp.run_polling(bot, skip_updates=True)
