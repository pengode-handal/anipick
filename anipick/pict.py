
from requests import get
from random import choice

class Animages:
        url1 = 'https://nekos.best/api/v1/'
        url2 = 'https://api.waifu.pics/sfw/'
        url3 = 'https://purrbot.site/api/img/sfw/'
        @classmethod
        def pict(anu, url: str) -> str:
            re = get(url).json()
            try:
                return re['url']
            except:
                return re['link']
        @classmethod
        def neko(anu):
            """Neko random images"""
            nekoo = choice(['neko/img', 'neko/gif'])
            nekoo = choice([anu.url3 + nekoo, 'https://api.waifu.pics/sfw/neko', anu.url1 + 'nekos'])
            return anu.pict(nekoo)
        @classmethod
        def bite(anu):
            """Bite anime random images"""
            bite = choice([anu.url1 + 'bite', anu.url2 + 'bite', anu.url3 + 'bite/gif'])
            return anu.pict(bite)
        @classmethod
        def blush(anu):
            "blush random image"
            blush = choice([anu.url3 + 'blush/gif', anu.url1 + 'blush', anu.url2 + 'blush'])
            return anu.pict(blush)
        @classmethod
        def waifu(anu):
            return anu.pict(anu.url2 + 'waifu')
        @classmethod
        def baka(anu):
            return anu.pict(anu.url1 + 'baka')
        @classmethod
        def bored(anu):
            return anu.pict(anu.url1 + 'bored' )
        @classmethod
        def cry(anu):
            cry = choice([anu.url3 + 'cry/gif', anu.url2 + 'cry', anu.url1 + 'cry'])
            return anu.pict(cry)
        @classmethod
        def cuddle(anu):
            cuddle = choice([anu.url1 + 'cuddle', anu.url2 + 'cuddle', anu.url3 + 'cuddle/gif'])
            return anu.pict(cuddle)
        @classmethod
        def dance(anu):
            dance = choice([anu.url1 + 'dance', anu.url2 + 'dance', anu.url3 + 'dance/gif'])
            return anu.pict(dance)
        @classmethod
        def eevee(anu):
            eevee = choice([anu.url3 + 'eevee/gif', anu.url3 + 'eevee/img'])
            return anu.pict(eevee)
        @classmethod
        def feed(anu):
            feed = choice([anu.url1 + 'feed', anu.url3 + 'feed/gif'])
            return anu.pict(feed)
        @classmethod
        def fluff(anu):
            return anu.pict(anu.url3 + 'fluff/gif')
        @classmethod
        def holo(anu):
            return anu.pict(anu.url3 + 'holo/img')
        @classmethod
        def hug(anu):
            hug = choice([anu.url1 + 'hug', anu.url2 + 'hug', anu.url3 + 'hug/gif'])
            return anu.pict(hug)
        @classmethod
        def kiss(anu):
            kiss = choice([anu.url1 + 'kiss', anu.url2 + 'kiss', anu.url3 + 'kiss/gif'])
            return anu.pict(kiss)
        @classmethod
        def kitsune(anu):
            return anu.pict(anu.url3 + 'kitsune/img')
        @classmethod
        def lick(anu):
            lick = choice([anu.url1 + 'lick', anu.url2 + 'lick', anu.url3 + 'lick/gif'])
            return anu.pict(lick)
        @classmethod
        def okami(anu):
            return anu.pict(anu.url3 + 'okami/img')
        @classmethod
        def pat(anu):
            pat = choice([anu.url1 + 'pat', anu.url2 + 'pat', anu.url3 + 'pat/gif'])
            return anu.pict(pat)
        @classmethod
        def poke(anu):
            poke = choice([anu.url1 + 'poka', anu.url2 + 'poka', anu.url3 + 'poke/gif'])
            return anu.pict(poke)
        @classmethod
        def megumin(anu):
            return anu.pict(anu.url2 + 'megumin')
        @classmethod
        def shinobu(anu):
            return anu.pict(anu.url2 + 'shinobu')
        @classmethod
        def senko(anu):
            return anu.pict(anu.url3 + 'senko/img')
        @classmethod
        def slap(anu):
            slap = choice([anu.url1 + 'slap', anu.url2 + 'slap', anu.url3 + 'slap/gif'])
            return anu.pict(slap)
        @classmethod
        def smile(anu):
            smile = choice([anu.url1 + 'smile', anu.url2 + 'smile', anu.url3 + 'smile/gif'])
            return anu.pict(smile)
        @classmethod
        def tail(anu):
            return anu.pict(anu.url3 + 'tail/gif')
        @classmethod
        def tickle(anu):
            tickle = choice([anu.url1 + 'tickle', anu.url3 + 'tickle/gif'])
            return anu.pict(tickle)
        @classmethod
        def facepalm(anu):
            return anu.pict(anu.url1 + 'facepalm')
        @classmethod
        def happy(anu):
            happy = choice([anu.url1 + 'happy', anu.url2 + 'happy'])
            return anu.pict(happy)
        @classmethod
        def highfive(anu):
            return anu.pict([anu.url1 + 'highfive'])
        @classmethod
        def wink(anu):
            wink = choice([anu.url1 + 'wink', anu.url2 + 'wink'])
            return anu.pict(wink)
        @classmethod
        def awoo(anu):
            return anu.pict(anu.url2 + 'awoo')
        @classmethod
        def bonk(anu):
            return(anu.url2 + 'bonl')
        @classmethod
        def smug(anu):
            return anu.pict(anu.url2 + 'smug')
        @classmethod
        def handhold(anu):
            return anu.pict(anu.url2 + 'handhold')
        @classmethod
        def kill(anu):
            return anu.pict(anu.url2 + 'kill')
        @classmethod
        def cringe(anu):
            return anu.pict(anu.url2 + 'cringe')
        @classmethod
        def wave(anu):
            wave = choice([anu.url1 + 'wave', anu.url2 + 'wave'])
            return anu.pict(wave)

