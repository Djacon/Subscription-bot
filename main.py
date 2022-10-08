from aiogram.types import Message
from aiogram import Bot, Dispatcher, executor
from aiogram.utils.exceptions import MessageNotModified

from os import environ
from keyboards import *


TOKEN = environ['TOKEN']

bot = Bot(TOKEN)
dp = Dispatcher(bot)


@dp.errors_handler(exception=MessageNotModified)
async def message_not_modified_handler(*_):
    return True


def greet(user):
    return (f'Приветствую вас, {user}!\n\nВ списке курсов вы можете найти '
            'перечень предстоящих занятий.\nЗаписаться на нужный вам курс и '
            'произвести оплату:')


@dp.message_handler(commands=['start'])
async def start(message: Message):
    user = message.from_user.first_name
    await message.answer(greet(user), reply_markup=main_keyboard)


@dp.callback_query_handler(lambda c: c.data.startswith('course-'))
async def show_course(call):
    message = call.message
    index = int(call.data.split('-')[1])
    await message.edit_text(
        f"Курс: {DB.getCourse(index)[0]}\n\n"
        f'{DB.getCourse(index)[1]}',
        reply_markup=getCourseKeyboard(index)
    )


@dp.callback_query_handler(lambda c: c.data in ['courses', 'back'])
async def show_courses(call):
    message = call.message
    await message.edit_text(
        'Список предстоящих курсов:\n\n' +
        '\n\n'.join([f"{i+1}. {x[0]}" for i, x in enumerate(DB.getCourses())]),
        reply_markup=getCoursesKeyboard())


@dp.callback_query_handler(lambda c: c.data == 'homepage')
async def show_homepage(call):
    user = call.from_user.first_name
    await call.message.edit_text(greet(user), reply_markup=main_keyboard)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
