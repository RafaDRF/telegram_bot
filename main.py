import os
import telebot
import datetime

CHAVE_API = os.environ['API_TOKEN']

bot = telebot.TeleBot(CHAVE_API)

def verificar(mensagem):
    return True

@bot.message_handler(func = verificar)
def responder(mensagem):
    print(mensagem.from_user.first_name, end=" ")
    messageTime = datetime.datetime.fromtimestamp(mensagem.date) # datetime format UTC-LOCAL
    print(messageTime)

    nome = f" {mensagem.from_user.first_name}"
    bot.reply_to(mensagem, f"Olá {nome}")

bot.polling()
