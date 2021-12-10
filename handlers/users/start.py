from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from states import states_bot
from loader import dp
from data import config
from keyboards.default import button_bot


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    
    if message.chat.id == int(config.ADMINS[0]):
        await message.answer(f"Здравствуйте админ, {message.from_user.full_name}!\n"+"Выберите дальнейшие действия.", reply_markup=button_bot.admin_menu)
        await states_bot.Admins_state.menu_button.set()
    else:
        await message.answer(f"Здравствуйте, {message.from_user.full_name}!\n"+"Выберите инетрисующую Вас ваканию:")
        await states_bot.Users_state.list_vacant.set()