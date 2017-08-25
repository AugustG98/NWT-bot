import books

def process(book, Chapter_Verse):

    print('verse called: '+book+' '+Chapter_Verse)
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
