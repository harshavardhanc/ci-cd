#!/usr/bin/python
import subprocess,os
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer

PORT_NUMBER = 80

class myHandler(BaseHTTPRequestHandler):

  #Handler for the GET requests
  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type','text/html')
    self.end_headers()
    # Send the html message
    self.wfile.write("Hello! \n")
    self.wfile.write("Hostname is : " + subprocess.check_output("uname -n", shell=True))
    self.wfile.write("Process ID  : " + str(os.getpid()))
    return

try:
  server = HTTPServer(('', PORT_NUMBER), myHandler)
  print 'Started httpserver on port ' , PORT_NUMBER

  server.serve_forever()

except KeyboardInterrupt:
  print '^C received, shutting down the web server'
  server.socket.close()
