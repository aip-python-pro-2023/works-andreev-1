import os

import telebot
from dotenv import load_dotenv

import pokemons

load_dotenv()
TELEGRAM_TOKEN = os.environ['TELEGRAM_TOKEN']

bot = telebot.TeleBot(TELEGRAM_TOKEN, parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(commands=['pokemon'])
def get_pokemon(message):
    pokemon_name = message.text.split()[1]
    pokemon = pokemons.get_pokemon(pokemon_name)

    response = f"""*Название*: {pokemon['name']}
*Рост*: {pokemon['height'] * 10} см
*Вес*: {pokemon['weight'] * 100} г
*Типы*: {', '.join([t['type']['name'].capitalize() for t in pokemon['types']])}"""

    bot.send_message(message.chat.id, response, parse_mode='MarkdownV2')


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=2)
    button_1 = telebot.types.KeyboardButton('Hello')
    button_2 = telebot.types.KeyboardButton('from')
    button_3 = telebot.types.KeyboardButton('AIP')
    markup.add(button_1, button_2, button_3)

    bot.send_message(message.chat.id, message.text, reply_markup=markup)


bot.infinity_polling()
