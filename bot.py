import random
import telebot
import crypto_parser_bot

token = '1437801621:AAGqirw-CHQ9ecKw2T17pn1QWEj7ANvXrEM'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, я крипто-бот, знаю курсы всех известных криптовалют. Могу тебе показать. Введи название любой криптовалюты... ')

@bot.message_handler(commands=['help'])
def welcome_help(message):
    bot.send_message(message.chat.id, 'Вводите название с большой буквы. Проверяйте правильность написания, бот пока что чувствителен к регистру')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    name = message.text;
    lol = (crypto_parser_bot.parse(name))

    bot.send_message(message.chat.id, lol)



bot.polling()
