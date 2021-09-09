import requests
from requests.exceptions import MissingSchema
from bs4 import BeautifulSoup
from googlesearch import search
class Lyricspedia:
    def __init__(self, title: str):
        anu = search('site:animesonglyrics.com {}'.format(title), num_results=0)
        abu = ''.join(anu)
        try:
            url = requests.get(abu)
        except MissingSchema:
            pass
            error = 'No Results Found'
            raise MissingSchema(error)
        
        soup = BeautifulSoup(url.content, 'html.parser')
        lyrics_romaji = soup.find('div', {'id': 'tab1'})
        lyrics_romaji = str(lyrics_romaji)
        lyrics_romaji = lyrics_romaji.replace('<br/>', '\n')
        lyrics_romaji = lyrics_romaji.replace('''<div class="correct">[
                                            <a data-target="#romModal" data-toggle="modal" href="#">Correct these Lyrics</a> ]</div></div>''', '')
        lyrics_romaji = lyrics_romaji.replace('<hr/>', '')
        lyrics_romaji = lyrics_romaji.replace('''<div class="tab-pane fade in active" id="tab1">''', '')
        self.lyrics_romaji = lyrics_romaji or None
        lyrics_en = soup.find('div', {'id': 'tab2'})
        lyrics_en = str(lyrics_en)
        lyrics_en = lyrics_en.replace('<br/>', '\n')
        lyrics_en = lyrics_en.replace('''<div class="correct">[
                                            <a data-target="#engModal" data-toggle="modal" href="#">Correct these Lyrics</a> ]</div></div>''', '')
        lyrics_en = lyrics_en.replace('<hr/>', '')
        lyrics_en = lyrics_en.replace('''<div class="tab-pane fade" id="tab2">''', '')
        self.lyrics_en = lyrics_en or None
        name = soup.find('div', {'id': 'wrapper'})
        name = name.h1.text
        name = name.replace('                ','')
        self.name = name