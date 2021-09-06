import requests
import json
from googlesearch import search


class Anympedia:
  def __init__(self, title: str):
    if " " in title:
      title = title.replace(' ', '%20')
    url = f'https://api.jikan.moe/v3/search/anime?q={title}&order_by=title&sort=asc&limit=2'
    r = requests.get(url)
    res = r.json()
    self.res = res or None
#get my anime list id of anime
    mal_id = res['results'][0]['mal_id']
    self.mal_id = mal_id or None
    u = f'https://api.jikan.moe/v3/anime/{self.mal_id}'
    re = requests.get(u)
    resu = re.json()
    self.resu = resu or None
    #Anime Title
    anime = resu['title']
    self.anime = anime or None

#anime url
    anime_url = res['results'][0]['url']
    self.anime_url = anime_url or None

#image anime url
    image_url = res['results'][0]['image_url']
    self.image_url = image_url or None

#rated anime, example = PG - 13
    rated = res['results'][0]['rated']
    self.rated = rated or None

#type anime, example = TV
    type_nime = res['results'][0]['type']
    self.type = type_nime or None

#score rating anime
    score = res['results'][0]['score']
    self.score = score or None

#episode anime
    eps = res['results'][0]['episodes']
    self.eps = eps or None



#opening song
    op_song = resu['opening_themes']
    op_song = '"'.join(op_song)
    self.op_song = op_song or None

#ending song
    ed_song = resu['ending_themes']
    ed_song = '"'.join(ed_song)
    self.ed_song = ed_song or None

#aired
    aired = resu['aired']['string']
    self.aired = aired or None

#ranking
    ranknim = resu['rank']
    self.rank = ranknim or None

#popularity
    popularity = resu['popularity']
    self.popularity = popularity or None

#synopsis
    synopsis = resu['synopsis']
    self.synopsis = synopsis or None

#trailer url(EMBED)
    trailer_url = resu['trailer_url']
    self.trailer_url = trailer_url or None
#status anime
    status = resu['status']
    self.status = status or None
#premiered
    premiered = resu['premiered']
    self.premiered = premiered or None
#broadcast
    broadcast = resu['broadcast']
    self.broadcast = broadcast or None
#adaptation anime type
    try:
        adaptation_type = resu['related']['Adaptation'][0]['type']
    except:
        adaptation_type = "This Anime Doesn't Have A Manga/Anime Adaptation"
    self.adaptation_type = adaptation_type or None
#adaptation anime name
    try:
        adaptation_name = resu['related']['Adaptation'][0]['name']
    except:
        adaptation_name = "This Anime Doesn't Have A Manga/Anime Adaptation"
    self.adaptation_name = adaptation_name or None
#sequel name
    try:
        sequel_name = resu['related']['Sequel'][0]['name']
    except:
        sequel_name = "This Anime Doesn't Have A Anime Sequel"
    self.sequel = sequel_name or None
#sequel url
    try:
        sequel_url = resu['related']['Sequel'][0]['url']
    except:
        sequel_url = "This Anime Doesn't Have A Anime Sequel"
    self.sequel_url = sequel_url or None
#adaptation
    adaptation = f' {adaptation_type}, {adaptation_name}'
    self.adaptation = adaptation or None
#favorite
    favorite = resu['favorites']
    self.favorite = favorite or None
  @property
  def studio(self):
      studio = []
      for nama in self.resu['studios']:
          studio.append(nama['name'])
      studio = ', '.join(studio)
      return studio or None
  @property
  def genre(self):
      genre = []
      for nama in self.resu['genres']:
          genre.append(nama['name'])
      genre = ', '.join(genre)
      return genre or None
  @property
  def producers(self):
      producers = []
      for nama in self.resu['producers']:
          producers.append(nama['name'])
      producers = ', '.join(producers)
      return producers or None
  @property
  def recommend(self):
      recommend = []
      url = f'https://api.jikan.moe/v3/anime/{self.mal_id}/recommendations'
      su = requests.get(url)
      sult = su.json()
      self.sult = sult
      for nama in self.sult['recommendations']:
          recommend.append(nama['title'])
      recommend = recommend[:5]
      recommend = '; '.join(recommend)
      return recommend or None
  def nsfw(self) -> bool:
      return any(a in self.rated for a in ['R', '17'])