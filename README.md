ffm
===

fatfox module for orakel xmpp bot

Add the folowing lines to orakel.py:

#[fatfox add-in]

from fatfox import FatFox
  fatfox = FatFox()
  xmpp.add_message_listener(fatfox)
