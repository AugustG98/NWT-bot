import urllib.request
import bs4 as bs
import re
import languages

def GetData(booknumber, chapter, verse, fromVerse, toVerse, language):

    if language in languages.languageURLs:
        URL = languages.languageURLs.get(language)

    sauce = urllib.request.urlopen(URL+booknumber+'/'+chapter+'#study=discover').read()
    soup = bs.BeautifulSoup(sauce, 'lxml')
    for paragraph in soup.find_all(class_='resultsNavigationSelected documentLocation navChapter'):
        header = paragraph.text.strip()

    result = ''

    for index in range(int(fromVerse), int(toVerse)+1):

        for paragraph in soup.find_all('span', id= 'v'+booknumber+'-'+chapter+'-'+str(index)+'-1' ):
            result += paragraph.text
            versenumber = str(index)

            for index in range(2, 10):
                for paragraph in soup.find_all('span', id= 'v'+booknumber+'-'+chapter+'-'+versenumber+'-'+str(index)):
                    result = result.replace(':', ': ')
                    result += ' '
                    result += paragraph.text

    result = result.replace('+', '')
    result = result.replace('*', '')
    result = result.replace('.0', '. 0')
    result = result.replace('.1', '. 1')
    result = result.replace('.2', '. 2')
    result = result.replace('.3', '. 3')
    result = result.replace('.4', '. 4')
    result = result.replace('.5', '. 5')
    result = result.replace('.6', '. 6')
    result = result.replace('.7', '. 7')
    result = result.replace('.8', '. 8')
    result = result.replace('.9', '. 9')

    return(header, verse, result)

