from aiogram import types
from aiogram.dispatcher.filters import state
from states import states_bot
from loader import dp
from aiogram.dispatcher import FSMContext

from keyboards.default import button_bot

@dp.message_handler(state=states_bot.Users_state.list_vacant, content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
    if message.text in button_bot.vacant_mass:
        state = await state.get_state()
        await message.answer('Спасибо за ответ!\nЗаполните превичное резюме чтоб мы передали его в приемную комиссию.')
        await message.answer('Введите Ваше ФИО\nНапример(Иванов Иван Иванович)')
        await states_bot.Users_state.fio.set()

@dp.message_handler(state=states_bot.Users_state.fio, content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
    state = await state.get_state()
    await message.answer(f'{message.text}, напишите пожалуйта свою дату рождения.\nНапример(01.01.2000)')
    await message.answer(f"Эхо в состоянии <code>{state}</code>.\n")
    await states_bot.Users_state.date_birth.set()

@dp.message_handler(state=states_bot.Users_state.date_birth, content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
    state = await state.get_state()
    await message.answer(f'{message.text}, красивая дата, помню ее как вчера...\nГде проживаете или хотели бы найти работу?\nНапример(Москва/Сакнкт-Петербург/Екатеринбург)')
    await message.answer(f"Эхо в состоянии <code>{state}</code>.\n")
    await states_bot.Users_state.city.set()

@dp.message_handler(state=states_bot.Users_state.city, content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
    state = await state.get_state()
    await message.answer(f'{message.text}...\nБыл там на днях)\nТеперь расскажите пожалуйста какое у вас образование.\nНапример(Высшее/Средее-профессиональное/Среднее-общее)')
    await message.answer(f"Эхо в состоянии <code>{state}</code>.\n")
    await states_bot.Users_state.education.set()

@dp.message_handler(state=states_bot.Users_state.education, content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
    state = await state.get_state()
    await message.answer(f'{message.text}, понял.\nБыл ли у Вас поыт работы в данной сфере, если был то сколько лет?\nНапример(5 лет/-)')
    await message.answer(f"Эхо в состоянии <code>{state}</code>.\n")
    await states_bot.Users_state.experience.set()


@dp.message_handler(state=states_bot.Users_state.experience, content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
    state = await state.get_state()
    await message.answer(f'{message.text}, неплохо.\nГражданином какой страны Вы являетесь?\nНапример(Российская Федерация/Узбекистан/казахстан)')
    await message.answer(f"Эхо в состоянии <code>{state}</code>.\n")
    await states_bot.Users_state.citizenship.set()


@dp.message_handler(state=states_bot.Users_state.citizenship, content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
    state = await state.get_state()
    await message.answer(f'{message.text}, понятно.\nУ Вас есть разрешение на работу?', reply_markup=button_bot.yes_no)
    await message.answer(f"Эхо в состоянии <code>{state}</code>.\n")
    await states_bot.Users_state.work_permit.set()

@dp.message_handler(state=states_bot.Users_state.work_permit, content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
    if message.text in button_bot.yes_or_no:
        state = await state.get_state()
        await message.answer(f'На какую зароботную плату расчитываете?\nНапример(40000)')
        await message.answer(f"Эхо в состоянии <code>{state}</code>.\n")
        await states_bot.Users_state.zp.set()

@dp.message_handler(state=states_bot.Users_state.zp, content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
    state = await state.get_state()
    await message.answer(f'{message.text}, тоже такую хочу)\nЕсть ли еще какая-то информация, которую я должен зать при рассмотреии Вашей кандедатуры.')
    await message.answer(f"Эхо в состоянии <code>{state}</code>.\n")
    await states_bot.Users_state.about_me.set()

@dp.message_handler(state=states_bot.Users_state.about_me, content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
    state = await state.get_state()
    await message.answer(f'Приму это к сведению.\nЕсли есть какая-то сылка на ваши достижения или портфолио, отправьте его пожалуйста.\nНапример(https://rainforce.spb.ru/)')
    await message.answer(f"Эхо в состоянии <code>{state}</code>.\n")
    await states_bot.Users_state.link.set()

@dp.message_handler(state=states_bot.Users_state.link, content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
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
