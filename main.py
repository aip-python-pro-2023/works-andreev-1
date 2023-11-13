import os

import telebot
from dotenv import load_dotenv

import players
import pokemons

load_dotenv()
TELEGRAM_TOKEN = os.environ['TELEGRAM_TOKEN']

bot = telebot.TeleBot(TELEGRAM_TOKEN, parse_mode=None)


@bot.message_handler(commands=['help'])
def send_welcome(message):
    response = """Основные команды:

/start - регистрация и получение стартового покемона (один раз)
/pokemon <name> - получение базовой информации о покемоне
/battle - битва с другим игроков
/shop - магазин
/stats - статистика игрока"""
    bot.send_message(message.chat.id, response)


@bot.message_handler(commands=['start'])
def register_player(message: telebot.types.Message):
    is_ok = players.register(message.from_user.id)
    if not is_ok:
        bot.send_message(message.chat.id, 'Вы уже зарегистрированы :\\)', parse_mode='MarkdownV2')
        return

    bot.send_message(message.chat.id, 'Поздравляем с регистрацией\\! 🎉', parse_mode='MarkdownV2')

    markup = telebot.types.InlineKeyboardMarkup(row_width=3)
    button_1 = telebot.types.InlineKeyboardButton('Grookey', callback_data='starter_grookey')
    button_2 = telebot.types.InlineKeyboardButton('Scorbunny', callback_data='starter_scorbunny')
    button_3 = telebot.types.InlineKeyboardButton('Sobble', callback_data='starter_sobble')
    markup.add(button_1, button_2, button_3)

    response = """*Выберите стартового покемона*

Вы можете выбрать одного из трёх стартовых покемонов:

🌿 *Grookey:* Покемон травяного типа
🔥 *Scorbunny:* Покемон огненного типа
🌊 *Sobble:* Покемон водяного типа
"""

    bot.send_message(message.chat.id, response, parse_mode='MarkdownV2', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data.startswith('starter_'))
def handle_starter_selection(call: telebot.types.CallbackQuery):
    selected = call.data.split('_')[1]
    match selected:
        case 'grookey' | 'scorbunny' | 'sobble' as name:
            bot.answer_callback_query(call.id, f'Вы выбрали {name.capitalize()}!')
            players.add_pokemon(call.from_user.id, name)
            bot.edit_message_reply_markup(call.message.chat.id, call.message.id, reply_markup=None)
            bot.send_message(call.message.chat.id, f'Вы выбрали {name.capitalize()}!')
        case _:
            bot.answer_callback_query(call.id, "Вы выбрали что\\-то не то :\\(")


@bot.message_handler(commands=['pokemon'])
def get_pokemon(message):
    if message.text == '/pokemon':
        response = 'Вместе с командой нужно отправить название Покемона, например, `/pokemon pikachu`'
        bot.send_message(message.chat.id, response, parse_mode='MarkdownV2')
        return

    pokemon_name = message.text.split()[1]
    response = pokemons.get_text_description(pokemon_name)

    bot.send_message(message.chat.id, response, parse_mode='MarkdownV2')


@bot.message_handler(commands=['stats'])
def get_stats(message):
    response = players.get_text_description(message.from_user.id)
    if response is None:
        bot.send_message(message.chat.id, 'Вы ещё не стали тренером... Но можете им стать, отправив /start', parse_mode='MarkdownV2')
        return

    bot.send_message(message.chat.id, response, parse_mode='MarkdownV2')


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.send_message(message.chat.id, 'Непонятное сообщение...')


bot.infinity_polling()
