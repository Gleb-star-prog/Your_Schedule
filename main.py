import telebot
import config
from telebot import types

bot = telebot.TeleBot(config.TELEGRAM_BOT_TOKEN)

keyboard = types.InlineKeyboardMarkup()

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == '/start':
        bot.send_message(message.from_user.id, 'Привет')
        bot.send_message(message.from_user.id, 'Я бот "твое расписание"')
        bot.send_message(message.from_user.id, 'Ты сможешь во мне создавать свое расписание')
    elif message.text == 'Начнем':
        key_schedule1 = types.InlineKeyboardButton(text='расписание1', callback_data='schedule')
        keyboard.add(key_schedule1)

        key_schedule2 = types.InlineKeyboardButton(text='расписание2', callback_data='schedule')
        keyboard.add(key_schedule2)

        key_schedule3 = types.InlineKeyboardButton(text='расписание3', callback_data='schedule')
        keyboard.add(key_schedule3)

        key_schedule4 = types.InlineKeyboardButton(text='расписание4', callback_data='schedule')
        keyboard.add(key_schedule4)

        key_schedule5 = types.InlineKeyboardButton(text='расписание5', callback_data='schedule')
        keyboard.add(key_schedule5)
        bot.send_message(message.from_user.id, text='Хорошо \n выбери ячейку', reply_markup=keyboard)
    elif message.text == '/help':
        bot.send_message(message.from_user.id, 'чтобы начать создовать свое расписание')
        bot.send_message(message.from_user.id, 'нужно написать "Начнем"')
    else:
        bot.send_message(message.from_user.id, 'я тебя не понял')
        bot.send_message(message.from_user.id, 'напиши "/help"')

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == 'schedule':
        bot.send_message(call.message.chat.id, 'окей \n напиши себе напоминание')

bot.polling(none_stop=True, interval=0)