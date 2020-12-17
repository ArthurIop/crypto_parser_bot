import random
import telebot
import crypto_parser_bot

token = '1437801621:AAGqirw-CHQ9ecKw2T17pn1QWEj7ANvXrEM'
bot = telebot.TeleBot(token)
lol = str(crypto_parser_bot.parse('Kusama'))

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    name = message.text;
    lol = (crypto_parser_bot.parse(name))

    bot.send_message(message.chat.id, lol)


@bot.message_handler(commands=['help'])
def welcome_help(message):
    bot.send_message(message.chat.id, 'Чем я могу тебе помочь')

bot.polling()
