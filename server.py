#!/usr/bin/env python
# -*- coding: utf-8 -*-
#эхо-сервер
#закрыть по CTRL-C



def main():
	import socket			#импортируем модуль "soket"
	host="localhost"		#здесь должны указывать IP
	port=6000				#порт
	bufsize=1024			#размер получаемого/отсылаемого пакета
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)	#создаем беркли сокет для tcp
	if s==-1:
		print 'socket not created'
	s.bind((host,port))		#биндим ip:port чтобы не вмешались другие программы
	s.listen(2)				#слушаем 1 соединение
	
	while True:				#бесконечный цикл пока не break'нем
		print 'waiting for connection...'
		clientsock,addr=s.accept()		#получаем клиентский сокет?? и адрес, переводим сервер в режим ожидания подключения accept()
		print '...connected from: ',addr
		
		while True:			#еще 1 бесконечный цикл
			mdata=clientsock.recv(bufsize)	#получаем данные
			if not mdata:	#если нет данных - прерываем цикл
				print 'client ',addr,' disconnected'
				break
			print mdata		#печатаю данные на сервере
			clientsock.send(mdata) #посылаем принятые данные обратно
			
			
		clientsock.close()	#закрываем клиентский сокет??
		
	serversock.close()		#закрываем серверный сокет
	return 0

if __name__ == '__main__':
	main()
