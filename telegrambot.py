import telebot
import time
import datetime

bot = telebot.Telebot('')

numOfTheDay = 20
msgReminder = 'Передай показания счётчиков'
alreadyDid = false

# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("Показания уже переданы")
    markup.add(item1) 
    bot.send_message(m.chat.id, 'Введите число, с которого необходимо передавать показания счётчика')

 Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text.strip() == 'Показания уже переданы':
        alreadyDid = true    
    if int(message.text) > 1 and int(message.text) < 31:  
        msgResponse = 'Вы утверждаете, что передавать показания счётчиков необходимо с '
        bot.send_message(message.chat.id, msgResponse + message.text + ' числа')
        numOfTheDay = message.text
    else
        bot.send_message('Вы написали какую-то херню, пожалуйста, введите цифру от 1 до 31')


while true:   
    if datetime.date.today().day = 1:
        alreadyDid = false
    if datetime.date.today().day >= numOfTheDay and alreadyDid = false:    
        bot.send_message(message.chat.id, 'Братишка, от души, передай показания')
        time.sleep(12000)

    
# Запускаем бота
bot.polling(none_stop=True, interval=0)
