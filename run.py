import telebot
import parser
from constants import HELLO_MESSAGE
from enums import CryptoCoin

TOKEN = '1299846139:AAGorwPjH8PxmesERnX7Abglo5FurAG9920'

bot = telebot.TeleBot(TOKEN)

# todo: add typings
@bot.message_handler(commands=['start'])
def start_message(message):
    markup = telebot.types.InlineKeyboardMarkup()

    markup.add(telebot.types.InlineKeyboardButton(text=CryptoCoin.BITCOIN.value, callback_data=1))
    markup.add(telebot.types.InlineKeyboardButton(text='Ethereum', callback_data=2))
    markup.add(telebot.types.InlineKeyboardButton(text='Polkadot', callback_data=3))
    markup.add(telebot.types.InlineKeyboardButton(text='Kusama', callback_data=4))

    bot.send_message(message.chat.id, text=HELLO_MESSAGE, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    bot.answer_callback_query(callback_query_id=call.id, text='Крипта правит миром')
    answer = ''
    if call.data == '1':
        answer = parser.get_content('Bitcoin')
    elif call.data == '2':
        answer = parser.get_content('Ethereum')
    elif call.data == '3':
        answer = parser.get_content('Polkadot')
    elif call.data == '4':
        answer = parser.get_content('Kusama')

    bot.send_photo(call.message.chat.id, answer.image)
    bot.send_message(call.message.chat.id, answer.text)


@bot.message_handler(commands=['help'])
def welcome_help(message):
    bot.send_message(message.chat.id, 'Проверяйте правильность написания. Название криптовалюты должно быть написано на английском языке')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    name = message.text
    lol = (parser.get_content(name))
    try:
        bot.send_photo(message.chat.id, lol.image)
        bot.send_message(message.chat.id, lol.text)
    except AttributeError:
        bot.send_message(message.chat.id, 'Вы ввели неправильное значение, введите /help для подробной информации')


if __name__ == "__main__":
    bot.polling()
