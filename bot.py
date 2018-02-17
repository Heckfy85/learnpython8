
import logging
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


# Импортируем нужные компоненты
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler #Updater - это компонент отвечающий за коммуникацию с сервером, CommandHandler - обработчик команд


# Функция, которая соединяется с платформой Telegram, "тело" нашего бота
def main():
    updater = Updater("463329761:AAGE7IKeQ8usM-3LZ7J3WAs7ZKeuzpNidzM")
    def greet_user(bot, update):
        text = 'Вызван /start'
        print(text)
        update.message.reply_text(text)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))    #добавим команду "/start"
    def talk_to_me(bot, update):
        user_text = update.message.text 
        print(user_text)
        update.message.reply_text(user_text)
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    updater.start_polling()
    updater.idle()

# Вызываем функцию - эта строчка собственно запускает бота
main()
