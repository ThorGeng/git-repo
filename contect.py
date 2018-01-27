# -*- coding: utf-8 -*-
#define:contect.py

import hashlib
import web

class Contect(object):
	def GET(self):
		try:
			data=web.input()
			if len(data)==0:
				return "hello,this is handle view"
			signature = data.signature
			timestamp = data.timestamp
			nonce = data.nonce
			echostr = data.echostr
			token = "wenquan"

			list = [token,timestamp,nonce]
			list.sort()
			sha1 = hashlib.sha1()
			map(sha1.update,list)
			hashcode = sha1.hexdigest()
			print "concect/GET func: hashcode,signture:",hashcode,signature
			if hashcode ==signature:
				return echostr
			else:
				return ""
		except exception,Argument:
			return Argument
	
