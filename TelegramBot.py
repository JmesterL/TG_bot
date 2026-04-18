import telebot
import os
from telebot import types

#token bota
TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

#переменная клавиатура, в которой хранится эта команда
#как я понял, в скобочках дается размер кнопок, когда правда = они маленькие, когда лож = они большие
Keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
#А это сами кнопки, кнопки это просто слова которые не надо печатать. Если написать в ручную, то все будет работать
#у меня knopka = knp
knp1 = types.KeyboardButton("Помощь")

#Надо добавить теперь кнопку на экран
Keyboard.add(knp1)


#1 функция
#если нажата кнопка старт, то он будет печатать это
@bot.message_handler(commands=["start"])
def start(message):                                                                                #насильно вызывает клавиатуру во время старта
    bot.send_message(message.chat.id, "ПРИВЕЕЕЕТ! Я бот попугай и буду повторять за тобой слова!", reply_markup=Keyboard)
     #тут аналогично, не нужно ретурн, функция сама выполнит и напишет по айди отправителя уже заданный текст!



#2 функция
#если напечатать помощь, то он будет писать кто он и для чего. Ловер и стрип должны быть после text для правильности
@bot.message_handler(func=lambda message: message.text.lower().strip() == "помощь")#и если я делаю кнопки, лучше значения писать с маленькой буквы
def help(message):
    bot.send_message(message.chat.id, "Давай введу в курс дела!\nЯ создан для чила и расслабона!\nПока я могу лишь только повторять за тобой слова\nНО! В будущем я стану куда продвинутей!")
        #тут аналогично, не нужно ретурн, функция сама выполнит и напишет по айди отправителя уже заданный текст!




#3 функиця
#если он ловит любое сообщение, то вызывается основная функция попугая
@bot.message_handler(func=lambda message:True)
def echo(message):
    bot.send_message(message.chat.id, f"КхмКхм... {message.text}")
        #Это то что он будет делать, писать сообщение по айди отправителя копируя его текст с препиской кхмкхм


print("Бот работает!")
bot.infinity_polling()