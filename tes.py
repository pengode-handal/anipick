import anipick

title = input('input anime name: ')
animm = anipick.Lyricspedia(title)
a = f'''{animm.lyrics_romaji}
'''
print(a)
