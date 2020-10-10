from bs4 import BeautifulSoup
from requests import get
from io import open as iOpen
from src.download import download

mainUrlSet = {"http://ftm.ddns.net/"}
alreadyCrawled = set()

# Functions Start

def crawlThrough(url):
    response = get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    anchorTags = soup.findAll("a")
    website = url.split("/")[2]

    urlsToCrawl = set()

    for hrefs in anchorTags:
        href = hrefs.get("href")
        if href is None:
            continue
        elif (href.startswith("http") or href.startswith("https")) and (website in href):
            urlsToCrawl.add(href)
    return urlsToCrawl

# Functions End


previouslyCrawled = 0
numberOfIteration = 10
while numberOfIteration > 0:
    print("Crawling", str(len(mainUrlSet)), "URLs")
    for url in mainUrlSet:
        if url is None:
            continue
        elif url.endswith("/") and not (url in alreadyCrawled):
            print(url)
            alreadyCrawled.add(url)
            mainUrlSet = mainUrlSet.union(crawlThrough(url))
    numberOfIteration = numberOfIteration - 1

dataToWrite = ""
for i in alreadyCrawled:
    dataToWrite = dataToWrite + "\n" + i
with iOpen("crawled.txt", "w") as f:
    f.write(dataToWrite)
    f.close

dataToWrite = ""
for i in mainUrlSet:
    dataToWrite = dataToWrite + "\n" + i
with iOpen("all.txt", "w") as f:
    f.write(dataToWrite)
    f.close

print("Crawled", str(len(alreadyCrawled)), "URLs of",str(len(mainUrlSet)),"found")
for i in alreadyCrawled:
    download(str(i))