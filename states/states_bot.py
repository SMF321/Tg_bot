from aiogram.dispatcher.filters.state import State, StatesGroup

class Admins_state(StatesGroup):
    menu_button = State()

    find_vacant = State()
    filters = State()
    create_test = State()

class Users_state(StatesGroup):
    list_vacant = State()

    fio = State()
    date_birth = State()
    city = State()
    education = State()
    experience = State()
    citizenship = State()
    work_permit = State()
    zp = State()
    about_me = State()
    link = State()
    
    question_for_testing = State()

    send_application = State()