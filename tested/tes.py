
from bs4 import BeautifulSoup
import requests
import json
title = input()
animm = anipick.Anympedia(title)
a = f'''{animm.genre}\n
op song: {animm.op_song}\n
ed song: {animm.ed_song}\n
title: {animm.anime}\n
trailer: {animm.trailer_url}\n
aired: {animm.aired}\n
type: {animm.type}\n
episode: {animm.eps}\n
score: {animm.score}\n
status: {animm.status}\n
id: {animm.mal_id}\n
popularity: {animm.popularity}\n
image: {animm.image_url}\n
rank: {animm.rank}\n
rated: {animm.rated}\n
sysnopsis: {animm.synopsis}\n
anime url: {animm.anime_url}\n
producers: {animm.producers}\n
adaptation: {animm.adaptation}\n
sequel: {animm.sequel}\n
        {animm.sequel_url}\n
broadcast: {animm.broadcast}\n
premiered: {animm.premiered}\n
recommendation: {animm.recommend}\n
studio: {animm.studio}\n
favorites: {animm.favorite}\n
'''
url = requests.get('https://myanimelist.net/anime/46471/Tantei_wa_Mou_Shindeiru')
soup = BeautifulSoup(url.content, 'html.parser')

dark = soup.findAll('span', {'class':'dark_text'})

