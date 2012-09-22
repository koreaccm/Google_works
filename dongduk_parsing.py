#-*- coding: cp949 -*-
import urllib
from bs4 import BeautifulSoup
from urllib.request import urlopen
html = urlopen('http://www.dongduk.ac.kr/contents/main/cor/notice.html')
soup = BeautifulSoup(html, "lxml")
print(soup)
