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
    if message.text == '/pokemon':
        response = 'Вместе с командой нужно отправить название Покемона, например, `/pokemon pikachu`'
        bot.send_message(message.chat.id, response, parse_mode='MarkdownV2')
        return

    pokemon_name = message.text.split()[1]
    response = pokemons.get_text_description(pokemon_name)

    bot.send_message(message.chat.id, response, parse_mode='MarkdownV2')


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.send_message(message.chat.id, 'Непонятное сообщение...')


bot.infinity_polling()
