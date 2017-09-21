import discord
from discord.ext import commands
import re
import InputHandler
import OutputHandler
import languages
import books

des = 'A discord bot for getting Bible verses from the New World Translation'
prefix = '!'
client = commands.Bot(description=des, command_prefix=prefix)
online = '\n\nBot is online!\n\n'
error = 'too many characters, 2000 characters max!'
TooLong = '**The passage is too long for me to grab, sorry!**'
Format = '**Wrong format used, try again:**\n```!language bookname chapter:verse(s)```'

@client.event
async def on_ready():
    print(online)

#PRINT AVAILABLE LANGUAGES IN CHAT
@client.command(pass_context=True)
async def language():
    available = ''
    for language in languages.languageURLs:
        available += '\n!'+language

    await client.say('**Languages available:**```'+available+'```')

#ENGLISH
@client.command(pass_context=True)
async def english(ctx, book, chapterANDverse, add='0'):
    language = 'english'
    try:
        header, verse, data = getdata(book, chapterANDverse, language, add)
        try:
            await client.say('**'+header+':'+verse+' - New World Translation (NWT)**\n\n```css\n'+data+'```')

        except Exception:
            await client.say(TooLong)

    except Exception:
        await client.say(Format)
        pass

#HEBREW
@client.command(pass_context=True)
async def hebrew(ctx, book, chapterANDverse, add='0'):
    language = 'hebrew'
    try:
        header, verse, data = getdata(book, chapterANDverse, language, add)
        try:
            await client.say('**'+header+':'+verse+' - New World Translation (NWT)**\n\n```css\n'+data+'```')

        except Exception:
            await client.say(TooLong)

    except Exception:
        await client.say(Format)
        pass

#GREEK
@client.command(pass_context=True)
async def greek(ctx, book, chapterANDverse, add='0'):
    language = 'greek'
    try:
        header, verse, data = getdata(book, chapterANDverse, language, add)
        try:
            await client.say('**'+header+':'+verse+' - New World Translation (NWT)**\n\n```css\n'+data+'```')

        except Exception:
            await client.say(TooLong)

    except Exception:
        await client.say(Format)
        pass

#FRENCH
@client.command(pass_context=True)
async def french(ctx, book, chapterANDverse, add='0'):
    language = 'french'
    try:
        header, verse, data = getdata(book, chapterANDverse, language, add)
        try:
            await client.say('**'+header+':'+verse+' - New World Translation (NWT)**\n\n```css\n'+data+'```')

        except Exception:
            await client.say(TooLong)

    except Exception:
        await client.say(Format)
        pass

#SPANISH
@client.command(pass_context=True)
async def spanish(ctx, book, chapterANDverse, add='0'):
    language = 'spanish'
    try:
        header, verse, data = getdata(book, chapterANDverse, language, add)
        try:
            await client.say('**'+header+':'+verse+' - New World Translation (NWT)**\n\n```css\n'+data+'```')

        except Exception:
            await client.say(TooLong)

    except Exception:
        await client.say(Format)
        pass

#GERMAN
@client.command(pass_context=True)
async def german(ctx, book, chapterANDverse, add='0'):
    t0 = time.time()
    language = 'german'
    try:
        header, verse, data = getdata(book, chapterANDverse, language, add)
        try:
            await client.say('**'+header+':'+verse+' - New World Translation (NWT)**\n\n```css\n'+data+'```')

        except Exception:
            await client.say(TooLong)
            print(error+line)

    except Exception:
        await client.say(Format)
        print('Wrong format used.'+line)
        pass

def getdata(book, chapterANDverse, language, add):

    booknumber, chapter, verse, fromVerse, toVerse = InputHandler.process(book, chapterANDverse, language, add)
    header, verse, data = OutputHandler.getVerses(booknumber, chapter, verse, fromVerse, toVerse, language)
    return(header, verse, data)

client.run('')
