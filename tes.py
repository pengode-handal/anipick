import anipick
from googlesearch import search
title = input()
animm = anipick.Mangaography(title)
print(f'''
{animm.manga_id}\n\n
{animm.type}\n
{animm.status}\n
{animm.aired}\n
{animm.name}\n
{animm.name_en}\n
{animm.name_jp}\n
{animm.manga_url}\n
{animm.image_url}\n
{animm.score}\n
{animm.ranking}\n
{animm.volume}\n
{animm.chapter}\n
{animm.member}\n
{animm.genres}\n
{animm.author}\n
{animm.related}\n
{animm.serialization}\n
{animm.popularity}\n
{animm.synopsis}\n
{animm.weapon}''')