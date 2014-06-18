# -*- coding: utf-8 -*-
# Python 3.4.1

import urllib.parse, urllib.request, http.cookiejar, json, datetime, re

"""cookie"""

cookie = http.cookiejar.CookieJar()
chandle = urllib.request.HTTPCookieProcessor(cookie)

def get(url, header = False):
	if header:
		r = urllib.request.Request(url, headers = header)
	else:
		r = urllib.request.Request(url)
	opener = urllib.request.build_opener(chandle)
	u = opener.open(r)
	data = u.read()
	try:
		data = data.decode('utf-8')
	except:
		data = data.decode('gbk', 'ignore')
	return data

def post(url, data, header = False):
	data = urllib.parse.urlencode(data)
	data = bytes(data,'utf-8')
	if header:
		r = urllib.request.Request(url, data, headers = header)
	else:
		r = urllib.request.Request(url, data)
	opener = urllib.request.build_opener(chandle)
	u = opener.open(r)
	data = u.read()
	try:
		data = data.decode('utf-8')
	except:
		data = data.decode('gbk', 'ignore')
	return data

if __name__=="__main__":
	pass
