import requests
from requests.exceptions import MissingSchema
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

def search(term, num_results=10, lang="en") -> list:
    
    user_agent = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/61.0.3163.100 Safari/537.36'
        }

    def fetch_results(search_term, number_results, language_code):
        escaped_search_term = search_term.replace(' ', '+')

        google_url = 'https://www.google.com/search?q={}&num={}&hl={}'.format(escaped_search_term, number_results+1,
                                                                              language_code)
        response = Request(url = google_url, headers = user_agent)
        response_open = urlopen(response)

        return response_open.read()

    def parse_results(raw_html):
        
        soup = BeautifulSoup(raw_html, 'html.parser')
        result_block = soup.find_all('div', attrs={'class': 'g'})
        for result in result_block:
            link = result.find('a', href=True)
            title = result.find('h3')
            if link and title:
                yield link['href']

    html = fetch_results(term, num_results, lang)
    return list(parse_results(html))
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