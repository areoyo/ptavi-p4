#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""
import sys
import time
import socketserver
import json

class SIPRegisterHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """
    misdatos = {}
    
    def register2json(self):
        json.dump(self.misdatos, open('registered.json', 'w'))
    
    def json2registered(self):
        try:
            with open('registered.json') as client_file:
                self.misdatos = json.load (client_file)
        except:
            self.register2json()
    
    def time_out(self):
        cliente = []
        for client in self.misdatos:
            time_expires = self.misdatos[client]['expires']
            time_expire = time.strptime(time_expires, '%Y-%m-%d %H:%M:%S')
            if time_expire <= time.gmtime(time.time()):
                cliente.append(client)
        for hora in cliente:
            del self.misdatos[hora]
                 
    def handle(self):        
        datos = self.rfile.read().decode('utf-8').split()
        if datos[0] == 'REGISTER':
            self.hora = float(time.time()) + float(datos[-1])            
            self.expires = time.strftime('%Y-%m-%d %H:%M:%S', 
                                         time.gmtime(self.hora))
            self.datoscliente = {'address': self.client_address[0], 'expires': self.expires}
            self.misdatos[datos[1].split(':')[-1]] = self.datoscliente
            if int(datos[-1]) == 0:
                del self.misdatos[datos[1].split(':')[-1]]     
        self.wfile.write(b"SIP/2.0 200 OK\r\n\r\n")
        self.time_out()
        self.register2json()
        print (self.misdatos)
        
if __name__ == "__main__":
    serv = socketserver.UDPServer(('', int(sys.argv[1])), SIPRegisterHandler)
    print("Lanzando servidor UDP de eco...")
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Finalizado servidor")
