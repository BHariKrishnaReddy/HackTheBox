import requests                                           // to make connection with web  
from bs4 import BeautifulSoup
import hashlib
url=input("Enter the value")
r=requests.session()
re=r.get(url)
soup =BeautifulSoup(re)
s=soup.select('h3')[0].text
h = hashlib.md5(s.encode('utf-8')).hexdigest
sr=r.post(url=url,data={'hash':h})
sr.text                                                   //output
