
from .database import genshindata
char = genshindata.character

class Genshinchar:

  help = '''
  endpoints:
  character('name')
  character('id')
  character('slug')
  character('descriptiom')
  character('weapon')
  character('obtain')
  character('gender')
  character('rarity')
  character('birthday')
  character('vision')
  '''
  def __init__(self, query: str):
    try:
      diluc = char[0][query]
      self.diluc = diluc or None
      jean = char[1][query]
      self.jean = jean or None
      keqing = char[2][query]
      self.keqing = keqing or None
      klee = char[3][query]
      self.klee = klee
      mona = char[4][query]
      self.mona = mona or None
      qiqi = char[5][query]
      self.qiqi = qiqi or None
      venti = char[6][query]
      self.venti = venti or None
      xiao = char[7][query]
      self.xiao = xiao or None
      tartanglia = char[8][query]
      self.tartanglia = tartanglia or None
      zhongli = char[9][query]
      self.zhongli = zhongli or None
      amber = char[10][query]
      self.amber = amber or None
      barbara = char[11][query]
      self.barbara = barbara or None
      beidou = char[12][query]
      self.beidou = beidou or None
      bennnett = char[13][query]
      self.bennett = bennnett or None
      chongyun = char[14][query]
      self.chongyun = chongyun or None
      fischl = char[15][query]
      self.fischl = fischl or None
      kaeya = char[16][query]
      self.kaeya = kaeya or None
      lisa = char[17][query]
      self.lisa = lisa or None
      ningguang = char[18][query]
      self.ningguang = ningguang or None
      noelle = char[19][query]
      self.noelle = noelle or None
      razor = char[20][query]
      self.razor = razor or None
      sucrose = char[21][query]
      self.sucrose = sucrose or None
      xiangling = char[22][query]
      self.xianling = xiangling or None
      xiangqiu = char[23][query]
      self.xiangqiu = xiangqiu or None
      diona = char[24][query]
      self.diona = diona or None
      xinyan = char[25][query]
      self.xinyan = xinyan or None
      ayaka = char[26][query]
      self.ayaka = ayaka or None
      baal = char[27][query]
      self.baal = baal or None
    except KeyError:
      raise KeyError('''Not in endpoints, for help in help, example: id = character('id'), print(id.help), or print(character.help''')

