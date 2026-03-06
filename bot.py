import telebot
import os

TOKEN = os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "ПРИВЕЕЕЕТ! Я бот попугай и буду повторять за тобой слова!")

@bot.message_handler(func=lambda message:True)
def echo(message):
    bot.send_message(message.chat.id, f"КхмКхм... {message.text}")

print("Бот работает!")
bot.infinity_polling()