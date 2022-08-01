# --*-- encoding: utf-8 --*--
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ContentType, Message
from aiogram_dialog import DialogManager, ChatEvent
from aiogram_dialog.widgets.kbd import Checkbox, ManagedCheckboxAdapter
from aiogram_dialog.widgets.text import Const

API_TOKEN = '5342176536:AAEknzzBVOeMu31IaPUogLs-98cpDFnPjYA'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(content_types=[ContentType.NEW_CHAT_MEMBERS])
async def new_members_handler(message: Message):
    new_member = message.new_chat_members[0]
    await bot.send_message(message.chat.id, f"Добро пожаловать, {new_member.mention}")

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Hello world!")


@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    await message.reply("Чем я могу помочь?")


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)