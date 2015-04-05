__author__ = 'Hanz'
from SocketServer import TCPServer, StreamRequestHandler

class Handler(StreamRequestHandler):

    def handle(self):
        addr = self.request.getpeername()
        print 'Got connection from', addr
        self.wfile.write('Thank you for your connecting !')

server = TCPServer(('', 1234), Handler)
server.serve_forever()

