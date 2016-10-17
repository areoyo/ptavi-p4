  #!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""
import sys
import socketserver

PORT = int(sys.argv[1])

class SIPRegisterHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """
    misdatos = {}
    
    def handle(self):
        print ('IP del cliente: ' + self.client_address[0])
        print ('PUERTO del cliente: ' + str(self.client_address[1]) + '\n')
        datos = self.rfile.read().decode('utf-8').split()
        print (datos[-1])
        if datos[0] == 'REGISTER':
            self.misdatos[datos[1]] = self.client_address[0]
            self.wfile.write(b"SIP/2.0 200 OK\r\n\r\n")
            if int(datos[-1]) == 0:
                del self.misdatos[datos[1]]
        print (self.misdatos)
        
if __name__ == "__main__":
    serv = socketserver.UDPServer(('', PORT), SIPRegisterHandler)
    print("Lanzando servidor UDP de eco...")
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Finalizado servidor")
