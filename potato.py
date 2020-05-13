# -*- coding: UTF-8 -*-
__title__ = 'potato'
__version__ = '1.0.0'
__author__ = '@gyscordia'
__license__ = 'MIT'
__copyright__ = 'Copyright 2020 by Me'

try:
    from googlesearch import search
except ImportError:
    print("dammmm..")


import googlesearch
import os
import sys
from datetime import datetime
agente = googlesearch.get_random_user_agent()
data = str(datetime.today())
horario = data[0:19]
print("getting urls... {}".format(horario))


try:
    for j in search(query=sys.argv[1], tld=sys.argv[2], lang=sys.argv[3], num=int(sys.argv[4]), stop=int(sys.argv[4]), pause=5, user_agent=agente):
        print(j)
except IndexError:
    print('try: '+ __file__ + ' search (query you want to use) com(top level domain) language(pt-br, en) num(number of urls, eg. 10)')
    print('example: '+ __file__ + ' noticias com pt-br 50')
