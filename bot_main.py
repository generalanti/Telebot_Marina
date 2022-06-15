# --*-- encoding: utf-8 --*--

import config
import telebot
from telebot import types
import random

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start', 'end'])
def start(message):
    bot.send_message(message.chat.id, '<b>Тексты с описанием товара и тезисы для инфографики</b>', parse_mode="HTML")
    bot.send_message(message.chat.id, 'Утп (если есть)\nкраткое описание, главные преимущества, состав, материалы и прочая важная информация о товаре')



bot.polling(none_stop=True)