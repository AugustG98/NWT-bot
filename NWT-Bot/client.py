import discord
from discord.ext import commands
import InputHandler
import OutputHandler
import re


des = 'A discord bot for getting Bible verses from the New World Translation'
prefix = '!'
client = commands.Bot(description=des, command_prefix=prefix)

@client.event
async def on_ready():
    print('Bot online!')

#ENGLISH
@client.command(pass_context=True)
async def english(ctx, book, chapterANDverse):
    language = 'english'
    header, verse, result = inputANDoutput(book, chapterANDverse, language)

    await client.say('**'+header+':'+verse+' - New World Translation (NWT)**\n\n```css\n'+result+'```')

#HEBREW
@client.command(pass_context=True)
async def hebrew(ctx, book, chapterANDverse):
    language = 'hebrew'
    header, verse, result = inputANDoutput(book, chapterANDverse, language)

    await client.say('**'+header+':'+verse+' - New World Translation (NWT)**\n\n```css\n'+result+'```')

#GREEK
@client.command(pass_context=True)
async def greek(ctx, book, chapterANDverse):
    language = 'greek'
    header, verse, result = inputANDoutput(book, chapterANDverse, language)

    await client.say('**'+header+':'+verse+' - New World Translation (NWT)**\n\n```css\n'+result+'```')

#FRENCH
@client.command(pass_context=True)
async def french(ctx, book, chapterANDverse):
    language = 'french'
    header, verse, result = inputANDoutput(book, chapterANDverse, language)

    await client.say('**'+header+':'+verse+' - New World Translation (NWT)**\n\n```css\n'+result+'```')

#SPANISH
@client.command(pass_context=True)
async def spanish(ctx, book, chapterANDverse):
    language = 'spanish'
    header, verse, result = inputANDoutput(book, chapterANDverse, language)

    await client.say('**'+header+':'+verse+' - New World Translation (NWT)**\n\n```css\n'+result+'```')

#GERMAN
@client.command(pass_context=True)
async def german(ctx, book, chapterANDverse):
    language = 'german'
    header, verse, result = inputANDoutput(book, chapterANDverse, language)

    await client.say('**'+header+':'+verse+' - New World Translation (NWT)**\n\n```css\n'+result+'```')

def inputANDoutput (book, chapterANDverse, language):

    booknumber, chapter, verse, fromVerse, toVerse = InputHandler.process(book, chapterANDverse)
    header, verse, result = OutputHandler.getVerses(booknumber, chapter, verse, fromVerse, toVerse, language)
    return(header, verse, result)

client.run('MzQ2Nzg0MTI5OTIyMjM2NDI3.DHfORQ.U-ELYc67t1Sa0Mb1XMESc_bM9mA')
