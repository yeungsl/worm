import urllib.request
from bs4 import BeautifulSoup

link = "http://zzk.xywy.com/"
page = urllib.request.urlopen(link)
soup = BeautifulSoup(page)
right_list = soup.find_all('ul')
print(right_list)

