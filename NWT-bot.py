import discord
from discord.ext import commands
import bs4 as bs
import urllib.request
import re



des = 'A discord biblebot for NWT'

prefix = '!'

client = commands.Bot(description=des, command_prefix=prefix)

@client.event
async def on_ready():
    print('Bot online!')


#ENGLISH
@client.command(pass_context=True)
async def english(ctx, book, chapterANDverse):

    chapter, verse = chapterANDverse.split(':')

    dict = {
    'Genesis' : '1',
    'genesis' : '1',
    'Gen' : '1',
    'gen' : '1',
    'Exodus' : '2',
    'exodus' : '2',
    'Exo' : '2',
    'exo' : '2',
    'Ex' : '2',
    'ex' : '2',
    'Leviticus' : '3',
    'leviticus' : '3',
    'Lev' : '3',
    'lev' : '3',
    'Numbers' : '4',
    'numbers' : '4',
    'Numb' : '4',
    'numb' : '4',
    'Deuteronomy' : '5',
    'Deut' : '5',
    'Joshua' : '6',
    'Josh' : '6',
    'Judges' : '7' ,
    'Judg' : '7',
    'Ruth' : '8',
    '1 Samuel' : '9',
    '1 Sam' : '9',
    '2 Samuel' : '10',
    '2 Sam' : '10',
    '1 Kings' : '11',
    '1 Ki' : '11',
    '2 Kings' : '12',
    '2 Ki' : '12',
    '1 Chronicles' : '13',
    '1 Chron' : '13',
    '2 Chronicles' : '14',
    '2 Chron' : '14',
    'Ezra' : '15',
    'Nehemiah' : '16',
    'Neh' : '16',
    'Esther' : '17',
    'Job' : '18',
    'Psalms' : '19',
    'Ps' : '19',
    'Proverbs' : '20',
    'Prov' : '20',
    'Ecclesiastes' : '21',
    'Eccl' : '21',
    'Song of Solomon' : '22',
    'Song of Sol' : '22',
    'Isaiah' : '23',
    'Isa' : '23',
    'Jeremiah' : '24',
    'Jer' : '24',
    'Lamentations' : '25',
    'Lam' : '25',
    'Ezekiel' : '26',
    'Ez' : '26',
    'Daniel' : '27',
    'Dan' : '27',
    'Hosea' : '28',
    'Hos' : '28',
    'Joel' : '29',
    'Amos' : '30',
    'Obadiah' : '31',
    'Obad' : '31',
    'Jonah' : '32',
    'Micah' : '33',
    'Mic' : '33',
    'Nahum' : '34' ,
    'Nah' : '34',
    'Habakkuk' : '35',
    'Hab' : '35',
    'Zephaniah' : '36',
    'Zeph' : '36',
    'Haggai' : '37',
    'Hag' : '37',
    'Zechariah' : '38',
    'Zech' : '38',
    'Malachi' : '39',
    'Mal' : '39',
    'Matthew' : '40',
    'Matt' : '40',
    'Mark' : '41',
    'Luke' : '42',
    'John' : '43',
    'Acts' : '44',
    'Romans' : '45',
    'Rom' : '45',
    '1 Corinthians' : '46',
    '1 Cor' : '46',
    '2 Corinthians'  : '47',
    '2 Cor' : '47',
    'Galatians' : '48',
    'Gal' : '48',
    'Ephesians' : '49',
    'Eph' : '49',
    'Philippians' : '50',
    'Phil' : '50',
    'Colossians' : '51',
    'Col' : '51',
    '1 Thessalonians' : '52',
    '1 Thess' : '52',
    '2 Thessalonians' : '53',
    '2 Thess' : '53',
    '1 Timothy' : '54',
    '1 Tim' : '54',
    '2 Timothy' : '55',
    '2 Tim' : '55',
    'Titus' : '56',
    'Philemon' : '57',
    'Philem' : '57',
    'Hebrews' : '58',
    'Heb' : '58',
    'James' : '59',
    'Jas' : '59',
    '1 Peter' : '60',
    '1 Pet' : '60',
    '2 Peter' : '61',
    '2 Pet' : '61',
    '1 John' : '62',
    '2 John' : '63',
    '3 John' : '64',
    'Jude' : '65',
    'Revelation' : '66',
    'Rev' : '66',
    }

    if book in dict:
        booknumber = dict.get(book)

    sauce = urllib.request.urlopen('https://wol.jw.org/en/wol/b/r1/lp-e/nwt/E/2013/'+booknumber+'/'+chapter+'#study=discover').read()
    soup = bs.BeautifulSoup(sauce, 'lxml')
    for paragraph in soup.find_all('span', id= 'v'+booknumber+'-'+chapter+'-'+verse+'-1' ):
        result = paragraph.text
    for paragraph in soup.find_all(class_='resultsNavigationSelected documentLocation navChapter'):
        header = paragraph.text.strip()

    await client.say('**'+header+':'+verse+' - New World Translation (NWT)**\n\n```css\n'+result+'```')

