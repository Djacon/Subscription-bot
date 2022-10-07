from aiogram import Bot, Dispatcher, executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, Message

TOKEN = '5798953874:AAGdbXmRWxwN9niTAVzBmVfpyZM4UnDEf3M'

bot = Bot(TOKEN)
dp = Dispatcher(bot)


def getKeyboard():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    getcource = KeyboardButton('Получить курс')
    markup.add(getcource)
    return markup


@dp.message_handler(commands=['start'])
async def start(message: Message):
    user = message.from_user.first_name
    greet = (f'Приветствую вас, {user}!\nЗдесь вы можешь легко подписаться на'
             ' нужный вам курс\n\nНажмите «Получить курс», чтобы продолжить:')
    await message.answer(greet, reply_markup=getKeyboard())


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
