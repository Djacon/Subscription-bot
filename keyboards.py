from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from database import DB


def getCourseKeyboard(i: int):
    sub = InlineKeyboardButton('✍ Записаться и перейти к оплате',
                               callback_data=f'subscribe-{i}',
                               url=DB.getCourse(i)[2])
    back = InlineKeyboardButton('⬅ Назад', callback_data='back')
    homepage = InlineKeyboardButton('🏠 На главную', callback_data='homepage')
    courses_keyboard = InlineKeyboardMarkup(resize_keyboard=True)
    return courses_keyboard.add(sub).row(back, homepage)


def getCoursesKeyboard():
    courses = []
    for i, x in enumerate(DB.getCourses()):
        courses.append(InlineKeyboardButton(f"{i+1}. {x[0]}",
                       callback_data=f'course-{i}'))
    homepage = InlineKeyboardButton('🏠 На главную', callback_data='homepage')
    courses_keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
    return courses_keyboard.add(*courses).row(homepage)


main_keyboard = InlineKeyboardButton('Показать курсы', callback_data='courses')
main_keyboard = InlineKeyboardMarkup(resize_keyboard=True).add(main_keyboard)
