# shani korshov :)


# add hava a nice day + emoji

# from typing import Text
import telebot
import time
from datetime import datetime

API_KEY = '2015370576:AAH1khk0sub9VVBDY5zOEj4c4v8QxLWziA8'
bot = telebot.TeleBot(token=API_KEY)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    response = "Hey🌈🤗👋🏼\nHows it going?👻\nPlease type a day📅"
    bot.send_message(message.chat.id, response)


def day_request(message):
    return True


def is_day(message):
    day = message.text.lower()
    word = day.split()
    if len(word) > 1:
        if "hey" in day or "hello" in day or "hi" in day:
            return False, "greet"
        else:
            return False, "None"
    days = ("sunday", "monday", "tuesday", "wednesday",
            "thursday", "friday", "saturday")
    ok = False
    if day in days:
        return True, day
    else:
        return False, day


@bot.message_handler(func=day_request)
def send_day(message):
    ok, day = is_day(message)
    if (day == "greet" or "hey" in day or "hi" in day or "hello" in day):
        response = "Hey🌈🤗👋🏼\nHows it going?👻\nPlease type a day📅"
        bot.send_message(message.chat.id, response)
    elif ok == False:
        bot.send_message(
            message.chat.id, "Ugh I didn't understand 😩\nPlease try again 🥴🙈")
    else:
        now = datetime.now()
        response = now.strftime("%d/%m/%y\n%H:%M:%S\n\n")
        response += "🔹 Your Schedule for today📢 🔹\n\n"
        if day == "sunday":
            response += "▪️Introduction To System Programming Lecture\n12:00-13:50\nLink📎:\nhttps://tinyurl.com/y22nzm6n\n"
            response += "▪️Introduction To System Programming Practice \n14:00-15:50\nLink📎:\nhttps://tinyurl.com/y22nzm6n\n"
            bot.send_message(message.chat.id, response)
        elif day == "monday":
            response += "▪️Mathematics Logic Practice\n10:00-11:50\nLink📎:\nhttps://tinyurl.com/y22nzm6n\n"
            response += "▪️Introduction To Software Engineering Practice \n12:00-13:50\nLink📎:\nhttps://tinyurl.com/y22nzm6n\n"
            response += "▪️Mathematics Logic Lecture\n14:00-15:50\nLink📎:\nhttps://tinyurl.com/y22nzm6n\n"
            bot.send_message(message.chat.id, response)
        elif day == "tuesday":
            response += "▪️Computers Communications Lab\n8:00-9:50\nLink📎:\nhttps://tinyurl.com/y22nzm6n\n"
            response += "▪️Computers Communications Lecture\n10:00-12:50\nLink📎:\nhttps://tinyurl.com/y22nzm6n\n"
            response += "▪️Computers Communications Practice\n13:00-13:50\nLink📎:\nhttps://tinyurl.com/y22nzm6n\n"
            response += "▪️Data Structures Lecture\n18:00-19:50\nLink📎:\nhttps://tinyurl.com/y22nzm6n\n"
            bot.send_message(message.chat.id, response)
        elif day == "thursday":
            response += "▪️Data Structures Practice\n16:00-17:50\nLink📎:\nhttps://tinyurl.com/y22nzm6n\n"
            response += "▪️Data Structures Lecture\n18:00-19:50\nLink📎:\nhttps://tinyurl.com/y22nzm6n\n"
            bot.send_message(message.chat.id, response)
        elif day == "wednesday" or day == "friday" or day == "saturday":
            response = "This is your free day!\nGo to the gym 💪🏋️‍♂️👽"
            bot.send_message(message.chat.id, response)


while True:
    try:
        bot.polling()  # checking for messages
    except Exception:
        time.sleep(5)
