#!/usr/bin/env python
import socket
import time
#import pickle

def Tcp_connect( HostIp, Port ):
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.connect((HostIp, Port))
    return

def Tcp_server_wait ( numofclientwait, port ):
	global s2
	s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	s2.bind(('',port)) 
	s2.listen(numofclientwait) 

def Tcp_server_next ( ):
	global s
	s = s2.accept()[0]

def Tcp_Write():
    print('enter the message to client:')
    a = input()
    #a = a+'\r'
    a = bytes(a, 'utf-8')
    s.send(a)
    return 

def Tcp_Read():
    
    a = s.recv(64)
    #print('received......')
    #print(a)
    #time.sleep(10)
    #print('counting to 10.....')
    a = a.decode('utf-8')
    print('received from client: {}'.format(a))
    return

def Tcp_Close( ):
    s.close()
    return 

Tcp_server_wait ( 5, 17101 )
Tcp_server_next()

while True:
    Tcp_Read()
    Tcp_Write()

Tcp_Close()
