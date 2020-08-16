import telebot
import requests
import vk
import sqlite3
import random


'''
разберись с phone

лист тип выходит из максимума :3
	@bot.message_handler(commands=['phone'])
	def welcome_start(message):
		m_1=message.text.split()
		bot.send_message(message.chat.id, "поиск : {0}".format(m_1[1]))
		i=0
		while len(massiv)>=i:
			if massiv[i][0]!=m_1[1]:
				i+=1
			else:
				bot.send_message(message.chat.id,'Ссылка : '+str(massiv[i][1]))
				break
'''
if __name__ == '__main__':
	conn = sqlite3.connect("db.db")
	c = conn.cursor()
	massiv=[]
	for row in c.execute('SELECT * FROM vk ORDER BY Link'):
		massiv.append(row)
	#print(massiv) 
	
	bot = telebot.TeleBot('1331849473:AAHxZ1cYKacvANmo1sq4CLtbBWiadzlO-os') #@db_deanon_bot

	# Тут работаем с командой start
	@bot.message_handler(commands=['start'])
	def welcome_start(message):
		file_1=open('sticker1.webp', 'rb')
		file_2=open('sticker.webp','rb')
		file_3=open('sticker2.webp','rb')
		file_4=open('sticker3.webp','rb')
		r=[file_2,file_1,file_3,file_4]
		bot.send_photo(message.chat.id,random.choice(r))
		chat_id = message.chat.username
		bot.send_message(message.chat.id,'Привет, {0}!\nНапиши /help для получения команд :3\n'.format(chat_id,bot.get_me(),
	parse_mode='html'))
	@bot.message_handler(commands=['help'])
	def help(message):
		bot.send_message(message.chat.id,"""/link <ссылка в формате vk.com/id1> (узнать номер по ссылке на вк)
/name <никнейм> (поиск по никнейму	)
P.S без указывать без <> :3
--------------------------------------------------------
Стоимость подписки на бота составляет 100р на один месяц
--------------------------------------------------------
""")
	@bot.message_handler(commands=['link'])
	def link(message):
		m_1=message.text.split()
		bot.send_message(message.chat.id, "поиск : {0}".format(m_1[1]))
		i=0
		while len(massiv)>=i:
			if massiv[i][1]!=m_1[1]:
				i+=1
			else:
				bot.send_message(message.chat.id,'Номер : '+str(massiv[i][0]))
				break

		#print(massiv)		
		#bot.send_message(message.chat.id,massiv[0][0])

	@bot.message_handler(commands=['name'])
	def name(message):
		ms=message.text.split()
		bot.send_message(message.chat.id, "поиск : {0}".format(ms[1]))		
		sites=['https://vk.com/','https://bitbucket.org/',' https://cash.me/$','https://www.chess.com/ru/member/','https://www.codecademy.com/profiles/','https://www.codewars.com/users/',
'https://www.ebay.com/usr/','https://www.facebook.com/','https://www.reddit.com/user/','https://open.spotify.com/user/','https://steamcommunity.com/id/','https://www.youtube.com/','https://github.com/']
		i=0
		while len(sites)>i:
			r=requests.post(str(sites[i])+str(ms[1]))
			if r.status_code != 404:
				bot.send_message(message.chat.id,str(sites[i])+str(ms[1]))
				i+=1
			else:
				i+=1
				
	bot.polling()

	while True: # Don't let the main Thread end.
		pass	
		'''

	'''