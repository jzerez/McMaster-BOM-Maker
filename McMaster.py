"""
Jonathan Zerez, Summer 2018
This script takes a URL, part number, and quantity needed as an input, and
returns important info, such as price, units needed, etc.
"""
from bs4 import BeautifulSoup
import urllib.request as urllib2
import os

def scrape(id, qty):
    id = id.lower()
    if "mcmaster.com" in id:
        part_num = id.split("mcmaster.com")[-1]
        url = "http://www.McMaster.com" + part_num
    else:
        part_num = id.split("#")[-1]
        url = "http://www.McMaster.com/#" + part_num

    print(url)
    html = urllib2.urlopen(url).read()
    soup = BeautifulSoup(html, 'lxml')
    #dom = BeautifulSoup.BeautifulSoup(dom)
    print(soup.prettify())

    for price in soup.find_all('p'):
        print(price.get_text())
        #if '$' in price.get_text():
        #    print(price.get_text())

if __name__ == '__main__':
    url = ("https://www.mcmaster.com/#1946K44/")
    scrape(url, 1)
