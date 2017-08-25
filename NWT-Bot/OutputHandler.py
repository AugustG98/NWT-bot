import urllib.request
import bs4 as bs
import re
import languages

def getVerses(booknumber, chapter, verse, fromVerse, toVerse, language):

    result = ''

    if language in languages.languageURL:
        URL = languages.languageURL.get(language)

    sauce = urllib.request.urlopen(URL+booknumber+'/'+chapter+'#study=discover').read()
    soup = bs.BeautifulSoup(sauce, 'lxml')
    for paragraph in soup.find_all(class_='resultsNavigationSelected documentLocation navChapter'):
        header = paragraph.text.strip()

    for index in range(int(fromVerse), int(toVerse)+1):

        for paragraph in soup.find_all('span', id= 'v'+booknumber+'-'+chapter+'-'+str(index)+'-1' ):
            result += paragraph.text


    result = result.replace('+', '')
    result = result.replace('*', '')

    return(header, verse, result)
