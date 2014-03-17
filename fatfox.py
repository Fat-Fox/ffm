# -*- coding: utf-8 -*-

class FatFox(object):
	def __call__(self, msg, nick, send_message):
		result = self.handle(msg.lower(),nick)
		if result:
			send_message(result)

	def handle(self, msg, nick):
		if nick == 'fatfox':
			if msg == 'ich bin nicht dick':
				return 'its fluff (http://skia.deviantart.com/art/It-s-Fluff-177820732)'
			if msg == 'was sagt man dazu':
				return 'HAHA! (http://skia.deviantart.com/art/Haha-166700813)'
			if msg == 'zeit zum basteln...':
				return 'Caution! Fox with tools! (http://culpeo-fox.deviantart.com/art/Commission-Mad-Scientist-175079567)'
