#-*- coding: cp949 -*-
import urllib
from bs4 import BeautifulSoup
from urllib.request import urlopen
html = urlopen('http://comic.naver.com/webtoon/weekday.nhn')
soup = BeautifulSoup(html, "lxml")
titles = soup.find_all("a", "title")
 
for title in titles:
    print ('title:{0:10s} link:{1:20s}굈'.format(title['title'], title['href'].encode('utf-8')))
