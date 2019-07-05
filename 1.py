import os
import sys
import requests
from peewee import *
from lxml import etree

resp = requests.get('https://www.jd.com/')
page = etree.HTML(resp.text)
lite0 = page.xpath('//*/div[@id="app"]/div[@id="header"]/div/div[@id="navitems"]/ul/li/a')

lite1 = page.xpath('//*/div[@id="app"]/div[@id="header"]/div/div[@id="navitems"]/ul/li/a/text()')

db = SqliteDatabase('blank.db')

class Blank (Model):
    id = PrimaryKeyField()
    text = CharField()
    href = CharField()

    class Meta:
        database = db

db.connect()
db.create_tables([Blank])

s = len(lite0)



for i in range(0,s):
    href = lite0[i].get('href')
    text = lite1[i]
    m = 'id = '+ str(i) + ',text = \'' + text + '\',href = \'' + href + '\''
    Blank.create(id = i, text = text, href = href)

for b in Blank.select():
    print(b.id, b.text, b.href)