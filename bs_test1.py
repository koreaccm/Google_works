from bs4 import BeautifulSoup

soup = BeautifulSoup(open("sandbox_su.html"))
boxtag = soup.find_all(class_="kno-desc kno-fb-ctx")
print boxtag

