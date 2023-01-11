import telebot
import requests


API_TOKEN = '5761948695:AAEWDCLtbSbIaE-tZUBe0t_6SqSv6lis8go'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am MessageSender bot.
I am sending messages from API\
""")

@bot.message_handler(func=lambda message: True)
def token_message(message):
    chat_id = message.chat.id
    URL = "http://127.0.0.1:8000/user/"
    DATA = {
	            "tg_chat_id":chat_id
            }
    HEADERS = {'Authorization':"Bearer "+str(message.text)}
    r = requests.post(url = URL, headers = HEADERS, data=DATA)
    if r.status_code==201:
        answer="Спасибо что используюте этот сервис, ваш аккаунт сохранен"
    else:
        detail = r.json()['detail']
        answer=str
        if detail == "You already registered":
            answer="Вы уже указали свой token"
        elif detail == "Given token not valid for any token type":
            answer="Ваш token не валидный"
        elif detail == "This user is used by other telegram account":
            answer="На этот телеграм аккаунт уже привязан другой token"
        else:
            answer="Спасибо что используюте этот сервис, ваш аккаунт сохранен"
    bot.reply_to(message, answer)
    print(chat_id)

bot.infinity_polling()
