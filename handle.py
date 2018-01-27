# -*- coding: utf-8 -*-
#filename: handle.py

import hashlib
import web
import reply
import receive

class Handle(object):
	def POST(self):
		try:
			webData = web.data()
			print "Handle Post webdata is ",webData #后台打日志
			recMsg = receive.parse_xml(webData)
			if isinstance(recMsg,receive.Msg):
				toUser = recMsg.FromUserName
				fromUser = recMsg.ToUserName
				if recMsg.MsgType =='text':
					content = recMsg.Content
					replyMsg = reply.TextMsg(toUser, fromUser, content)
					return replyMsg.send()
				if recMsg.MsgType =='image':
					mediaid = recMsg.MediaId
					replyMsg = reply.ImageMsg(toUser, fromUser, mediaid)
					return replyMsg.send()
				else:
					return reply.Msg().send()
			else:
				print "暂不处理"
				return reply.Msg().send()
		except Exception, Argment:
				return Argment
