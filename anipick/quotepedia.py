
import json
import os
import requests

try:
  from download import download
except:
  os.system('pip install download')
finally:
  from download import download

try:
  from rich.console import Console 
  konsol = Console()
  log = konsol.log
except:
  log = print

#uhh
class Quote_Anime:
  """
  #methods:
  ```
  quote
  char
  anym
  ```
  """
  base_url = 'https://animechan.vercel.app/api/random'
  r = requests.get(base_url)
  result = r.json()
  quote = result['quote']
  char = result['character']
  anime = result['anime']
  