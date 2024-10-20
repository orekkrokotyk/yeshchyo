import telebot
from telebot import types
import main_bot
admin_key = "123"

bot = telebot.TeleBot("7898989327:AAHJWKTbd4LZ4XkHjiG3a5oyi2eeO4Dnf8k")

@bot.message_handler(commands=['start', 'restart'])
def start_message(message):
    bot.send_message(message.chat.id, f"""Добро пожаловать, если вы админ ввидите команду /admin""")


@bot.message_handler(commands=['admin'])
def admin_message(message):
    bot.send_message(message.chat.id, f"""Ввидите ключь""")
    bot.register_next_step_handler(message, check_admin)


def check_admin(message):
    if message.text == admin_key:
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton(text='Меню', callback_data='Меню'))
        markup.add(types.InlineKeyboardButton(text='Заказы', callback_data='Заказы'))

        bot.send_message(message.chat.id, f"""Добро пожаловать на кухню""", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, f"""Хорошая попытка. Напишите команду /admin для ещё одной попытки или /restart если передумали""")

@bot.callback_query_handler(func=lambda callback: callback.data)
def callback_query(callback):
    markup = types.InlineKeyboardMarkup(row_width=2)
    if callback.data == 'Меню':
        button1 = types.InlineKeyboardButton(text="Напиток🥤", callback_data="drink")
        button2 = types.InlineKeyboardButton(text="Лапша 🥡", callback_data="drink")
        button3 = types.InlineKeyboardButton(text="Бургер 🍔", callback_data="drink")
        markup.add(button1, button2)
        markup.add(button3)
        bot.send_message(callback.message.chat.id, "MENU", reply_markup=markup)

bot.infinity_polling()