#!/usr/bin/env python
# -*- coding: utf-8 -*-
#"exit" для выхода

def main():
	import socket		
	host='localhost'
	port=6000
	bufsize=1024
	
	clientsock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	clientsock.connect((host,port))
		
	while True:
		mdata=raw_input('> ')	#получаем строки с клавиатуры
		if mdata=='exit':		#для выхода
			print 'bye bye'
			break
		clientsock.send(mdata)
		mdata=clientsock.recv(bufsize)
		print mdata				#печатаем получаемые данные
			
	clientsock.close()
	
	return 0

if __name__ == '__main__':
	main()
