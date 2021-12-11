from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from states import states_bot
from loader import dp
from data import config
from keyboards.default import button_bot
from utils.db_api import API_INSERT_DB

@dp.message_handler(CommandStart(),state="*")
async def bot_start(message: types.Message):
    
    if message.chat.id == int(config.ADMINS[0]):
        print(button_bot.administrator_actions)
        await message.answer(f"Здравствуйте админ, {message.from_user.full_name}!\n"+"Выберите дальнейшие действия.", reply_markup=button_bot.add_button(button_bot.administrator_actions))
        await states_bot.Admins_state.menu_button.set()
    else:
        API_INSERT_DB.insert_id(message.chat.id)
        await message.answer(f"Здравствуйте, {message.from_user.full_name}!\n"+"Компания Цифровая Лаборатория - Продуктовая IT компания. Мы поддерживаем и помогаем нашим сотрудникам развиваться на любом карьерном этапе. Работа в Цифровой Лаборатории — 1001 возможность для тебя!\nВыберите инетрисующую Вас ваканию:", reply_markup=button_bot.vacant_list)
        await states_bot.Users_state.list_vacant.set()