import telebot
from telebot import types
import random
import os
global script_dir
token = ''
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def handle_start(message):
    start(message)
@bot.message_handler(commands=['start'])
def eawryhhhsgh(message):
    
    start(message)

@bot.message_handler(commands=['debug'])
def debug(message):
    bot.reply_to(message, message)
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton('Перезагрузка'),types.KeyboardButton('Случайное число'))
    markup.add(types.KeyboardButton('Случайная буква'),(types.KeyboardButton('Покричи')))

    if message.from_user.id == 5577696042:
        bot.reply_to(message, 'Привет Битл!!', reply_markup=markup)
    elif message.from_user.id == 7136699146:
        bot.reply_to(message, 'Привет Чикенгай26к!!')
    else:
        bot.reply_to(message,
                     'Привет! Это бот Битла версии 2 мини.',
                     reply_markup=markup)



def handle_reboot(message):
    start(message)


def handle_random_number(message):
    random_number = random.randint(-100, 100)
    bot.reply_to(message, f"Случайное число: {random_number}")


def handle_random_letter(message):
    letters = [
        'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М',
        'Н', 'О', 'П', 'Р', 'Т', 'С', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ',
        'Ь', 'Э', 'Ю', 'Я'
    ]
    random_letter = random.choice(letters)
    bot.reply_to(message, f"Случайная буква: {random_letter}")


def handle_user_id(message):
    bot.reply_to(message, f"Ваш id: {message.from_user.id}")

def AAAAA(message):
    if message.chat.type == 'group':
        bot.reply_to(message,
                     'Мне папа запретил кричать в общественных местах.')
    else:
        if message.chat.type == 'supergroup':
            bot.reply_to(message,
                         'Мне папа запретил кричать в общественных местах.')
        else:
            wh = 0
            ranqq = 2
            while (wh < ranqq):
                bot.reply_to(
                    message,
                    'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
                )
                wh = wh + 1


@bot.message_handler(commands=['say'])
def handle_say(message):
    
    command_parts = message.text.split(maxsplit=1)
    if len(command_parts) > 1:
        text_to_say = command_parts[1]
        bot.reply_to(message, text_to_say)
    else:
        bot.reply_to(message, 'Укажи текст после команды /say.')


@bot.message_handler(commands=['run'])
def handle_run_command(message):
    if message.from_user.id == 5577696042:
        global commandtorun
        command = message.text[5:]  # Получаем команду после '/run '
        if command:
            commandtorun = command.strip()
            exec(commandtorun)
def handle_message(message):
    com = message.text.lower()
    if com == 'перезагрузка':
        handle_reboot(message)
    elif com == 'случайное число':
        handle_random_number(message)
    elif com == 'случайная буква':
        handle_random_letter(message)
    elif com == 'покричи':
        AAAAA(message)
    elif com in ['битл', 'бот', 'битл бот', 'битл бот 2', 'бот битл','бот битл 2', 'бот битла', 'боты', 'бетле', 'рапта','бетле рапта']:
        ans = ['Да-да?', 'Что?', 'Я тута!']
        send = random.choice(ans)
        bot.reply_to(message, send)


@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    handle_message(message)


# Запуск бота
bot.infinity_polling()
