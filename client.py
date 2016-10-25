#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente UDP que abre un socket a un servidor
"""
import sys
import socket

# Constantes. Dirección IP del servidor y contenido a enviar
if len(sys.argv) != 6:
    sys.exit("Usage: client.py ip puerto register sip_address expires_value")
_, SERVER, PORT, METODO, LINE, EXPIRES = sys.argv
PORT = int(PORT)

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
    my_socket.connect((SERVER, PORT))
    if METODO == 'register':
        LINE = 'REGISTER sip:' + LINE + ' SIP/2.0\r\n' + 'Expires: ' + EXPIRES + '\r\n\r\n'
    print("Enviando:", LINE)
    my_socket.send(bytes(LINE, 'utf-8') + b'\r\n')
    data = my_socket.recv(1024)
    print('Recibido -- ', data.decode('utf-8'))

print("Socket terminado.")
