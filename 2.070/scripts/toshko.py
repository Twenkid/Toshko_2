# toshko.py
# "Toshko 2.070" POST server. Receives speech requests, returns mp3 records.
# Target: Python 2.7 
# Author: Todor Arnaudov, thanks to sample code from Python's core site and other sources
# 2-4-2016 - 13-4-2016+
# Free Bulgarian Text-to-speech synthesizer.
# http://twenkid.com/software/toshko2/
#-*-

# Настройте пътя до папката, където синтезаторът извежда файловете.
# Set the path to the mp3 output folder of Toshko 2

mp3Path = "C:\\program files\\toshko2\\mp3\\"
mp3File = "pythonSay"
mp3Ext = ".mp3"
wavExt = ".wav"

HOST_NAME = 'localhost'
PORT_NUMBER = 8079

import sys			
from sys import version as python_version
if python_version.startswith('3'):
    print("Please, use Python 2 (e.g. 2.7)! http://python.org")
    sys.exit(0)
	
import time
import BaseHTTPServer
import CGIHTTPServer 
#import t80_3	#WM_COPYDATA .. wmcopydataB  --> wmcopydata
import wmcopydata

from cgi import parse_header, parse_multipart
from urlparse import parse_qs
from BaseHTTPServer import BaseHTTPRequestHandler

import random
	
#if python_version.startswith('3'):   
    #from urllib.parse import parse_qs
    #from http.server import BaseHTTPRequestHandler
#else:
    #from urlparse import parse_qs
    #from BaseHTTPServer import BaseHTTPRequestHandler
	

class PostHandler(CGIHTTPServer.CGIHTTPRequestHandler ):
	#def __Init__(self):
	#	busy = False
	def do_HEAD(s):
		s.send_response(200)
		s.send_header("Content-type", "text/html")
		s.end_headers()
	def do_GET(s):
		"""Respond to a GET request."""
		s.send_response(200)
		s.send_header("Content-type", "text/html")
		s.end_headers()
		s.wfile.write("OK GET")        
		
	def parse_POST(self):
		ctype, pdict = parse_header(self.headers['content-type'])
		if ctype == 'multipart/form-data':
			postvars = parse_multipart(self.rfile, pdict)
		elif ctype == 'application/x-www-form-urlencoded':
			length = int(self.headers['content-length'])
			postvars = parse_qs(
					self.rfile.read(length), 
					keep_blank_values=1)
		else:
			postvars = {}
		return postvars
		
	def do_POST(self):
		try:
			print("called do_POST?")
			self.send_response(200)
			self.send_header("CAANANAAA", "text/html")
			self.end_headers()
			
			postvars = self.parse_POST()
			print(postvars)
			print(postvars["@say"])
			print(postvars["@say"][0])
			
			say = postvars["@say"][0]
			
			command = ":::f,14," + postvars["@consonants"][0] + ",7," + postvars["@vowels"][0] +";"; # + ";\n"; # + ",9" + 
			random.seed(int(time.time()))
			nn = random.randint(1000000,9999909)
			
			mp3File = "pythonSay" + str(nn)
			print(mp3File)
						
			command += "$$$"+mp3File + ";\n" # 12-4-2016
			
			print("Before say1251 = ...")

			print("BUSY... Communicating with Toshko...")
			
			#print(postvars["@say"][0](encoding='windows-1251'))
			print(command)
			say = command + say; ###### 9-4-2016

			s = say.decode(encoding='utf-8') #windows-1251')
			say = s.encode('windows-1251')
			wmcopydata.wmcopydataB(say)
			time.sleep(3) #0.250)
			# Защото изговорът е в нишка и е изговорило частично!
			# Ако няма друга синхронизация и се синтезира дълго изказване,
			# друг вариант е да се стробира например през секунда 
			# и да се следи  кога размерът на файла ще спре да расте. 
			import base64
			#pythonSay.wav.mp3
			print(mp3File)
			print(mp3Path + mp3File + wavExt + mp3Ext)
			f = open(mp3Path + mp3File + wavExt + mp3Ext , 'rb')  #with vars
			d = f.read()
			encoded = base64.b64encode(d)			
			f.close()		
			self.wfile.write(encoded)
			
			print("OK! READY for new requests");
		except:			
			print(sys.exc_info())

def cgiServer():
	server_class = BaseHTTPServer.HTTPServer
	httpd = server_class((HOST_NAME, PORT_NUMBER), PostHandler)	
	print(time.asctime(), "Toshko POST Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER))
	try:
		httpd.serve_forever()
	except KeyboardInterrupt:
		pass
	httpd.server_close()
	print(time.asctime(), "Toshko POST Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER))

	
if __name__ == '__main__':	
	cgiServer()
