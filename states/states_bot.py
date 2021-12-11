from aiogram.dispatcher.filters.state import State, StatesGroup

class Admins_state(StatesGroup):
    menu_button = State()
    redactor_vacant = State()
    find_vacant = State()
    find_in_db_filter = State()
    create_and_redactor_test = State()
    stat = State()

class Users_state(StatesGroup):
    list_vacant = State()

    fio = State()
    city = State()
    date_birth = State()
    sex = State()
    citizenship = State()
    experience = State()
    time_type = State()
    skills = State()
    portfolio = State()
    link = State()
    
    question_for_testing = State()

    send_application_or_testing = State()

