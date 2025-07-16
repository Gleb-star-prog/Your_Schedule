import telebot
import config
from telebot import types

bot = telebot.TeleBot(config.TELEGRAM_BOT_TOKEN)

keyboard1 = types.InlineKeyboardMarkup()
keyboard2 = types.InlineKeyboardMarkup()

class User():
    def __init__(self, Schedule1, Schedule2, Schedule3, Schedule4, Schedule5, Time1, Time2, Time3, Time4, Time5):
        self.Schedule1 = Schedule1
        self.Schedule2 = Schedule2
        self.Schedule3 = Schedule3
        self.Schedule4 = Schedule4
        self.Schedule5 = Schedule5
        self.Time1 = Time1
        self.Time2 = Time2
        self.Time3 = Time3
        self.Time4 = Time4
        self.Time5 = Time5

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == '/start':
        bot.send_message(message.from_user.id, 'Привет \n Я бот "твое расписание" \n Ты сможешь во мне создавать свое расписание')
    elif message.text == 'Начнем':
        key_schedule1 = types.InlineKeyboardButton(text='расписание1', callback_data='schedule')
        keyboard1.add(key_schedule1)

        key_schedule2 = types.InlineKeyboardButton(text='расписание2', callback_data='schedule')
        keyboard1.add(key_schedule2)

        key_schedule3 = types.InlineKeyboardButton(text='расписание3', callback_data='schedule')
        keyboard1.add(key_schedule3)

        key_schedule4 = types.InlineKeyboardButton(text='расписание4', callback_data='schedule')
        keyboard1.add(key_schedule4)

        key_schedule5 = types.InlineKeyboardButton(text='расписание5', callback_data='schedule')
        keyboard1.add(key_schedule5)
        bot.send_message(message.from_user.id, text='Хорошо \n выбери ячейку', reply_markup=keyboard1)
    elif message.text == '/help':
        bot.send_message(message.from_user.id, 'чтобы начать создовать свое расписание \n нужно написать "Начнем"')
    elif message.text[0] != '1' and message.text[0] != '2':
        bot.send_message(message.from_user.id, 'я тебя не понял \n напиши "/help"')
    elif message.text[0] == '1':
        bot.send_message(message.from_user.id, 'теперь надо написать время, когда придет напоминание \n "2часов:минут"')
    elif message.text[0] == '2':

        choice1 = types.InlineKeyboardButton(text='да', callback_data='choice')
        keyboard2.add(choice1)

        choice2 = types.InlineKeyboardButton(text='нет', callback_data='choice')
        keyboard2.add(choice2)

        bot.send_message(message.from_user.id, 'окей \n вы хотите что нибуть поменять?', reply_markup=keyboard2)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == 'schedule':
        bot.send_message(call.message.chat.id, 'окей \n напиши себе напоминание \n "1твое расписание"')

bot.polling(none_stop=True, interval=0)