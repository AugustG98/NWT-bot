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

@client.event
async def on_message(message):
    if message.content.startswith('!announce'):
        botowner = 'Benroy#7151'
        print(message.author)
        if (str(message.author) == botowner):
            await client.send_message(message.channel, message.author)
            for server in client.servers:
                for channel in server.channels:
                    await client.send_message(channel, 'this is a test, ignore')
        else:
            await client.send_message(message.channel, 'Only Benroy#7151 can do this')

@client.command(pass_context=True)
async def servers(ctx):

    list = ''
    for server in client.servers:
        list += str(server)+',\n'
    await client.say('List of servers NWT-Bot is connected to: ```'+list+'```')

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

def getdata(book, chapterANDverse, language, add):

    booknumber, chapter, verse, fromVerse, toVerse = InputHandler.process(book, chapterANDverse, language, add)
    header, verse, data = OutputHandler.getVerses(booknumber, chapter, verse, fromVerse, toVerse, language)
    return(header, verse, data)

client.run('MzQ2Nzg0MTI5OTIyMjM2NDI3.DKcsUA.9hMx0MsYIqbolZJuUVyIabsi87s')
