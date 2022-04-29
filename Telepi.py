import os
import telebot

#API_KEY = os.getenv('API_KEY')

bot = telebot.TeleBot('5208741101:AAH7RzGlEqA7MB7vLFGl8LQMZV_il1_l9B0')

@bot.message_handler(commands=['Hello'])
def hello(message):
	bot.send_message(message.chat.id,"Hey! Hows it going?") 
	print(message)
bot.polling()

print('h1')
