# https://stackoverflow.com/questions/23264569/python-3-x-basehttpserver-or-http-server
# https://www.urldecoder.io/python/#:~:text=URL%20Decoding%20query%20strings%20or%20form%20parameters%20in,UTF-8encoding%20by%20default.%20Let%E2%80%99s%20see%20an%20example%20-

import http.server
import socketserver
import urllib.parse
import random
import time

from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = 'localhost'
hostPort = 9000

MAX_PRICE = 100.0
MAX_PRICE_CHANGE = 0.02

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        form = {}
        if self.path.find('?') > -1:
            queryStr = self.path.split('?')[1]
            form = dict([queryParam.split('=') for queryParam in queryStr.split('&')])
            
            body = '['

            if 'q' in form:
                quotes = []

                for symbol in urllib.parse.unquote_plus(form['q']).split(' '):
                    price = random.random() * MAX_PRICE
                    change = price * MAX_PRICE_CHANGE * (random.random() * 2.0 - 1.0)
                    quotes.append(('{"symbol":"%s","price":%f,"change":%f}' % (symbol, price, change)))

                body += ','.join(quotes)

            body += ']'

        if 'callback' in form:
            body = ('%s(%s);' % (form['callback'], body))

        self.send_response(200)
        self.send_header('Content-type', 'text/javascript')
        self.send_header('Content-Length', len(body))
        self.send_header('Expires', '-1')
        self.send_header('Cache-Control', 'no-cache')
        self.send_header('Pragma', 'no-cache')
        self.end_headers()

        self.wfile.write(bytes(body, 'utf-8'))
        self.wfile.flush()


myServer = HTTPServer((hostName, hostPort), MyHandler)
print(time.asctime(), 'Server Starts - %s:%s' % (hostName, hostPort))

try:
    myServer.serve_forever()
except KeyboardInterrupt:
    pass

myServer.server_close()
print(time.asctime(), "Server Stops - %s:%s" % (hostName, hostPort))