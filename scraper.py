import requests
from bs4 import BeautifulSoup
import random

response = requests.get(
  url="https://en.wikipedia.org/wiki/Web_scraping",
)
#define the parser
soup = BeautifulSoup(response.content, 'html.parser')

#scrap the title by id
title = soup.find(id="firstHeading")
#get all the links
allLinks = soup.find(id="bodyContent").find_all("a")
random.shuffle(allLinks)
linkToScrape = 0

#iterate through links and finding only containing wiki
for link in allLinks:
  # We are only interested in other wiki articles
  if link['href'].find("/wiki/") == -1:
    continue

  # Use this link to scrape
  linkToScrape = link
  break

print(linkToScrape.string)



