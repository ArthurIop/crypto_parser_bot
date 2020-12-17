import random
import telebot
import crypto_parser_bot

token = 'ТОКЕН'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='Bitcoin', callback_data=1))
    markup.add(telebot.types.InlineKeyboardButton(text='Ethereum', callback_data=2))
    markup.add(telebot.types.InlineKeyboardButton(text='Polkadot', callback_data=3))
    markup.add(telebot.types.InlineKeyboardButton(text='Kusama', callback_data=4))
    bot.send_message(message.chat.id, text="Привет, я крипто-бот, знаю курсы всех известных криптовалют. Могу тебе показать. Введи название любой криптовалюты. Вот тебе самые известные:", reply_markup=markup)



@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):

    bot.answer_callback_query(callback_query_id=call.id, text='Крипта правит миром')
    answer = ''
    if call.data == '1':
        answer = crypto_parser_bot.parse('Bitcoin')
    elif call.data == '2':
        answer = crypto_parser_bot.parse('Ethereum')
    elif call.data == '3':
        answer = crypto_parser_bot.parse('Polkadot')
    elif call.data == '4':
        answer = crypto_parser_bot.parse('Kusama')

    bot.send_message(call.message.chat.id, answer)

@bot.message_handler(commands=['help'])
def welcome_help(message):
    bot.send_message(message.chat.id, 'Вводите название с большой буквы. Проверяйте правильность написания, бот пока что чувствителен к регистру')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    name = message.text;
    lol = (crypto_parser_bot.parse(name))

    bot.send_message(message.chat.id, lol)


bot.polling()
