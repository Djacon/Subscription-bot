from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
<<<<<<< HEAD
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import ReplyKeyboardRemove
=======
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
>>>>>>> fea50e3b2be7c6435b78c4cbbff07791a11596c9
from database import DB


def getCourseKeyboard(i: int, isAdmin: bool):
    sub = InlineKeyboardButton('✍ Записаться и перейти к оплате',
                               callback_data=f'subscribe-{i}',
                               url=DB.getCourse(i)[2])
    back = InlineKeyboardButton('⬅ Назад', callback_data='courses')
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
    src = InlineKeyboardButton('Изменить ссылку',
                               callback_data=f'source-{i}')
    delete = InlineKeyboardButton('❌ Удалить курс',
                                  callback_data=f'delete-{i}')
<<<<<<< HEAD
    back = InlineKeyboardButton('⬅ Назад', callback_data=f'course-{i}')
    homepage = InlineKeyboardButton('🏠 На главную', callback_data='homepage')
    courses_keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=1)
    return courses_keyboard.add(title, desc, src, delete).row(back, homepage)
=======
    back = InlineKeyboardButton('⬅ Назад', callback_data='courses')
    homepage = InlineKeyboardButton('🏠 На главную', callback_data='homepage')
    courses_keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=1)
    return courses_keyboard.add(title, desc, src, delete).row(back, homepage)


def getAddKeyboard():
    yes = InlineKeyboardButton('Да', callback_data='add_surely')
    no = InlineKeyboardButton('Нет', callback_data='courses')
    return InlineKeyboardMarkup(resize_keyboard=True).add(yes, no)
>>>>>>> fea50e3b2be7c6435b78c4cbbff07791a11596c9


def getDeleteKeyboard(i: int):
    yes = InlineKeyboardButton('Да', callback_data=f'delete_surely-{i}')
    no = InlineKeyboardButton('Нет', callback_data=f'editCourse-{i}')
    return InlineKeyboardMarkup(resize_keyboard=True).add(yes, no)


<<<<<<< HEAD
def getAddKeyboard():
    yes = InlineKeyboardButton('Да', callback_data='add_surely')
    no = InlineKeyboardButton('Нет', callback_data='courses')
    return InlineKeyboardMarkup(resize_keyboard=True).add(yes, no)


addKb = getAddKeyboard()

mainKb = InlineKeyboardButton('Показать курсы', callback_data='courses')
mainKb = InlineKeyboardMarkup(resize_keyboard=True).add(mainKb)

cancelKb = KeyboardButton('Отмена')
cancelKb = ReplyKeyboardMarkup(resize_keyboard=True).add(cancelKb)

noneKb = ReplyKeyboardRemove()
=======
def getBackKb():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    back = KeyboardButton('<- Назад')
    return markup.add(back)


mainKb = InlineKeyboardButton('Показать курсы', callback_data='courses')
mainKb = InlineKeyboardMarkup(resize_keyboard=True).add(mainKb)

cancel_keyboard = KeyboardButton('Отмена')
cancel_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(cancel_keyboard)

noneKb = ReplyKeyboardRemove()
>>>>>>> fea50e3b2be7c6435b78c4cbbff07791a11596c9
