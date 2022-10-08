from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from database import DB


def getCourseKeyboard(i: int, isAdmin: bool):
    sub = InlineKeyboardButton('✍ Записаться и перейти к оплате',
                               callback_data=f'subscribe-{i}',
                               url=DB.getCourse(i)[2])
    back = InlineKeyboardButton('⬅ Назад', callback_data='back')
    homepage = InlineKeyboardButton('🏠 На главную', callback_data='homepage')
    courses_keyboard = InlineKeyboardMarkup(resize_keyboard=True)
    if not isAdmin:
        return courses_keyboard.add(sub).row(back, homepage)
    edit = InlineKeyboardButton('Отредактировать',
                                callback_data=f'editCourse-{i}')
    return courses_keyboard.add(sub).row(edit).row(back, homepage)


def getCoursesKeyboard(isAdmin: bool):
    courses = []
    for i, x in enumerate(DB.getCourses()):
        courses.append(InlineKeyboardButton(f"{i+1}. {x[0]}",
                       callback_data=f'course-{i}'))
    homepage = InlineKeyboardButton('🏠 На главную', callback_data='homepage')
    courses_keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
    if not isAdmin:
        return courses_keyboard.add(*courses).row(homepage)
    add = InlineKeyboardButton('✅ Добавить курс', callback_data='add')
    return courses_keyboard.add(*courses).row(add).row(homepage)


def getEditCourseKeyboard(i: int):
    title = InlineKeyboardButton('Изменить заголовок',
                                 callback_data=f'title-{i}')
    desc = InlineKeyboardButton('Изменить описание',
                                callback_data=f'description-{i}')
    delete = InlineKeyboardButton('❌ Удалить курс',
                                  callback_data=f'delete-{i}')
    back = InlineKeyboardButton('⬅ Назад', callback_data='back')
    homepage = InlineKeyboardButton('🏠 На главную', callback_data='homepage')
    courses_keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=1)
    return courses_keyboard.add(title, desc).row(delete).row(back, homepage)


def getAddKeyboard():
    yes = InlineKeyboardButton('Да', callback_data='add_surely')
    no = InlineKeyboardButton('Нет', callback_data='back')
    return InlineKeyboardMarkup(resize_keyboard=True).add(yes, no)


def getDeleteKeyboard(i: int):
    yes = InlineKeyboardButton('Да', callback_data=f'delete_surely-{i}')
    no = InlineKeyboardButton('Нет', callback_data=f'editCourse-{i}')
    return InlineKeyboardMarkup(resize_keyboard=True).add(yes, no)


main_keyboard = InlineKeyboardButton('Показать курсы', callback_data='courses')
main_keyboard = InlineKeyboardMarkup(resize_keyboard=True).add(main_keyboard)
