from requests import *
from telebot import TeleBot as TB
from telebot.types import InlineKeyboardMarkup as mk , InlineKeyboardButton as btn 
print(".")
print("..")
print("...")
print("....")
print(".....")
print("......")
print(".......")
print("........")
print(".........")
print("..........")
print("done✅")
bot = TB("2003578700:AAGfejhhqeXU2D6NwGRpV-MaJ2o583OksNQ")
A = btn(text="صانع بوت",url="t.me/pojavlu")
B = btn(text="قناة بوت",url="https://t.me/pojavlauncherforge")
C = btn(text="تصاميم حقوق مجاني DFG",url="https://t.me/AJ1KP0")
key = mk().add(A,B,C)
@bot.message_handler(func=lambda m:True)
def start(message):
	if message.text == "/start":
		bot.send_message(message.chat.id,"مرحبا، يمكنك في هذا بوت ارسال ايموجي وسوف يرسل لك معنى الايموجي مثل:😂 وليس تكرر ايموجي مثل: 😂😂😂 ارسل فقط واحد",parse_mode="Markdown",reply_markup=key)
	try:
		if message.text :
			u = get(f'https://dev-ooooo2oo.pantheonsite.io/Emoji.php?emoji={message.text}').json()['description']
			bot.send_message(message.chat.id,f"*{u} .*",parse_mode="Markdown",reply_markup=key)
	except:pass
bot.infinity_polling()