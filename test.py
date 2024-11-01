import telebot
#from config import API_token
from telebot.types import InlineKeyboardButton,InlineKeyboardMarkup,ReplyKeyboardMarkup



bot = telebot.TeleBot('6497653856:AAHqt39YeEOdlFGptYijL-xIPd5YMFxkJYY')

user_ID = []

button1 = InlineKeyboardButton(text="button1",url="https://google.com")
button2 = InlineKeyboardButton(text="button2", url="https://bing.com")
button3 = InlineKeyboardButton(text="button3",callback_data="btn3")
button4 = InlineKeyboardButton(text="button4", callback_data="btn4")
Inline_Keyboard = InlineKeyboardMarkup(row_width=2)
Inline_Keyboard.add(button1,button2,button3,button4)

reply_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
reply_keyboard.add(button1,button2,button3,button4)

@bot.message_handler(commands=['start'])
def welcome(messa):
    bot.send_message(messa.chat.id, 'welcome to my batlagh', reply_markup= reply_keyboard)
    # bot.register_next_step_handler(messa, process_name)
    # if messa.chat.id not in user_ID:
    #   user_ID.append(messa.chat.id)  
 ##message handling shit
# def process_name(messa):
#     name= messa.text
#     bot.send_message(messa.chat.id,f"hello {name}! how old are you?" )
#     bot.register_next_step_handler(messa, process_age)

# def process_age(messa):
#     age=messa.text
#     bot.send_message(messa.chat.id,f"you are {age} years old" )

    ##inline keyboard shits
# @bot.callback_query_handler(func=lambda call:True)
# def check_button(call):
#     if call.data == "btn1" :
#         bot.answer_callback_query(call.id, "btn1 is fucked", show_alert=True)
#     elif call.data == "btn2":
#         bot.answer_callback_query(call.id, "btn2 is pressed")

    #reply keyboard shit
@bot.message_handler(func=lambda message: True)
def check_button(message):
    if message.text == "button1":
        bot.reply_to(message, "b1")
    elif message.text == "button2":
        bot.reply_to(message, "b2")
    elif message.text == "button3":
        bot.reply_to(message, "b3")
    elif message.text == "button4":
        bot.reply_to(message, "b5")
    else:
        bot.reply_to(message, f"your message is {message.text}")



bot.polling()
