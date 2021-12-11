from aiogram import types
from aiogram.dispatcher.filters import state
from loader import dp
from aiogram.dispatcher import FSMContext

from states import states_bot
from keyboards.default import button_bot
from utils.db_api import API_INSERT_DB


@dp.message_handler(state=states_bot.Users_state.list_vacant, content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
    if message.text in button_bot.vacant_mass:
        API_INSERT_DB.insert_post(message.chat.id, message.text)
        state = await state.get_state()
        await message.answer('Спасибо за ответ!\nЗаполните превичное резюме для передачи его в приемную комиссию.')
        await message.answer('Введите Ваше ФИО\nНапример(Иванов Иван Иванович)')
        await states_bot.Users_state.fio.set()

@dp.message_handler(state=states_bot.Users_state.fio, content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
    API_INSERT_DB.insert_FIO(message.chat.id, message.text)
    state = await state.get_state()
    await message.answer(f'{message.text}, напишите пожалуйта город в каком хотели бы работать.\nНапример(Москва/Сакнкт-Петербург/Екатеринбург)')
    await message.answer(f"Эхо в состоянии <code>{state}</code>.\n")
    await states_bot.Users_state.city.set()

@dp.message_handler(state=states_bot.Users_state.city, content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
    API_INSERT_DB.insert_pmg(message.chat.id, message.text)
    state = await state.get_state()
    await message.answer(f'{message.text}...\nБыл там на днях)\nТеперь напишите дату рождения.\nНапример(01.01.2000)')
    await message.answer(f"Эхо в состоянии <code>{state}</code>.\n")
    await states_bot.Users_state.date_birth.set()

@dp.message_handler(state=states_bot.Users_state.date_birth, content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
    API_INSERT_DB.insert_Age(message.chat.id, message.text)
    state = await state.get_state()
    await message.answer(f'{message.text}, красивая дата, помню ее как вчера...\nУкажите Ваш пол:?', reply_markup=button_bot.sex)
    await message.answer(f"Эхо в состоянии <code>{state}</code>.\n")
    await states_bot.Users_state.sex.set()

@dp.message_handler(state=states_bot.Users_state.sex, content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
    if message.text in button_bot.sex_mass:
        if message.text == button_bot.sex_mass[0]:
            API_INSERT_DB.insert_Age(message.chat.id, 1)
        else:
            API_INSERT_DB.insert_Age(message.chat.id, 0)
        state = await state.get_state()
        await message.answer(f'{message.text}, ок.\nГражданином какой страны Вы являетесь?\nНапример(Российская Федерация/Узбекистан/казахстан)')
        await message.answer(f"Эхо в состоянии <code>{state}</code>.\n")
        await states_bot.Users_state.citizenship.set()

@dp.message_handler(state=states_bot.Users_state.citizenship, content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
    API_INSERT_DB.insert_cityzenship(message.chat.id, message.text)
    state = await state.get_state()
    await message.answer(f'{message.text}, понял.\nБыл ли у Вас опыт работы в данной сфере, если был то сколько лет?\nНапример(5 лет/-)')
    await message.answer(f"Эхо в состоянии <code>{state}</code>.\n")
    await states_bot.Users_state.experience.set()

@dp.message_handler(state=states_bot.Users_state.experience, content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
    API_INSERT_DB.insert_experience(message.chat.id, message.text)
    state = await state.get_state()
    await message.answer(f'{message.text}, понятно.\nТип занятости:', reply_markup=button_bot.work_time)
    await message.answer(f"Эхо в состоянии <code>{state}</code>.\n")
    await states_bot.Users_state.time_type.set()


@dp.message_handler(state=states_bot.Users_state.time_type, content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
    if message.text in button_bot.type_work_time:
        API_INSERT_DB.insert_employment(message.chat.id, message.text)
        state = await state.get_state()
        await message.answer(f'{message.text}, понятно.\nЕсть ли у вас навыки о которых мы должны знать?\nНапример(Когда-то разработал telegram...)')
        await message.answer(f"Эхо в состоянии <code>{state}</code>.\n")
        await states_bot.Users_state.skills.set()

@dp.message_handler(state=states_bot.Users_state.skills, content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
    API_INSERT_DB.insert_skills(message.chat.id, message.text)
    state = await state.get_state()
    await message.answer(f'Приму это к сведению.\nЕсли есть какая-то сылка на ваши достижения или портфолио, отправьте его пожалуйста.\nНапример(https://rainforce.spb.ru/)')
    await message.answer(f"Эхо в состоянии <code>{state}</code>.\n")
    await states_bot.Users_state.link.set()


@dp.message_handler(state=states_bot.Users_state.link, content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
    API_INSERT_DB.insert_portfolio(message.chat.id, message.text)
    state = await state.get_state()
    await message.answer(f'Хотите ли пройти входное тестирование по данному напрвлению?\nПо этому тетстированию мы поймем Вашу пригодноть к нашему рабочему месту.\nПри успешном прохождении тестирования мы свяжемся в Вами в ближайшее время)', reply_markup=button_bot.end_of_form_filling)
    await message.answer(f"Эхо в состоянии <code>{state}</code>.\n")
    await states_bot.Users_state.send_application_or_testing.set()
    if message.text == button_bot.end_of_form[0]:
        await message.answer(f"Оставить заявку повторно вы сможите оставить через неделю или пройдите входное тестирование.", reply_markup=button_bot.restart_or_test)
        await states_bot.Users_state.send_application_or_testing.set()
    elif message.text == button_bot.end_of_form[1]:
        await message.answer(f"Удачи на тестировании!!!")
        #############################НАЧАЛО ТЕСТА##########################


@dp.message_handler(state=states_bot.Users_state.send_application_or_testing, content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
    state = await state.get_state()
    await message.answer(f"Эхо в состоянии <code>{state}</code>.\n")
    if message.text == button_bot.end_of_form[0]:
        await message.answer(f"Оставить заявку повторно вы сможите оставить через неделю или пройдите входное тестирование.", reply_markup=button_bot.restart_or_test)
        await states_bot.Users_state.send_application_or_testing.set()
    elif message.text == button_bot.end_of_form[1]:
        await message.answer(f"Удачи на тестировании!!!")
        #############################НАЧАЛО ТЕСТА##########################
    # if message.text == button_bot.restart_test[0]:
    #     pass
    #     ###############ПРОВЕРКА В БД ДАТЫ ПОЛЕДНЕГО ЗАПОЛНЕНИЯ ФОРМЫ###################
    # elif message.text == button_bot.restart_test[1]:
    #     await message.answer(f"Удачи на тестировании!!!")
    #     #############################НАЧАЛО ТЕСТА##########################
# Эхо хендлер, куда летят ВСЕ сообщения с указанным состоянием
