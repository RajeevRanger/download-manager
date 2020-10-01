import requests
from bs4 import BeautifulSoup
import re
import webbrowser
import time
from qbittorrent import Client


movie = input("Enter What You Want To Download :  ")
movie_name = movie
if(len(movie.split()) > 1):
    movie = movie.split()
    movie = '%20'.join(movie)
else:
    movie = movie

url = f'https://thepiratebay10.org/search/{movie}/1/99/100,200,300,400,600'

r = requests.get(url)
htmlcontent = r.content

soup = BeautifulSoup(htmlcontent, 'html.parser')

anchors = soup.find_all("a")
all_links = []
all_names = []
all_search_links = []
for link in anchors:
    if(link.get('href') != '#'):
        linkName = link.get('title')
        linkText = link.get('href')
        all_links.append(linkText)
        if(linkName != None):
            all_names.append(linkName)
all_links = set(all_links)
all_links = list(all_links)

subsName = "Details for"
nameFinder = [i for i in all_names if subsName in i]

namelist = []
for name in nameFinder:
    if(name.startswith(subsName)):
        names = name[len(subsName)+1:]
        namelist.append(names)

for index, s in enumerate(namelist):
    print(str(index+1)+". "+s)


number_for_download = int(input("Enter number you want to download : "))-1
movie_title = namelist[number_for_download]
print("you're downloading : "+movie_title)


movie_title = movie_title.split()
movie_title = '%20'.join(movie_title)
url_selected = f'https://thepiratebay10.org/search/{movie_title}/1/99/100,200,300,400,600'

req = requests.get(url_selected)
htmlcontents = req.content

soup_selected = BeautifulSoup(htmlcontents, 'html.parser')

anchors_selected = soup_selected.find_all("a")
all_links_selected = []
for link_selected in anchors_selected:
    if(link_selected.get('href') != '#'):
        linkText_selected = link_selected.get('href')
        all_links_selected.append(linkText_selected)
all_links_selected = set(all_links_selected)
all_links_selected = list(all_links_selected)

subs2 = "magnet"
magnet_links2 = [i for i in all_links_selected if subs2 in i]


qb = Client("http://127.0.0.1:3500/")
qb.login("admin", "adminadmin")
magnet_url = magnet_links2[0]
qb.download_from_link(magnet_url)
