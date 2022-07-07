import ssl
from bs4 import BeautifulSoup
import urllib.request
# 让http不需要再认证
ssl._create_default_https_context = ssl._create_unverified_context

def get_text(url):
    response=urllib.request.urlopen(url)
    html=response.read()
    soup = BeautifulSoup(html,features="html.parser")
    text = soup.get_text()
    return text
#
# print(get_text("https://voiceapps.com/privacy"))
# print(transfer_nlp("https://www.stokedskills.com/privacy/escapetheroom.html"))