## anpick
anime and manga module to get infomations from [myanimelist](https://myanimelist.net)

## Instalation
Terminal
```
python3 -m pip install -U anipick
```

CMD
```
pip install anipick
```

## Import
```python
import anipick
```
## Usage

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