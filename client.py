#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente UDP que abre un socket a un servidor
"""
import sys
import socket

# Constantes. Dirección IP del servidor y contenido a enviar

SERVER = sys.argv[1]
PORT = int(sys.argv[2])
METODO = sys.argv[3]
LINE = sys.argv[4]
EXPIRES = sys.argv[5]

#SERVER = 'localhost' #string
#PORT = 6001          #int
#LINE = '¡Hola mundo!'#string

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
    my_socket.connect((SERVER, PORT))
    if METODO == 'register':
        LINE = 'REGISTER sip:' + LINE + ' SIP/2.0\r\n' + 'Expires: ' + EXPIRES + '\r\n'
    print("Enviando:", LINE)
    my_socket.send(bytes(LINE, 'utf-8') + b'\r\n')
    data = my_socket.recv(1024)
    print('Recibido -- ', data.decode('utf-8'))

print("Socket terminado.")
#sage: client.py ip puerto register sip_address expires_value
