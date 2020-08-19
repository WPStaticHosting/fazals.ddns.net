from urllib import request
from bs4 import BeautifulSoup
import re
import io


url = input("Enter the URL to the Sitemaps Index\nLeave blank for using default:\n")
if len(url) < 1:
    url = "http://ftm.ddns.net/sitemap_index.xml"

handle = request.urlopen(url).read()
soup = BeautifulSoup(handle, 'html.parser')
sitemapTags = soup.find_all("loc")
sitemapURLList = [url]

for sitemaps in sitemapTags:
    if sitemaps.string.endswith(".xml"):
        sitemapURLList.append(sitemaps.string)

wantToReplace = input("Do you want to replace text in files?\ntype 'y' for yes or 'n' for no: ")
if wantToReplace == 'y':
    textToReplace = input("enter the text to replace: ")
    textToBeReplacedWith = input("enter the text to be replaced with: ")

for linksFromSitemaps in sitemapURLList:
    if wantToReplace == "y":
        textData = request.urlopen(linksFromSitemaps).read().decode().replace(textToReplace,textToBeReplacedWith)
    else:
        textData = request.urlopen(linksFromSitemaps).read().decode()
    with io.open(linksFromSitemaps.split("/")[-1], "w", encoding="utf-8") as fileToBeWritten:
        fileToBeWritten.write(textData)
        fileToBeWritten.close()