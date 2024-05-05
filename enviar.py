import sys
import telebot
import ast
import json

def envia (mensaje):
    with open("config.json", "r") as archivo:
        datos = json.load(archivo)
    tokencillo = datos["telegram"]["token"]
    chat_id = datos["telegram"]["chatid"]
    bot = telebot.TeleBot(tokencillo)
    bot.send_message(chat_id, mensaje)


