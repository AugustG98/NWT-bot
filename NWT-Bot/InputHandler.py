import books
import time
from datetime import datetime

line = '\n'+'-'*30

def process(book, Chapter_Verse, language, add):
    if (add != '0'):
        book += Chapter_Verse
        Chapter_Verse = add
    else:
        pass
    print(str(datetime.now())+line+'\nverse(s) called in '+language+': '+book+' '+Chapter_Verse)

    chapter, verse = Chapter_Verse.split(':')

    try:
        fromVerse, toVerse = verse.split('-')

    except:
        fromVerse = verse
        toVerse = verse
        pass

    if book in books.bookprefix:
        booknumber = books.bookprefix.get(book)

        return(booknumber, chapter, verse, fromVerse, toVerse)
