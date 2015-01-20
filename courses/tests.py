#from django.test import TestCase
# coding=utf-8

# Create your tests here.
from django import forms
from models import Article

import datetime
import codecs

def myDate(date):
	dt = datetime.datetime.today()

	if date.year == dt.year and date.month == dt.month and date.day == dt.day:
		res = "今天"
	else:
		res = str(date.month) + "月" + str(date.day)+ "日"

	res = res + str(date.hour) + ":" + str(date.minute)
	return res

dd = datetime.datetime(1974, 9, 4, 18, 17, 30)

dt = datetime.datetime.now()

d = myDate(dt)

print unicode(d, "cp936")

d = myDate(dd)
print unicode(d, "cp936")



#print dt.date.year
#print dt.time.hour
#print dt
#print dt.year
#print dt.month
