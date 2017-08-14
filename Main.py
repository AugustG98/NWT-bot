import bs4 as bs
import urllib.request


while True:

    try:
        
        book, chapter, verse = input('Book, chapter and verse:\n').split()
        
    except ValueError:

        print('\nWrong format, try again!\n')
        continue

    if (book == 'john' or 'John'):
        book = '43'

    sauce = urllib.request.urlopen('https://wol.jw.org/en/wol/b/r1/lp-e/nwt/E/2013/'+book+'/'+chapter+'#study=discover').read()
    soup = bs.BeautifulSoup(sauce, 'lxml')


    #header
    print ('\n'+soup.title.text+'\n')

    
    #Print specific verse
    for paragraph in soup.find_all('span', id= 'v'+book+'-'+chapter+'-'+verse+'-1' ):
        print('')
        print(paragraph.text)

    input()

    #Print entire chapter
    #for paragraph in soup.find_all('p',class_='sb'):
    #    print(paragraph.text)

    #elif (book == 'john' or 'John'):
     #       book = '43'
