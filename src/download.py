from requests import get
from io import open as iOpen
import os
from platform import system

def download(url):
    if not url.endswith("/"):
        fileName = url.split('/')[-1]
    else:
        fileName = "index.html"
    website = url.split("/")[2]     # Gets the website url eg. fazals.ddns.net google.com and so on
    path = os.getcwd() + url.replace("https://","").replace("http://","").replace(website,"").replace(fileName,"")
    if system() == "Windows":
        path = path.replace("/","\\")       # Windows uses back slashes for path instead of forward slashes
    print(path)

    response = get(url)
    # print(website)

    if not os.path.exists(path):
        os.makedirs(path)
    if not fileName == "index.html":
        f = iOpen(os.path.join(path,fileName), "wb", encoding='utf-8')
        f.write(response.content)
    else:
        f = iOpen(os.path.join(path,fileName), "w", encoding='utf-8')
        f.write(response.text.replace("https://"+website,".").replace("http://"+website,".").replace('http://192.168.0.105','.'))
    f.close

# download("http://ftm.ddns.net/")