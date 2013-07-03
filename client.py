#!/usr/bin/env python
# -*- coding: utf-8 -*-
#"exit" для выхода

def main():
	import socket		
	host = 'localhost'
	port = 6000
	bufsize = 1024
	
	clientsock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
	clientsock.connect( ( host, port ) )
		
	while True:
		outData = raw_input('> ')	#получаем строки с клавиатуры
		if outData == 'exit':		
			print 'bye bye'
			break
		clientsock.send( outData )
		
		inData = clientsock.recv( bufsize )
		print inData				#печатаем получаемые данные
			
	clientsock.close()
	
	return 0

if __name__ == '__main__':
	main()
