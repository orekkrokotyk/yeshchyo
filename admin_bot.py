from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import InlineKeyboardBuilder

import asyncio

import static
import db_function

def admin_menu():
    buttons = [
            [types.InlineKeyboardButton(text='Меню', callback_data='Меню')],
            [types.InlineKeyboardButton(text='Заказы', callback_data='Заказы')]
        ]
        
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

class Admin(StatesGroup):
    pas = State()
    req_menu = State()

class Menu(StatesGroup):
    type = State()

bot = Bot(token="7898989327:AAHJWKTbd4LZ4XkHjiG3a5oyi2eeO4Dnf8k")
dp = Dispatcher()

@dp.message(Command(commands=['start', 'restart']))
async def start(message: Message):
    await message.answer("Добро пожаловать, если вы админ ввидите команду /admin")

@dp.message(Command('admin'))
async def admin_message(message: Message, state: FSMContext):
    await state.set_state(Admin.pas)
    await message.answer("Ввидите ключь")

@dp.message(Admin.pas)
async def check_admin(message: Message, state: FSMContext):
    if message.text == static.admin_key:
        await state.set_state(Admin.req_menu)

        await message.answer("Добро пожаловать на кухню", reply_markup=admin_menu())
    else:
        await message.answer("Хорошая попытка. Напишите команду /admin для ещё одной попытки или /restart если передумали")


@dp.callback_query(F.data == 'Меню', Admin.req_menu)
async def callback_query(callback: types.CallbackQuery, state: FSMContext):
    buttons = [
        [
            types.InlineKeyboardButton(text="Напиток🥤", callback_data="drink"),
            types.InlineKeyboardButton(text="Лапша 🥡", callback_data="noodle")
        ],
        [types.InlineKeyboardButton(text="Бургер 🍔", callback_data="burger")]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    await state.set_state(Menu.type)
    await callback.message.answer("Тутошние разделы меню", reply_markup=keyboard)
    await callback.answer()

@dp.callback_query(Menu.type)
async def callback_query(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer(db_function.element_menu(callback.data))

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)



if __name__ == "__main__":
    asyncio.run(main())