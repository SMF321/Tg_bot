from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

administrator_actions = ['Редактор вакансий','Запуск анализатора сторонних сайтов','Поиск кандедатов по параметрам заполнявших анкеты','Редактов входного контроля','Статичтика среди кандедатов',]


def add_button(administrator_actions):
    admin_menu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    for i in administrator_actions:
        admin_button = KeyboardButton(i)
        admin_menu.add(admin_button)
    return(admin_menu)

# find_vacant = KeyboardButton('Запустить парсинг ресурсов')
# filters = KeyboardButton('Установить/изменить фильтры для входящих вакансий')
# create_test = KeyboardButton('Создать викторину для определенной вакансии')

# admin_menu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
# admin_menu.add(find_vacant).add(filters).add(create_test)

vacant_mass = ['Вакансия 1','Вакансия 2','Вакансия 3']

vacant1 = KeyboardButton('Вакансия 1')
vacant2 = KeyboardButton('Вакансия 2')
vacant3 = KeyboardButton('Вакансия 3')



vacant_list = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
vacant_list.add(vacant1).add(vacant2).add(vacant3)

yes_or_no = ['Да','Нет']

yes = KeyboardButton('Да')
no = KeyboardButton('Нет')

yes_no = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
yes_no.add(yes).add(no)


end_of_form = ['Отправить заяку', 'ПРОЙТИ ТЕСТ!']

send_a_request = KeyboardButton('Отправить заяку')
take_the_test = KeyboardButton('ПРОЙТИ ТЕСТ!')

end_of_form_filling = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
end_of_form_filling.add(send_a_request).add(take_the_test)

restart_test = ['Заполнить завяку вновь', 'ПРОЙТИ ТЕСТ!']

new_request = KeyboardButton('Заполнить завяку вновь')

restart_or_test = ReplyKeyboardMarkup(resize_keyboard=True)
restart_or_test.add(new_request).add(take_the_test)

sex_mass = ['Мужчина', 'Женщина']

man = KeyboardButton(sex_mass[0])
girl = KeyboardButton(sex_mass[1])

sex = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
sex.add(man).add(girl)


type_work_time = ['Полная','Частичная','Удаленная работа']

full = KeyboardButton(type_work_time[0])
partial = KeyboardButton(type_work_time[1])
remote = KeyboardButton(type_work_time[2])

work_time = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
work_time.add(full).add(partial).add(remote)