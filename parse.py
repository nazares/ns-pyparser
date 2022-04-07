#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests

x = 0

while True:
    if x == 0:
        url = "https://news.ycombinator.com/newest"
    else:
        url = "https://news.ycombinator.com/newest" + nexx

    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    titles = soup.find_all("td", class_="title")

    for title in titles:
        title = title.find("a", {'class': 'titlelink'})
        if title is not None and 'github.com' in str(title):
            link = title.get('href')
            # print("===")
            print(str(title.text) + " " + str(link))

    nx = soup.find(class_="morelink")
    if nx is not None:
        nexlink = nx.get('href')
        nexx = nexlink[6:]
        x = x + 1
    else:
        exit()
