# --*-- encoding: utf-8 --*--

import config
import telebot
import emoji
from telebot import types

bot = telebot.TeleBot(config.TOKEN)



@bot.message_handler(commands=['start'])
def cmd_start(message):
    markup = types.InlineKeyboardMarkup()
    btn_my_site = types.InlineKeyboardButton(text="Нажми меня", url='https://forms.gle/e6h2suKgn4LgWV6g7')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id,
                     "Пожалуйста, заполните <b>техническое задание\nна разработку дизайна карточек товара</b> по ссылке:",
                     parse_mode="HTML", reply_markup=markup)




bot.polling(none_stop=True)
