import telebot
import TOKEN
from MAT import mat

# Создание объекта бота с токеном
bot = telebot.TeleBot(TOKEN.token)

# Переменная для отслеживания состояния функции удаления сообщений
delete_active = True

# Обработчик команды /toggle_delete
@bot.message_handler(commands=['toggle_delete'])
def toggle_delete(message):
    global delete_active
    delete_active = not delete_active
    if delete_active:
        bot.reply_to(message, "Функция удаления сообщений активирована.")
    else:
        bot.reply_to(message, "Функция удаления сообщений деактивирована.")

# Функция для проверки сообщения на наличие мата
def check_profanity(message):
    for word in mat:
        if word in message.text:
            return True
    return False

# Обработчик всех входящих сообщений
@bot.message_handler(func=lambda message: True)
def delete_messages(message):
    global delete_active
    # Проверка, что функция удаления сообщений включена
    if delete_active:
        # Проверка, что отправитель не является администратором
        if not message.from_user.username in ['@cz0rneboh']:
            # Проверка на наличие мата в сообщении
            if any(bad_word in message.text.lower() for bad_word in mat):
                # Удаление сообщения

                bot.send_message(message.chat.id, (message.from_user.username+". Ай яй яй, иди помой язык с мылом"))
                bot.delete_message(message.chat.id, message.message_id)

# Запуск бота
bot.polling()
