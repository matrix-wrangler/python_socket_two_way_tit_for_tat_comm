#!/usr/bin/env python
import socket
import time
import pickle

def Tcp_connect( HostIp, Port ):
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HostIp, Port))
    return

def Tcp_Write():
    a = input()
    #a = a+'\r'
    a = bytes(a, 'utf-8')
    s.send(a)
    return 

def Tcp_Read():
    a = s.recv(64)
    a = a.decode('utf-8')
    print(a)
    return

def Tcp_Close( ):
    s.close()
    return 

Tcp_connect( '192.168.107.194', 17101)

while True:
    Tcp_Write()
    Tcp_Read()

Tcp_Close()
