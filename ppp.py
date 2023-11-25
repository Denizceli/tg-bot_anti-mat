import telebot

# Создание объекта бота с токеном
bot = telebot.TeleBot("6515033748:AAGmsu4w8PH6rs10KxtMLJp1c3aKvwgb6ek")

# Переменная для отслеживания состояния функции удаления сообщений
delete_active = False

# Обработчик команды /toggle_delete
@bot.message_handler(commands=['toggle_delete'])
def toggle_delete(message):
    global delete_active
    delete_active = not delete_active
    if delete_active:
        bot.reply_to(message, "Функция удаления сообщений активирована.")
    else:
        bot.reply_to(message, "Функция удаления сообщений деактивирована.")

# Обработчик всех входящих сообщений
@bot.message_handler(func=lambda message: True)
def delete_messages(message):
    global delete_active
    # Проверка, что функция удаления сообщений включена
    if delete_active:
        # Проверка, что отправитель не является администратором
        if not message.from_user.username in ['@cz0rneboh']:
            # Удаление сообщения
            bot.delete_message(message.chat.id, message.message_id)

# Запуск бота
bot.polling()