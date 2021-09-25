# anpick
anime and manga module to get infomations from [myanimelist](https://myanimelist.net)

# Instalation
Terminal
```
python3 -m pip install -U anipick
```

CMD
```
pip install anipick
```

# Usage From Command Line(Incomplete Because Im So Lazy)
```
anipick --help/-h
```

# Import
```python
import anipick
```
# Usage Manual With Python File(Complete)

### Get Anime Info
```python
anime = anipick.Animegraphy('bofuri')

print(f'name: {anime.title}', f'description: {anime.synopsis}', sep='\n')
```

### Get Manga info
```python
manga = anipick.Mangaography('bofuri')

print(f'name: {manga.name}', f'description: {manga.synopsis}', sep='\n')
```

### Get Anime lyrics
```python
lyric = anipick.Lyricspedia('ending konosuba')
print(lyrics.lyrics_romaji)
```

### Get Anime Image and Gif
```python
pict = anipick.Animages()
print(pict.baka())
```

### Get Genshinchar
```python
char = anipick.Genshinchar
print(char('description').ayaka)
```

### Get Character info
```python
character = anipick.Charapedia('tanaka-kun')
print(f'name: {character.name}', f'about: {character.about}', f'anime refences: {character.anime}', sep='\n')
```

### Get Random Quotes From Anime
```python
quote = anipick.Quotenime()
print(quote.quote)
```

###  Get Season Anime Recomend
```python
####  Seasonal() is default now datetime
recommend = anipick.Seasonal(limit='3', years=2021, season='summer')
print(recommend.name)
```

#  ENDPOINTS

## ANIME
============

anipick.Animegraphy

#### title
#### anime_url
#### images_url
#### type
#### adaptation_type
#### aired
#### rated
#### rank
#### adaptation
#### adaptation_name
#### background
#### broadcast
#### duration
#### op_song
#### ed_song
#### eps
#### favorite
#### genre() -> list
#### mal_id
#### nsfw_scan() -> bool
#### premiered
#### popularity
#### producers
#### recommend() -> list
#### score
#### sequel
#### sequel_url
#### source
#### status
#### studio() -> list
#### synopsis
#### trailer_url

==============
## MANGA
===============

#### aird
    get aired info
#### author -> list
    get all author 
#### chapter
    get chapter info
#### favorite
    get favorite
#### genre -> list
    get all genre
#### image_url
    get image url
#### is_publishing() -> bool
    get publishing (True or False)
#### manga_id
    get manga id
#### manga_url
    get manga url
#### member
    get member
#### name
    get manga name
#### name_en
    get manga en ver name
#### name_jp
    get manga jp ver name
#### popularity
    get popularity
#### ranking
    get ranking
#### related -> list
    get related
#### score
    get scrore
#### serialization -> list
    get all serialization
#### synopsis
    get synopsis
#### status
    get manga status
#### type
    get manga type
#### volume
    get volume