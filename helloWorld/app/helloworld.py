import os
import SocketServer
import webserver
import response_handler as myApp
from helloworld_doc import defaultPage
from flask import Flask, request

SocketServer.ThreadingTCPServer.allow_reuse_address = True

app = Flask(__name__)

@app.route("/")
def main():
    return defaultPage

@app.route("/v1/")
def mainV1():
    return defaultPage

@app.route("/alexa/")
def mainAlexa():
    return defaultPage

@app.route("/v1/helloWorld",methods = ['GET','POST'])
def apicalls():
    if request.method == 'POST':
        req = request.get_json()
        #print "POST request"
        response = myApp.request_handler(req)
        return response + "\n"
    else:
        #print "GET request:", request
        return "Hello World!!"

def run_webserver():
    webserver.run(app)

if __name__ == "__main__":
    run_webserver()
