# shani korshov :)


# add hava a nice day + emoji

# from typing import Text
import telebot
import time
from datetime import datetime

API_KEY = '2015370576:AAH1khk0sub9VVBDY5zOEj4c4v8QxLWziA8'
bot = telebot.TeleBot(token=API_KEY)


@bot.message_handler(commands=['Hey', 'start', 'Hi', 'hi', 'hey', 'hello', 'sup', 'Hello'])
def send_welcome(message):
    response = "Hey🌈🤗👋🏼\nHows it going?👻\nPlease type a day and use this formatting: /day"
    bot.send_message(message.chat.id, response)


# sunday response
@bot.message_handler(commands=['sunday', 'SUNDAY', 'Sunday'])
def sunday(message):
    now = datetime.now()
    response = now.strftime(
        "%d/%m/%y\n%H:%M:%S\n\n")
    response += "🔹 Your Schedule for today📢 🔹\n\n"
    response += "▪️Introduction To System Programming Lecture\n12:00-13:50\nLink📎:\nhttps://tinyurl.com/y22nzm6n\n"
    response += "▪️Introduction To System Programming Practice \n14:00-15:50\nLink📎:\nhttps://tinyurl.com/y22nzm6n\n"
    bot.send_message(message.chat.id, response)

# monday response


@ bot.message_handler(commands=['monday', 'MONDAY', 'Monday'])
def sunday(message):
    now = datetime.now()
    response = now.strftime(
        "%d/%m/%y\n%H:%M:%S\n\n")
    response += "🔹 Your Schedule for today📢 🔹\n\n"
    response += "▪️Mathematics Logic Practice\n10:00-11:50\nLink📎:\nhttps://tinyurl.com/y22nzm6n\n"
    response += "▪️Introduction To Software Engineering Practice \n12:00-13:50\nLink📎:\nhttps://tinyurl.com/y22nzm6n\n"
    response += "▪️Mathematics Logic Lecture\n14:00-15:50\nLink📎:\nhttps://tinyurl.com/y22nzm6n\n"
    bot.send_message(message.chat.id, response)

# tuesday response


@ bot.message_handler(commands=['tuesday', 'TUESDAY', 'Tuesday'])
def sunday(message):
    now = datetime.now()
    response = now.strftime(
        "%d/%m/%y\n%H:%M:%S\n\n")
    response += "🔹 Your Schedule for today📢 🔹\n\n"
    response += "▪️Computers Communications Lab\n8:00-9:50\nLink📎:\nhttps://tinyurl.com/y22nzm6n\n"
    response += "▪️Computers Communications Lecture\n10:00-12:50\nLink📎:\nhttps://tinyurl.com/y22nzm6n\n"
    response += "▪️Computers Communications Practice\n13:00-13:50\nLink📎:\nhttps://tinyurl.com/y22nzm6n\n"
    response += "▪️Data Structures Lecture\n18:00-19:50\nLink📎:\nhttps://tinyurl.com/y22nzm6n\n"
    bot.send_message(message.chat.id, response)


# wednesday response

@ bot.message_handler(commands=['wednesday', 'WEDNESDAY', 'Wednesday', 'Friday', 'FRIDAY', 'friday', 'Saturday', 'saturday', 'SATURDAY'])
def sunday(message):
    response = "This is your free day!\nGo to the gym 💪🏋️‍♂️👽"
    bot.send_message(message.chat.id, response)


# thursday response

@ bot.message_handler(commands=['thursday', 'THURSDAY', 'Thursday'])
def sunday(message):
    now = datetime.now()
    response = now.strftime(
        "%d/%m/%y\n%H:%M:%S\n\n")
    response += "🔹 Your Schedule for today📢 🔹\n\n"
    response += "▪️Data Structures Practice\n16:00-17:50\nLink📎:\nhttps://tinyurl.com/y22nzm6n\n"
    response += "▪️Data Structures Lecture\n18:00-19:50\nLink📎:\nhttps://tinyurl.com/y22nzm6n\n"
    bot.send_message(message.chat.id, response)


while True:
    try:
        bot.polling()  # checking for messages
    except Exception:
        time.sleep(15)
