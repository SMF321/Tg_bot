from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton


find_vacant = KeyboardButton('Запустить парсинг ресурсов')
filters = KeyboardButton('Установить/изменить фильтры для входящих вакансий')
create_test = KeyboardButton('Создать викторину для определенной вакансии')

admin_menu = ReplyKeyboardMarkup(resize_keyboard=True)
admin_menu.add(find_vacant).add(filters).add(create_test)