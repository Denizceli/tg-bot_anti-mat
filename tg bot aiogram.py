from aiogram import Bot, Dispatcher, executor , types

bot = Bot('6515033748:AAGmsu4w8PH6rs10KxtMLJp1c3aKvwgb6ek')
dp = Dispatcher(bot)


@dp.message_hendler(commands=['start'])
async def start(message: types.message):
 await message.answer(1)






executor.start_polling(dp)