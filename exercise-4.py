# Создать телеграм-бота, который считывает входящие сообщения и выдает сколько раз повторяются в этом сообщении
# гласные буквы. Для простоты считайте, что все сообщения будут присылаться на латинице. Не забывайте, что гласные буквы
# могут быть в верхнем регистре

import telebot

bot = telebot.TeleBot("2114922619:AAGRZzL8T5Oi87tTOMAHRrIJqFtefqQYNUs")

letters = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
@bot.message_handler(commands=['start'])
def start_message(message):
	bot.send_message(message.chat.id, 'Hello')

@bot.message_handler(content_types=['text'])
def text_message(message):
	count = 0

	for i in message.text:
		if i in letters:
			count += 1

	bot.send_message(message.chat.id, count)

bot.polling()