#SPANISH
@client.command(pass_context=True)
async def spanish(ctx, book, chapterANDverse):

    chapter, verse = chapterANDverse.split(':')

    dict = {
    'Genesis' : '1',
    'genesis' : '1',
    'Gen' : '1',
    'gen' : '1',
    'Exodus' : '2',
    'exodus' : '2',
    'Exo' : '2',
    'exo' : '2',
    'Ex' : '2',
    'ex' : '2',
    'Leviticus' : '3',
    'leviticus' : '3',
    'Lev' : '3',
    'lev' : '3',
    'Numbers' : '4',
    'numbers' : '4',
    'Numb' : '4',
    'numb' : '4',
    'Deuteronomy' : '5',
    'Deut' : '5',
    'Joshua' : '6',
    'Josh' : '6',
    'Judges' : '7' ,
    'Judg' : '7',
    'Ruth' : '8',
    '1 Samuel' : '9',
    '1 Sam' : '9',
    '2 Samuel' : '10',
    '2 Sam' : '10',
    '1 Kings' : '11',
    '1 Ki' : '11',
    '2 Kings' : '12',
    '2 Ki' : '12',
    '1 Chronicles' : '13',
    '1 Chron' : '13',
    '2 Chronicles' : '14',
    '2 Chron' : '14',
    'Ezra' : '15',
    'Nehemiah' : '16',
    'Neh' : '16',
    'Esther' : '17',
    'Job' : '18',
    'Psalms' : '19',
    'Ps' : '19',
    'Proverbs' : '20',
    'Prov' : '20',
    'Ecclesiastes' : '21',
    'Eccl' : '21',
    'Song of Solomon' : '22',
    'Song of Sol' : '22',
    'Isaiah' : '23',
    'Isa' : '23',
    'Jeremiah' : '24',
    'Jer' : '24',
    'Lamentations' : '25',
    'Lam' : '25',
    'Ezekiel' : '26',
    'Ez' : '26',
    'Daniel' : '27',
    'Dan' : '27',
    'Hosea' : '28',
    'Hos' : '28',
    'Joel' : '29',
    'Amos' : '30',
    'Obadiah' : '31',
    'Obad' : '31',
    'Jonah' : '32',
    'Micah' : '33',
    'Mic' : '33',
    'Nahum' : '34' ,
    'Nah' : '34',
    'Habakkuk' : '35',
    'Hab' : '35',
    'Zephaniah' : '36',
    'Zeph' : '36',
    'Haggai' : '37',
    'Hag' : '37',
    'Zechariah' : '38',
    'Zech' : '38',
    'Malachi' : '39',
    'Mal' : '39',
    'Matthew' : '40',
    'Matt' : '40',
    'Mark' : '41',
    'Luke' : '42',
    'John' : '43',
    'Acts' : '44',
    'Romans' : '45',
    'Rom' : '45',
    '1 Corinthians' : '46',
    '1 Cor' : '46',
    '2 Corinthians'  : '47',
    '2 Cor' : '47',
    'Galatians' : '48',
    'Gal' : '48',
    'Ephesians' : '49',
    'Eph' : '49',
    'Philippians' : '50',
    'Phil' : '50',
    'Colossians' : '51',
    'Col' : '51',
    '1 Thessalonians' : '52',
    '1 Thess' : '52',
    '2 Thessalonians' : '53',
    '2 Thess' : '53',
    '1 Timothy' : '54',
    '1 Tim' : '54',
    '2 Timothy' : '55',
    '2 Tim' : '55',
    'Titus' : '56',
    'Philemon' : '57',
    'Philem' : '57',
    'Hebrews' : '58',
    'Heb' : '58',
    'James' : '59',
    'Jas' : '59',
    '1 Peter' : '60',
    '1 Pet' : '60',
    '2 Peter' : '61',
    '2 Pet' : '61',
    '1 John' : '62',
    '2 John' : '63',
    '3 John' : '64',
    'Jude' : '65',
    'Revelation' : '66',
    'Rev' : '66',
    'rev' : '66',
    }

    if book in dict:
        booknumber = dict.get(book)

    sauce = urllib.request.urlopen('https://wol.jw.org/es/wol/b/r4/lp-s/Rbi8/S/1987/'+booknumber+'/'+chapter+'#study=discover').read()
    soup = bs.BeautifulSoup(sauce, 'lxml')
    for paragraph in soup.find_all('span', id= 'v'+booknumber+'-'+chapter+'-'+verse+'-1' ):
        result = paragraph.text
    for paragraph in soup.find_all(class_='resultsNavigationSelected documentLocation navChapter'):
        header = paragraph.text.strip()


    await client.say('**'+header+':'+verse+' - New World Translation (NWT)**\n\n''```css\n'+result+'```')


client.run('MzQ2Nzg0MTI5OTIyMjM2NDI3.DHUMFA.snA-jb3pfPi4xGmKA46msJrE7C4')
