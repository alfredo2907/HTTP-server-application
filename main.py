#!/usr/bin/python3.7
# -- coding: utf-8 --

import os
import time
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = "localhost"
serverPort = 8099
response = os.system("ping -c 5 " + hostName)

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.endswith("/ping"):
            if response == 0:
              print(hostName, "is up!")
              self.send_response(200)
              self.send_header("Content-type", "text/html")
              self.end_headers()
              self.wfile.write(bytes("<html><body><h1> Health check is OK </h1></body></html>", "utf-8"))

            else:
              print(hostName, "is down!")
              self.send_response(200)
              self.send_header("Content-type", "text/html")
              self.end_headers()
              self.wfile.write(bytes("<html><body><h1> Health check isn't OK </h1></body></html>", "utf-8"))
              sys.exit()

        if self.path.endswith("/datetime"):
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
            self.wfile.write(bytes('{"time": "'+ date + '"}', "utf-8"))

    def do_POST(self):
        if self.path.endswith("/ping"):
            if response == 0:
              print(hostName, "is up!")
              self.send_response(200)
              self.send_header("Content-type", "text/html")
              self.end_headers()
              self.wfile.write(bytes("<html><body><h1> Health check is OK </h1></body></html>", "utf-8"))

            else:
              print(hostName, "is down!")
              self.send_response(200)
              self.send_header("Content-type", "text/html")
              self.end_headers()
              self.wfile.write(bytes("<html><body><h1> Health check isn't OK </h1></body></html>", "utf-8"))
              sys.exit()

        if self.path.endswith("/datetime"):
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
            self.wfile.write(bytes('{"time": "'+ date + '"}', "utf-8"))

if response == 0:
    server = HTTPServer(("0.0.0.0",serverPort), MyServer)
    print("Server is Running...")
    server.serve_forever()
    server.server_close()
    print("Server stoped.")
else:
    print("Server is not Running...")
