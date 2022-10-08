from aiogram.types import Message
from aiogram import Bot, Dispatcher, executor
from aiogram.utils.exceptions import MessageNotModified
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup

from os import environ
from keyboards import *

TOKEN = environ['TOKEN_COURSE']

bot = Bot(TOKEN)

storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


class Course(StatesGroup):
    index = State()
    title = State()
    description = State()


@dp.errors_handler(exception=MessageNotModified)
async def message_not_modified_handler(*_):
    return True


def greet(user: int) -> str:
    return (f'Приветствую Вас, {user}!\n\nВ списке курсов Вы можете найти '
            'перечень предстоящих занятий.\nЗаписаться на нужный Вам курс и '
            'произвести оплату:')


def isAdmin(message) -> bool:
    return message.from_user.id in [915782472, 1268258973]


@dp.message_handler(commands=['start'])
async def start(message: Message):
    user = message.from_user.first_name
    await message.answer(greet(user), reply_markup=main_keyboard)


@dp.callback_query_handler(lambda c: c.data.startswith('editCourse'))
async def show_editCourse(call):
    message = call.message
    index = int(call.data.split('-')[1])
    await message.edit_text(
        f"Курс: {DB.getCourse(index)[0]}\n\n"
        f'{DB.getCourse(index)[1]}',
        reply_markup=getEditCourseKeyboard(index))


@dp.callback_query_handler(lambda c: c.data.startswith('title'))
async def show_editTitle(call):
    message = call.message
    ind = int(call.data.split('-')[1])

    state = dp.current_state(user=call.from_user.id)
    await state.update_data(index=ind)

    await Course.title.set()
    await message.edit_text('Введите новый заголовок'
                            ' (Введите `отмена`, чтобы выйти):')


@dp.callback_query_handler(lambda c: c.data.startswith('description'))
async def show_editTitle(call):
    message = call.message
    ind = int(call.data.split('-')[1])

    state = dp.current_state(user=call.from_user.id)
    await state.update_data(index=ind)

    await Course.description.set()
    await message.edit_text('Введите новое описание'
                            ' (Введите `отмена`, чтобы выйти):')


@dp.message_handler(state=Course.title)
async def scheduleDay(message: Message, state):
    async with state.proxy() as data:
        index = data['index']
    await state.finish()

    if message.text.lower() != 'отмена':
        DB.editCourse(index, 0, message.text)
        await message.answer('Изменено')
    else:
        await message.answer('Отменено')

    await message.answer(
        f"Курс: {DB.getCourse(index)[0]}\n\n"
        f'{DB.getCourse(index)[1]}',
        reply_markup=getEditCourseKeyboard(index))


@dp.message_handler(state=Course.description)
async def scheduleDay(message: Message, state):
    async with state.proxy() as data:
        index = data['index']
    await state.finish()

    if message.text.lower() != 'отмена':
        DB.editCourse(index, 1, message.text)
        await message.answer('Изменено')
    else:
        await message.answer('Отменено')

    await message.answer(
        f"Курс: {DB.getCourse(index)[0]}\n\n"
        f'{DB.getCourse(index)[1]}',
        reply_markup=getEditCourseKeyboard(index))


@dp.callback_query_handler(lambda c: c.data.startswith('course-'))
async def show_course(call):
    message = call.message
    index = int(call.data.split('-')[1])
    await message.edit_text(
        f"Курс: {DB.getCourse(index)[0]}\n\n"
        f'{DB.getCourse(index)[1]}',
        reply_markup=getCourseKeyboard(index, isAdmin(call)))


async def courses_page(call):
    message = call.message
    await message.edit_text(
        'Список предстоящих курсов:\n\n' +
        '\n\n'.join([f"{i+1}. {x[0]}" for i, x in enumerate(DB.getCourses())]),
        reply_markup=getCoursesKeyboard(isAdmin(call)))


@dp.callback_query_handler(lambda c: c.data == 'add')
async def show_add(call):
    message = call.message
    await message.edit_text('Вы хотите создать курс?',
                            reply_markup=getAddKeyboard())


@dp.callback_query_handler(lambda c: c.data == 'add_surely')
async def show_add(call):
    DB.addCourse()
    await courses_page(call)


@dp.callback_query_handler(lambda c: c.data.startswith('delete_surely'))
async def show_delete(call):
    index = int(call.data.split('-')[1])
    DB.deleteCourse(index)
    await courses_page(call)


@dp.callback_query_handler(lambda c: c.data.startswith('delete'))
async def show_delete(call):
    message = call.message
    index = int(call.data.split('-')[1])
    await message.edit_text('Вы точно уверены, что хотите удалить курс?',
                            reply_markup=getDeleteKeyboard(index))


@dp.callback_query_handler(lambda c: c.data in ['courses', 'back'])
async def show_courses(call):
    await courses_page(call)


@dp.callback_query_handler(lambda c: c.data == 'homepage')
async def show_homepage(call):
    user = call.from_user.first_name
    await call.message.edit_text(greet(user), reply_markup=main_keyboard)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
