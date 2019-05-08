#!/usr/bin/env python
# -*- coding: utf-8 -*-

#MathBot - BetaTest
#Telegram: @answermebitch

#imports
import telepot
import math
import time
import re
import os

#api do bot
api = ''
bot = telepot.Bot(api)

### funções individuais ###

# função de elevar ao quadrado
def elevar(f):
	return f**2

# função de elevar de elevar ao cubo
def elevar(w):
	return w**3

# função de elevar base e expoente
def elevar_base_expoente(x,y):
	return x**y

# função de divisão
def divisao(e,t):
	return e/t

# função de multiplicar para saber a circunferencia
def calc_circ(b):
	return b * 2 * 3.14

# função de soma
def soma(n,m):
	return n+m

# função de subtração
def sub(l,p):
	return l-p

# função de multiplicação
def mul(k,j):
	return k*j

# função handle
def handle(msg):
	uid = msg['from']['id']
	firstname = msg['from']['first_name']
	chat_id = msg['chat']['id']
	chat_type = msg['chat']['type']
	try:
		user = '@' + msg['from']['username']
	except:
		print ''
	msgid = msg['message_id']

	content_type, chat_type, chat_id = telepot.glance(msg)
	if msg.get('text'):
		texto = msg['text'].split()[0]
		log = open('log_math.txt','a')
		messagelog = open('messagelog.txt','a')
		if texto == '/start':
			if chat_type == 'private':
				bot.sendMessage(chat_id, 'Sou um bot de matemática desenvolvido por laps3', reply_to_message_id=msgid)
				print '[+] BOT STARTED'
				log.write(time.asctime())
				log.write('Command: ' + texto + '\nFirst Name: ' + firstname + '\n\n')
				log.close()
			elif chat_type == 'supergroup':
				bot.sendMessage(chat_id, 'Sou um bot de matemática desenvolvido por laps3', reply_to_message_id=msgid)
				log.write(time.asctime())
				log.write('Command: ' + texto + '\nFirst Name: ' + firstname + '\n\n')
				log.close()
		elif texto == '/multipl':
			multi1 = int(msg['text'].split()[1])
			multi2 = int(msg['text'].split()[2])
			multi3 = mul(multi1,multi2)
			bot.sendMessage(chat_id, 'Resultado: ' + str(multi3), reply_to_message_id=msgid)
			log.write(time.asctime())
			log.write('Command: ' + texto + '\nFirst Name: ' + firstname + '\n\n')
			log.close()
		elif texto == '/subt':
			sub1 = int(msg['text'].split()[1])
			sub2 = int(msg['text'].split()[2])
			sub3 = sub(sub1,sub2)
			bot.sendMessage(chat_id, 'Resultado: ' + str(sub3))
			log.write(time.asctime())
			log.write('Command: ' + texto + '\nFirst Name: ' + firstname + '\n\n')
			log.close()
		elif texto == '/som':
			soma1 = int(msg['text'].split()[1])
			soma2 = int(msg['text'].split()[2])
			soma3 = soma(soma1,soma2)
			bot.sendMessage(chat_id, 'Resultado: ' + str(soma3), reply_to_message_id=msgid)
			print '[+] SOMA USED'
			log.write(time.asctime())
			log.write('Command: ' + texto + '\nFirst Name: ' + firstname + '\n\n')
			log.close()
		elif texto == '/div':
			div1 = int(msg['text'].split()[1])
			div2 = int(msg['text'].split()[2])
			div3 = divisao(div1,div2)
			bot.sendMessage(chat_id, 'Resultado: ' + str(div3), reply_to_message_id=msgid)
			print '[+] DIV USED'
			log.write(time.asctime())
			log.write('Command: ' + texto + '\nFirst Name: ' + firstname + '\n\n')
			log.close()
		elif texto == '/id':
			bot.sendMessage(chat_id, uid, reply_to_message_id=msgid)
			print '[+] ID PRINTED'
			log.write(time.asctime())
			log.write('Command: ' + texto + '\nFirst Name: ' + firstname + '\n\n')
			log.close()
		elif texto == '/base_expoente':
			base_expoent = int(msg['text'].split()[1])
			base_expoen = int(msg['text'].split()[2])
			ex = elevar_base_expoente(base_expoent,base_expoen)
			bot.sendMessage(chat_id, 'Resultado: ' + str((ex)), reply_to_message_id=msgid)
			print '[+] BASE_EXPOENTE CALCULED'
			log.write(time.asctime())
			log.write('Command: ' + texto + '\nFirst Name: ' + firstname + '\n\n')
			log.close()
		elif texto == '/calc_circu':
			mult = int(msg['text'].split()[1])
			multi = int(calc_circ(mult))
			bot.sendMessage(chat_id, 'A circuferência é: ' + str(multi), reply_to_message_id=msgid)
			log.write(time.asctime())
			log.write('Command: ' + texto + '\nFirst Name: ' + firstname + '\n\n')
			log.close()
		elif texto == '/help':
			helpcommand = open('help.txt','r')
			helpcommand_read = helpcommand.read()
			bot.sendMessage(chat_id, helpcommand_read, reply_to_message_id=msgid)
			helpcommand.close()
			print '[+] HELP PRINTED'
			log.write(time.asctime())
			log.write('Command: ' + msg['text'][0:] + '\nFirst Name: ' + firstname + '\n\n')
			log.close()
		elif msg.get('text'):
			messagelog.write(time.asctime() + '\n')
			messagelog.write('Command: ' + msg['text'][0:] + ' First Name: ' + firstname + '\n\n')
			messagelog.close()
		elif msg.get('text'):
			print msg['text'][0:]
	elif msg.get('new_chat_member'):
		print '[+] NEW MEMBER ' + user
		bot.sendMessage(chat_id, 'Bem vindo ' + user)
bot.message_loop(handle)
print '[+] ON'
while 1:
	pass
