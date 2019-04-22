#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
微信报警
'''

from wxpy import *
bot = Bot()
bot.file_helper.send('hello world!')
print("ending")