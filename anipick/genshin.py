from database import genshindata
char = genshindata.character

class character:
  def diluc(query):
    diluc = char[0][query]
    
print(character.diluc('name').diluc)