#!/usr/bin/env python3
"""
Very simple HTTP server in python for logging requests
Usage::
    ./server.py [<port>]
    
based on this example:  https://gist.github.com/mdonkers/63e115cc0c79b4f6b8b3a6b797e485c7

"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
import zlib

class S(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        #logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
        #        str(self.path), str(self.headers), post_data.decode('utf-8'))

        bytes_hex = bytes.fromhex(post_data.decode("utf-8"))
        decompressed = zlib.decompress(bytes_hex)
        logging.info("decompressed = %s", decompressed)

        self._set_response()
        self.wfile.write(decompressed)

def run(server_class=HTTPServer, handler_class=S, port=2112):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')

if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
