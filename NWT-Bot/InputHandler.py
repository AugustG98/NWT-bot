import books
import time
from datetime import datetime

def Process(book, Chapter_Verse, language, add):
    if (add != '0'):
        book += Chapter_Verse
        Chapter_Verse = add
    else:
        pass

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
