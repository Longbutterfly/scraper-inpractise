import requests
from bs4 import BeautifulSoup
import re

url = "https://inpractise.com/articles/n26-disrupting-banking"
print(requests.get(url).content)

def get_download(url):
    result = requests.get(url)
    soup = BeautifulSoup(result.content)
    download = soup.findall("audio")
    link = re.search("https://downloads.ctfassets.net/m2k10scfwpz8/^[a-zA-Z0-9_.-]*$.mp3", download)
    return link
