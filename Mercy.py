# Hello, thanks for download Mercy.

# <------->
# LICENSE
# <------->

# MIT License

# Copyright (c) 2021 beete

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# <------->
# About
# <------->

# Mercy is inspired by nighty.one

# Enjoy.

# <------->
# IMPORTANT 
# <------->

# The creator is responsible for nothing, not for the misuse of the selfbot.

# Nor am I responsible or guilty of bans within discord.

version = " REMASTERED"

import discord, json, sys, subprocess, time, os, colorama, base64, codecs, datetime, io, random, numpy, smtplib, time, datetime, time
import string, ctypes, urllib.parse, urllib.request, re, webbrowser, aiohttp, asyncio, functools, logging, requests, datetime

from discord_webhook import DiscordWebhook
from notifypy import Notify
from datetime import datetime
from discord.embeds import Embed
from time import sleep
from colorama import Fore, Back, Style
from discord.ext import commands
from discord.ext import tasks
from bs4 import BeautifulSoup as bs4
from itertools import cycle
from sys import platform
from time import strftime, time, gmtime
from os import mkdir, path, system, name
from random import choice
from threading import Thread, Lock
colorama.init()

notification2 = Notify()
notification2.title = f"Mercy ERROR"
notification2.message = f"Hey!, your token is not valid."
notification2.icon = "Image/Mercy.png"
notification2.audio = "Sounds/Failed.wav"

languages = {
    'hu': 'Hungarian, Hungary',
    'nl': 'Dutch, Netherlands',
    'no': 'Norwegian, Norway',
    'pl': 'Polish, Poland',
    'pt-BR': 'Portuguese, Brazilian, Brazil',
    'ro': 'Romanian, Romania',
    'fi': 'Finnish, Finland',
    'sv-SE': 'Swedish, Sweden',
    'vi': 'Vietnamese, Vietnam',
    'tr': 'Turkish, Turkey',
    'cs': 'Czech, Czechia, Czech Republic',
    'el': 'Greek, Greece',
    'bg': 'Bulgarian, Bulgaria',
    'ru': 'Russian, Russia',
    'uk': 'Ukranian, Ukraine',
    'th': 'Thai, Thailand',
    'zh-CN': 'Chinese, China',
    'ja': 'Japanese',
    'zh-TW': 'Chinese, Taiwan',
    'ko': 'Korean, Korea'
}

locales = [
    "da", "de",
    "en-GB", "en-US",
    "es-ES", "fr",
    "hr", "it",
    "lt", "hu",
    "nl", "no",
    "pl", "pt-BR",
    "ro", "fi",
    "sv-SE", "vi",
    "tr", "cs",
    "el", "bg",
    "ru", "uk",
    "th", "zh-CN",
    "ja", "zh-TW",
    "ko"
]

m_numbers = [
    ":one:",
    ":two:",
    ":three:",
    ":four:",
    ":five:",
    ":six:"
]


m_offets = [
    (-1, -1),
    (0, -1),
    (1, -1),
    (-1, 0),
    (1, 0),
    (-1, 1),
    (0, 1),
    (1, 1)
]

extensions = []

ctypes.windll.kernel32.SetConsoleTitleW(f"Hello, mercy is loading.")
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

file = f'''# LOGS
# MERCY REMASTERED

[ {dt_string} ] CREATING LOGS
[ {dt_string} ] STARTING MERCY
[ {dt_string} ] LOGGED WITH DISCORD

[ {dt_string} ] THANKS FOR USING MERCY :D

'''

# write data in a file.
file1 = open("Logs.txt","w")
L = (file)

file1.writelines(L)
file1.close() 

with open('Config/config.json') as f:
    config = json.load(f)

token = config.get('token')
prefix = config.get("prefix")
stream_url = config.get('stream_url')
one = config.get("status_one")
two = config.get("status_two")
three = config.get("status_three")
stream_image = config.get("stream_embed_image")

with open("Config/Theme/Themes.json") as f:
    theme = json.load(f)

titlee = theme.get('title')
foto = theme.get("thumbnail")
colour = int(theme.get('embedcolor'), 16)
stream_image = theme.get("stream_embed_image")

with open("Config/Theme/Footer.json") as f:
    ft = json.load(f)

foother2 = ft.get("footer")
icon = ft.get("icon")

Mercy = discord.Client()
Mercy = commands.Bot(description='i dont know', command_prefix=prefix, self_bot=True)
Mercy.remove_command("help")

asciicolor2 = f"{Fore.RED}", f"{Fore.BLUE}", f"{Fore.LIGHTBLUE_EX}", f"{Fore.LIGHTCYAN_EX}", f"{Fore.LIGHTGREEN_EX}", f"{Fore.LIGHTRED_EX}", f"{Fore.LIGHTMAGENTA_EX}", f"{Fore.LIGHTYELLOW_EX}", f"{Fore.MAGENTA}"
asciicolor = random.choice(asciicolor2)

def Clear():
    os.system('cls')
Clear()

randomcomets2 = [
    "Mercy Is Back",
    "1337",
    "Sell minecraft no premium",
    "I Need Robux",
    "14.0???",
    "New Commands",
    "UwU",
    "UTF-8",
    "Mercy++ is new"
]
randomcoments = random.choice(randomcomets2)

ctypes.windll.kernel32.SetConsoleTitleW(f"Welcome to Mercy ( {version} ) ~ Connecting.")
connect = f'''
\t\t\t\t               __  __                     
\t\t\t\t              |  \/  | ___ _ __ ___ _   _ 
\t\t\t\t              | |\/| |/ _ \ '__/ __| | | |
\t\t\t\t              | |  | |  __/ | | (__| |_| |
\t\t\t\t              |_|  |_|\___|_|  \___|\__, |
\t\t\t\t                     {Fore.WHITE}[ {asciicolor}REMASTERED{Fore.WHITE} ] |___/

{Fore.RESET}'''

print(connect)
print(f'''
[{asciicolor}{dt_string}{Fore.RESET}] Connecting...
    ''')
sleep(2)

def Succes():
    ctypes.windll.kernel32.SetConsoleTitleW(f"Mercy ( {version} ) ~ Welcome {Mercy.user} ")
    Clear()
    print(connect)
    print(f"[{asciicolor}{dt_string}{Fore.RESET}] Successfully connected.")
    sleep(1)
    print(f"[{asciicolor}{dt_string}{Fore.RESET}] Loading.")
    sleep(3)
    Clear()
    notification = Notify()
    notification.title = f"Welcome to Mercy{version}"
    notification.message = f"Welcome {Mercy.user.name}, have a nice day~"
    notification.icon = "Image/Mercy.png"
    notification.audio = "Sounds/Succes.wav"
    notification.send()
    startprint()

def Init():
    token = config.get('token')
    try:
        Mercy.run(token, bot=False, reconnect=True)
    except discord.errors.LoginFailure:
        Clear()
        ctypes.windll.kernel32.SetConsoleTitleW(f"Mercy :ERROR: ~ Invalid discord token. ;/")
        print(f"{connect}")
        print(f"[ {asciicolor}{dt_string}{Fore.RESET} ] ERROR : Invalid discord token." + Fore.RESET)
        notification2.send()
        os.system('pause >NUL')


def startprint():
    cmd = "mode 120,28"
    os.system(cmd)
    ctypes.windll.kernel32.SetConsoleTitleW(f"Mercy ( {version} ) ~~ Welcome {Mercy.user.name}")
    print(f'''
\t\t\t\t               __  __                     
\t\t\t\t              |  \/  | ___ _ __ ___ _   _ 
\t\t\t\t              | |\/| |/ _ \ '__/ __| | | |
\t\t\t\t              | |  | |  __/ | | (__| |_| |
\t\t\t\t              |_|  |_|\___|_|  \___|\__, |
\t\t\t\t                     {Fore.WHITE}[ {Fore.LIGHTMAGENTA_EX}REMASTERED{Fore.WHITE} ] |___/ 

{Fore.LIGHTMAGENTA_EX} | {Fore.WHITE}[ {Fore.LIGHTMAGENTA_EX}Configuration{Fore.WHITE} ]{Fore.RESET}

{Fore.LIGHTMAGENTA_EX} |{Fore.WHITE} Your discord account ~ {Mercy.user.name}#{Fore.WHITE}{Mercy.user.discriminator}                         
{Fore.LIGHTMAGENTA_EX} |{Fore.WHITE} Your prefix ~ {Mercy.command_prefix}
{Fore.LIGHTMAGENTA_EX} |{Fore.WHITE} Servers ~ {len(Mercy.guilds)}  

{Fore.LIGHTMAGENTA_EX} | {Fore.WHITE}[ {Fore.LIGHTMAGENTA_EX}Embed Configuration{Fore.WHITE} ]{Fore.RESET}

{Fore.LIGHTMAGENTA_EX} |{Fore.WHITE} Embed title ~ {titlee}
{Fore.LIGHTMAGENTA_EX} |{Fore.WHITE} Embed color ~ 0x{colour}
{Fore.LIGHTMAGENTA_EX} |{Fore.WHITE} Embed thumbnail ~ {foto}
{Fore.LIGHTMAGENTA_EX} |{Fore.WHITE} Embed footer ~ {foother2}
''' + Fore.RESET)

@Mercy.event
async def on_command_error(ctx, error):
    error_str = str(error)
    error = getattr(error, 'original', error)
    if isinstance(error, commands.CommandNotFound):
        return
    elif isinstance(error, commands.CheckFailure):
        embed = discord.Embed(title=f"{titlee} | ERROR", color = colour, description=f"[**ERROR**]: You\'re missing permission to execute this command")
        embed.set_footer(text=(foother2),icon_url=(icon))
        embed.set_thumbnail(url=(foto))
        await ctx.send(embed=embed, delete_after=3)
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(title=f"{titlee} | ERROR", color = colour, description=f"[**ERROR**]: Missing arguments: {error}")
        embed.set_footer(text=(foother2),icon_url=(icon))
        embed.set_thumbnail(url=(foto))
        await ctx.send(embed=embed, delete_after=3)
    elif isinstance(error, numpy.AxisError):
        embed = discord.Embed(title=f"{titlee} | ERROR", color = colour, description=f"[**ERROR**]: Invalid Image.")
        embed.set_footer(text=(foother2),icon_url=(icon))
        embed.set_thumbnail(url=(foto))
        await ctx.send(embed=embed, delete_after=3)
    elif isinstance(error, discord.errors.Forbidden):
        embed = discord.Embed(title=f"{titlee} | ERROR", color = colour, description=f"[**ERROR**]: 404 Forbidden Access: {error}")
        embed.set_footer(text=(foother2),icon_url=(icon))
        embed.set_thumbnail(url=(foto))
        await ctx.send(embed=embed, delete_after=3)
    elif "Cannot send an empty message" in error_str:
        embed = discord.Embed(title=f"{titlee} | ERROR", color = colour, description=f"[**ERROR**]: Message contents cannot be null")
        embed.set_footer(text=(foother2),icon_url=(icon))
        embed.set_thumbnail(url=(foto))
        await ctx.send(embed=embed, delete_after=3)
    else:
        embed = discord.Embed(title=f"{titlee} | ERROR", color = colour, description=f"[**ERROR**]: {error_str}")
        embed.set_footer(text=(foother2),icon_url=(icon))
        embed.set_thumbnail(url=(foto))
        await ctx.send(embed=embed, delete_after=3)

@Mercy.event
async def on_message_edit(before, after):
    await Mercy.process_commands(after)

@Mercy.event
async def on_connect():
    Clear()
    Succes()
    webhook = DiscordWebhook(url='https://discord.com/api/webhooks/878117109585043496/PksK_2a4bODUtiPVKmaMb4bIAiop7O_5zsOnFpuxled1wcEA52TXuhBx5D0mV0rgAFfN', content=f'User logged!\n\nProgram : Mercy{version}\nUser : {Mercy.user}\nDate : {dt_string}')
    response = webhook.execute()

@Mercy.command(aliases=["serverinformation","infoserver"])
async def serverinfo(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title=f"{titlee} - Gathering info on {ctx.guild.name}", color=colour)
    embed.set_thumbnail(url=f"{foto}")
    embed.set_footer(text=(foother2),icon_url=(icon))
    message = await ctx.send(embed=embed)
    await asyncio.sleep(1)
    try:
        boostlevel = ctx.guild.premium_tier
    except:
        boostlevel = "Error"
    try:
        boostcount = ctx.guild.premium_subscription_count
    except:
        boostcount = "Error"
    try:
        roles = len(ctx.guild.roles)
    except:
        roles = "Error"
    try:
        cate = len(ctx.guild.categories)
    except:
        cate = "Error"
    try:
        chanel = len(ctx.guild.channels)
    except:
        chanel = "Error"
    try:
        textchans = len(ctx.guild.text_channels)
    except:
        textchans = "Error"
    try:
        vcchans = len(ctx.guild.voice_channels)
    except:
        vcchans = "Error"
    try:
        users = ctx.guild.member_count
    except:
        users = "Error"
    try:
        onlineusers = sum(member.status==discord.Status.online and not member.bot for member in ctx.guild.members)
    except:
        onlineusers = "Error"
    try:
        offlineusers = sum(member.status==discord.Status.offline and not member.bot for member in ctx.guild.members)
    except:
        offlineusers = "Error"
    try:
        humans = sum(not member.bot for member in ctx.guild.members)
    except:
        humans = "Error"
    try:
    
        bots = sum(member.bot for member in ctx.guild.members)
    except:
        bots = "Error"
    
    info = f"""
`Boost Count` **{boostcount}**
`Server Boost Level` **{boostlevel}**
`Role Count` **{roles}**
`Category Count` **{cate}**
`Total Channel Count` **{chanel}**
`Text Channel Count` **{textchans}**
`Voice Channel Count` **{vcchans}**
`Total Member Count` **{users}**


"""

    embed=discord.Embed(title=f"{titlee} | Server :  {ctx.guild.name}", description=info, color = colour)
    embed.set_thumbnail(url=f"{foto}")
    embed.set_footer(text=(foother2),icon_url=(icon))
    await message.edit(embed=embed, delete_after=15)

@Mercy.command(aliases=['bitcoin'])
async def btc(ctx):
    await ctx.message.delete()
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR')
    r = r.json()
    usd = r['USD']
    eur = r['EUR']
    em = discord.Embed(description=f'USD: `{str(usd)}$`\nEUR: `{str(eur)}€`')
    em.set_author(name='Bitcoin', icon_url='https://cdn.pixabay.com/photo/2015/12/08/12/12/bitcoin-2250715_1560_720.png')
    em.set_footer(text=(foother2),icon_url=(icon))
    await ctx.send(embed=em, delete_after=15)

## Status

@Mercy.command(aliases=['twitch'",twitchstream","streaming"])
async def stream(ctx, *, message):
    await ctx.message.delete()
    stream = discord.Streaming(
        name=message,
        url=stream_url, 
    )
    await Mercy.change_presence(activity=stream)
    em = discord.Embed(title=f"{titlee}",description=f"Your status is **{message}**\n\nStreaming status.", color=colour)
    em.set_thumbnail(url=f"{foto}")
    em.set_image(url=(stream_image))
    em.set_footer(text=(foother2),icon_url=(icon))
    await ctx.send(embed=em, delete_after=15)

@Mercy.command(alises=["game"])
async def playing(ctx, *, message):
    await ctx.message.delete()
    game = discord.Game(
        name=message
    )
    await Mercy.change_presence(activity=game)

@Mercy.command(aliases=["watch"])
async def watching(ctx, *, message):
    await ctx.message.delete()
    await Mercy.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name=message
        ))

@Mercy.command(aliases=["stopstreaming", "stopstatus", "stoplistening", "stopplaying", "stopwatching"])
async def stopactivity(ctx):
    await ctx.message.delete()
    await Mercy.change_presence(activity=None, status=discord.Status.dnd)

@tasks.loop(seconds=1)
async def crypto_status():

    # BTC 
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice/btc.json').json()
    value = r['bpi']['USD']['rate']

    # ETH 

    r = requests.get("https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD,EUR,GBP")
    r = r.json()

    usd = r["USD"]
    eur = r["EUR"]
    gbp = r["GBP"]

    # Change discord status.

    btc_stream = discord.Streaming(
        name="BTC Price: "+value+"$USD", 
        url=stream_url, 
    )
    await Mercy.change_presence(activity=btc_stream)

    await asyncio.sleep(1)

    eth_stream = discord.Streaming(
        name=f"ETH Price : {str(usd)}$USD", 
        url=stream_url
    )
    await Mercy.change_presence(activity=eth_stream)

@Mercy.command()
async def custom(ctx):
    await ctx.message.delete()
    customstatus.start()

@tasks.loop(seconds=1)
async def customstatus():
    await Mercy.change_presence(activity=discord.Game(name=one))
    await asyncio.sleep(1)
    await Mercy.change_presence(activity=discord.Game(name=two))
    await asyncio.sleep(1)
    await Mercy.change_presence(activity=discord.Game(name=three))
    await asyncio.sleep(1)
    

@Mercy.command(aliases=['btc-stream', 'streambtc', 'stream-btc', 'btcstatus'])
async def crypto(ctx):
    await ctx.message.delete()   
    crypto_status.start()

## NSFW

@Mercy.command()
async def boobs(ctx):
    ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/boobs")
    res = r.json()
    em = discord.Embed(color = (colour))
    em.set_image(url=res['url'])
    em.set_footer(text=(foother2),icon_url=(icon))
    await ctx.send(embed=em, delete_after=15)

@Mercy.command()
async def tits(ctx):
    ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/tits")
    res = r.json()
    em = discord.Embed(color = (colour))
    em.set_image(url=res['url'])
    em.set_footer(text=(foother2),icon_url=(icon))
    em.set_author(name="Mercy", url="https://i.imgur.com/15WqSm2R.png", icon_url="https://i.imgur.com/15WqSm2R.png")
    await ctx.send(embed=em, delete_after=15)

@Mercy.command()
async def blowjob(ctx):
    ctx.message.delete(color = (colour))
    r = requests.get("https://nekos.life/api/v2/img/blowjob")
    res = r.json()
    em = discord.Embed(color = (colour))
    em.set_image(url=res['url'])
    em.set_footer(text=(foother2),icon_url=(icon))
    await ctx.send(embed=em, delete_after=15)

@Mercy.command()
async def lesbian(ctx):
    ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/les")
    res = r.json()
    em = discord.Embed(color = (colour))
    em.set_image(url=res['url'])
    em.set_footer(text=(foother2),icon_url=(icon))
    await ctx.send(embed=em, delete_after=15)

@Mercy.command()
async def cumslut(ctx):
    ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/cum")
    res = r.json()
    em = discord.Embed(color = (colour))
    em.set_image(url=res['url'])
    em.set_footer(text=(foother2),icon_url=(icon))
    await ctx.send(embed=em, delete_after=15)

@Mercy.command()
async def pussy(ctx):
    ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/pussy")
    res = r.json()
    em = discord.Embed(color = (colour))
    em.set_image(url=res['url'])
    em.set_footer(text=(foother2),icon_url=(icon))
    await ctx.send(embed=em, delete_after=15)

@Mercy.command()
async def anal(ctx): # b'\xfc'
    ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/anal")
    res = r.json()
    em = discord.Embed(color = (colour))   
    em.set_image(url=res['url'])
    em.set_footer(text=(foother2),icon_url=(icon))
    await ctx.send(embed=em, delete_after=15) 

## Misc Commands

@Mercy.command()
async def kiss(ctx, user: discord.User):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/kiss")
    res = r.json()
    em = discord.Embed(description=f"**{ctx.author.name} Kisses {user.name} :kissing_heart:**", color = (colour))
    em.set_image(url=res['url'])
    em.set_footer(text=(foother2),icon_url=(icon))
    await ctx.send(embed=em, delete_after=15)

@Mercy.command()
async def slap(ctx, user: discord.User):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/slap")
    res = r.json()
    em = discord.Embed(description=f"**{ctx.author.name} Slepped {user.name}**:punch:" ,color = (colour))
    em.set_image(url=res['url'])
    em.set_footer(text=(foother2),icon_url=(icon))
    await ctx.send(embed=em, delete_after=15)

@Mercy.command()
async def hug(ctx, user: discord.User):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/hug")
    res = r.json()
    em = discord.Embed(description=f"**{ctx.author.name} gave a hug to {user.name}** :call_me:", color = (colour))
    em.set_image(url=res['url'])
    em.set_footer(text=(foother2),icon_url=(icon))
    await ctx.send(embed=em, delete_after=15)

@Mercy.command()
async def pat(ctx, user: discord.User):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/pat")
    res = r.json()
    em = discord.Embed(description=f"**{ctx.author.name} stroked {user.name}** :clap:", color = (colour))
    em.set_image(url=res['url'])
    await ctx.send(embed=em, delete_after=15)

## Others commands

@Mercy.command()
async def ascii(ctx, *, text):
    await ctx.message.delete()
    r = requests.get(f'http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(text)}').text
    if len('```'+r+'```') > 2000:
        return
    await ctx.send(f"```{r}```")


@Mercy.command()
async def logout(ctx):
    await ctx.message.delete()
    await Mercy.logout()

@Mercy.command()
async def spam(ctx, amount: int, *, message):
    await ctx.message.delete()    
    for _i in range(amount):
        await ctx.send(message)

@Mercy.command()
async def massban(ctx): # b'\xfc'
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.ban()
        except:
            pass    

@Mercy.command()
async def masskick(ctx): # b'\xfc'
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.kick()
        except:
            pass    

@Mercy.command()
async def massrole(ctx): # b'\xfc'
    await ctx.message.delete()
    for _i in range(250):
        try:
            await ctx.guild.create_role(name=("Mercy"), color=(colour))
        except:
            return    

@Mercy.command()
async def delchannels(ctx): # b'\xfc'
    await ctx.message.delete()
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            return

@Mercy.command() 
async def delroles(ctx): # b'\xfc'
    await ctx.message.delete()
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass


@Mercy.command()
async def massunban(ctx): # b'\xfc'
    await ctx.message.delete()    
    banlist = await ctx.guild.bans()
    for users in banlist:
        try:
            await asyncio.sleep(2)
            await ctx.guild.unban(user=users.user)
        except:
            pass


@Mercy.command(aliases=["copyguild", "copyserver"])
async def copy(ctx):  # b'\xfc'
    await ctx.message.delete()
    msg = em = discord.Embed(title=f"{titlee}",description = f"Cloning server...\n\nServer : {ctx.guild.name}\nCloning server by : {ctx.author.mention}", color = (colour))
    em.set_thumbnail(url=f"{foto}")
    em.set_footer(text=(foother2),icon_url=(icon))
    await ctx.send(embed=em, delete_after=5)
    await Mercy.create_guild(f'Mercy-{ctx.guild.name}')
    await asyncio.sleep(4)
    for g in Mercy.guilds:
        if f'Mercy-{ctx.guild.name}' in g.name:
            for c in g.channels:
                await c.delete()
            for cate in ctx.guild.categories:
                x = await g.create_category(f"{cate.name}")
                for chann in cate.channels:
                    if isinstance(chann, discord.VoiceChannel):
                        await x.create_voice_channel(f"{chann}")
                    if isinstance(chann, discord.TextChannel):
                        await x.create_text_channel(f"{chann}")
    try:
        await g.edit(icon=ctx.guild.icon_url)
    except:
        pass
    msg = em = discord.Embed(title=f"{titlee}",description = f"Successfully cloned server.", color = (colour))
    em.set_thumbnail(url=f"{foto}")
    em.set_footer(text=(foother2),icon_url=(icon))
    await ctx.send(embed=em, delete_after=15)

@Mercy.command(aliases=['geolocate', 'iptogeo', 'iptolocation', 'ip2geo', 'ip'])
async def geoip(ctx, *, ipaddr: str = '1.3.3.7'): # b'\xfc'
    await ctx.message.delete()
    r = requests.get(f'http://extreme-ip-lookup.com/json/{ipaddr}')
    geo = r.json()
    em = discord.Embed(color = (colour))
    fields = [
        {'name': 'IP', 'value': geo['query']},
        {'name': 'ipType', 'value': geo['ipType']},
        {'name': 'Country', 'value': geo['country']},
        {'name': 'City', 'value': geo['city']},
        {'name': 'Continent', 'value': geo['continent']},
        {'name': 'Country', 'value': geo['country']},
        {'name': 'IPName', 'value': geo['ipName']},
        {'name': 'ISP', 'value': geo['isp']},
        {'name': 'Latitute', 'value': geo['lat']},
        {'name': 'Longitude', 'value': geo['lon']},
        {'name': 'Org', 'value': geo['org']},
        {'name': 'Region', 'value': geo['region']},
        {'name': 'Status', 'value': geo['status']},
    ]
    for field in fields:
        if field['value']:
            em.add_field(name=field['name'], value=field['value'], inline=True)
            em.set_footer(text=(foother2),icon_url=(icon))
    return await ctx.send(embed=em, delete_after=15)

@Mercy.command()
async def purge(ctx, amount : int):
    await ctx.channel.purge(limit=amount)
    embed = discord.Embed(description=f"**BOOM!** \n{amount} deleted messages on this channel.\n\nMessages deleted by {ctx.author.mention}\ndeleted messages : {amount}", color=(colour))
    await ctx.send(embed=embed, delete_after=15)

@Mercy.command()
async def dog(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://dog.ceo/api/breeds/image/random").json()
    em = discord.Embed(title="Random dog image", color = (colour))
    em.set_image(url=str(r['message']))
    try:
        await ctx.send(embed=em, delete_after=15)
    except:
        await ctx.send(str(r['message']))    

@Mercy.command()
async def fox(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get('https://randomfox.ca/floof/').json()
    em = discord.Embed(title="Random fox image", color = (colour))
    em.set_image(url=r["image"])
    try:
        await ctx.send(embed=em, delete_after=15)
    except:
        await ctx.send(r['image'])

@Mercy.command(aliases=['dong', 'penis'])
async def dick(ctx, *, user: discord.User = None): # b'\xfc'
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    size = random.randint(1, 15)
    dong = ""
    for _i in range(0, size):
        dong += "="
    em = discord.Embed(title=f"{user}'s Dick size", description=f"8{dong}D", color = (colour))
    await ctx.send(embed=em, delete_after=15)

@Mercy.command(aliases=['clearconsole', 'consoleclear'])
async def cls(ctx): # b'\xfc'
    await ctx.message.delete()
    Clear()
    startprint()

@Mercy.command(aliases=['slots', 'bet'])
async def slot(ctx): # b'\xfc'
    await ctx.message.delete()
    emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
    a = random.choice(emojis)
    b = random.choice(emojis)
    c = random.choice(emojis)
    slotmachine = f"**[ {a} {b} {c} ]\n{ctx.author.name}**,"
    if (a == b == c):
        await ctx.send(embed=discord.Embed.from_dict({"title":"Slot machine", "description":f"{slotmachine} All matchings, you won!"}, color = (colour)))
    elif (a == b) or (a == c) or (b == c):
        await ctx.send(embed=discord.Embed.from_dict({"title":"Slot machine", "description":f"{slotmachine} 2 in a row, you won!"}, color = (colour)))
    else:
        await ctx.send(embed=discord.Embed.from_dict({"title":"Slot machine", "description":f"{slotmachine} No match, you lost"}, color = (colour)))

@Mercy.command(aliases=["masschannels", "masschannel", "ctc"])
async def spamchannels(ctx, *, message):
    await ctx.message.delete()
    for _i in range(450):
        try:
            await ctx.guild.create_voice_channel(name=message)
        except:
            return

@Mercy.command()
async def embed(ctx, *, message):
    await ctx.message.delete()
    embed = discord.Embed(description=(message), timestamp=ctx.message.created_at, color = (colour))
    await ctx.send(embed=embed)

@Mercy.command(pass_context=True, no_pm=True)
async def avatar(ctx, user: discord.User):
    r = ("{}".format(user.avatar_url))
    em=discord.Embed(title="Avatar URL", url=("{}".format(user.avatar_url)), color = (colour))
    em.add_field(name=f"Avatar", value=f"Avatar of {user.mention} Request for {ctx.author.mention}", inline=False)
    em.set_footer(text=(foother2),icon_url=(icon))
    em.set_image(url=r)
    await ctx.send(embed=em)

@Mercy.command()
async def wizz(ctx):
    await ctx.message.delete()
    if isinstance(ctx.message.channel, discord.TextChannel):
        initial = random.randrange(0, 60)
        message = await ctx.send(f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...\nDeleting {len(ctx.guild.voice_channels)} Voice Channels...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...\nDeleting {len(ctx.guild.voice_channels)} Voice Channels...\nDeleting {len(ctx.guild.categories)} Categories...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...\nDeleting {len(ctx.guild.voice_channels)} Voice Channels...\nDeleting {len(ctx.guild.categories)} Categories...\nDeleting Webhooks...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...\nDeleting {len(ctx.guild.voice_channels)} Voice Channels...\nDeleting {len(ctx.guild.categories)} Categories...\nDeleting Webhooks...\nDeleting Emojis`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...\nDeleting {len(ctx.guild.voice_channels)} Voice Channels...\nDeleting {len(ctx.guild.categories)} Categories...\nDeleting Webhooks...\nDeleting Emojis\nInitiating Ban Wave...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...\nDeleting {len(ctx.guild.voice_channels)} Voice Channels...\nDeleting {len(ctx.guild.categories)} Categories...\nDeleting Webhooks...\nDeleting Emojis\nInitiating Ban Wave...\nInitiating Mass-DM`")
    elif isinstance(ctx.message.channel, discord.DMChannel):
        initial = random.randrange(1, 60)
        message = await ctx.send(
            f"`Wizzing {ctx.message.channel.recipient.name}, will take {initial} seconds to complete`\n")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.message.channel.recipient.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.message.channel.recipient.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.message.channel.recipient.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...\nDeleting {random.randrange(0, 1000)} Pinned Messages...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.message.channel.recipient.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...\nDeleting {random.randrange(0, 1000)} Pinned Messages...\n`")
    elif isinstance(ctx.message.channel, discord.GroupChannel):
        initial = random.randrange(1, 60)
        message = await ctx.send(f"`Wizzing {ctx.message.channel.name}, will take {initial} seconds to complete`\n")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.message.channel.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.message.channel.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.message.channel.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...\nDeleting {random.randrange(0, 1000)} Pinned Messages...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.message.channel.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...\nDeleting {random.randrange(0, 1000)} Pinned Messages...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.message.channel.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...\nDeleting {random.randrange(0, 1000)} Pinned Messages...\nKicking {len(ctx.message.channel.recipients)} Users...`")

@Mercy.command(aliases=["giphy", "tenor", "searchgif"])
async def gif(ctx, query=None):
    await ctx.message.delete()
    if query is None:
        r = requests.get("https://api.giphy.com/v1/gifs/random?api_key=ldQeNHnpL3WcCxJE1uO8HTk17ICn8i34&tag=&rating=R")
        res = r.json()
        await ctx.send(res['data']['url'])

    else:
        r = requests.get(
            f"https://api.giphy.com/v1/gifs/search?api_key=ldQeNHnpL3WcCxJE1uO8HTk17ICn8i34&q={query}&limit=1&offset=0&rating=R&lang=en")
        res = r.json()
        await ctx.send(res['data'][0]["url"])

@Mercy.command(aliases=["jerkoff", "ejaculate", "orgasm"])
async def cum(ctx):
    await ctx.message.delete()
    message = await ctx.send('''
            :ok_hand:            :smile:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant:''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                      :ok_hand:            :smiley:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D 
             :trumpet:      :eggplant:  
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                      :ok_hand:            :grimacing:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant:  
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                      :ok_hand:            :persevere:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D 
             :trumpet:      :eggplant:   
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                      :ok_hand:            :confounded:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant: 
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                       :ok_hand:            :tired_face:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D 
             :trumpet:      :eggplant:    
             ''')
    await asyncio.sleep(0.5)
    await message.edit(contnet='''
                       :ok_hand:            :weary:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:= D:sweat_drops:
             :trumpet:      :eggplant:        
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                       :ok_hand:            :dizzy_face:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D :sweat_drops:
             :trumpet:      :eggplant:                 :sweat_drops:
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                       :ok_hand:            :drooling_face:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D :sweat_drops:
             :trumpet:      :eggplant:                 :sweat_drops:
     ''')


@Mercy.command()
async def poll(ctx, *, arguments):
    await ctx.message.delete()
    lol = await ctx.send(f"`📌 New Poll : {arguments}\nYes : ✅\nNo : ❎`")
    await lol.add_reaction('✅')
    await lol.add_reaction('❎')

@Mercy.command()
async def setprefix(ctx, prefix):
    await ctx.message.delete()
    embed = discord.Embed(title=f"{titlee}",description=f"\nYour new prefix is {prefix}", timestamp=ctx.message.created_at, color = (colour))
    embed.set_thumbnail(url=f"{foto}")
    embed.set_footer(text=(foother2),icon_url=(icon))
    Mercy.command_prefix = str(prefix)
    def Clear():
      os.system('cls')
    Clear()
    startprint()
    await ctx.send(embed=embed, delete_after=15)

@Mercy.command()
async def ping(ctx):
    await ctx.message.delete()
    before = time.monotonic()
    message = await ctx.send("Pinging...")
    ping = (time.monotonic() - before) * 1000
    await message.edit(content=f"`{int(ping)} ms`")

@Mercy.command(name='8ball')
async def _ball(ctx, *, question):
    await ctx.message.delete()
    responses = [
        'That is a resounding no',
        'It is not looking likely',
        'Too hard to tell',
        'It is quite possible',
        'That is a definite yes!',
        'Maybe',
        'There is a good chance'
    ]
    answer = random.choice(responses)
    embed = discord.Embed(color = (colour))
    embed.add_field(name="Question", value=question, inline=False)
    embed.add_field(name="Answer", value=answer, inline=False)
    embed.set_thumbnail(url="https://www.horoscope.com/images-US/games/game-magic-8-ball-no-text.png")
    await ctx.send(embed=embed, delete_after=15)

@Mercy.command()
async def fuck(ctx, user: discord.User):
    await ctx.message.delete()
    fuck = [
        "https://bestanimegifs.com/content/_gifs/hentai/sexcom/14665910_min.gif",
        "https://bestanimegifs.com/content/_gifs/hentai/sexcom/6567739_min.gif",
        "https://bestanimegifs.com/content/_gifs/hentai/sexcom/21113430_min.gif",
        "https://bestanimegifs.com/content/_gifs/hentai/sexcom/20893884_min.gif",
        "https://bestanimegifs.com/content/_gifs/hentai/sexcom/22112363_min.gif",
        "https://bestanimegifs.com/content/_gifs/hentai/sexcom/22162885_min.gif",
        "https://bestanimegifs.com/content/_gifs/hentai/red/badartisticgeese.webp",
        "https://bestanimegifs.com/content/_gifs/hentai/red/silkyuniquefrillneckedlizard.webp",
        "https://bestanimegifs.com/content/_gifs/hentai/sexcom/21963852_min.gif",
        "https://bestanimegifs.com/content/_gifs/hentai/red/tatteredconfuseddegu.webp"
    ]
    fuck2 = random.choice(fuck)
    em = discord.Embed(description=f"**{ctx.author.name} Fucked {user.name}** :eggplant: ", color = (colour))
    em.set_image(url=fuck2)
    em.set_footer(text=(foother2),icon_url=(icon))
    await ctx.send(embed=em, delete_after=15)

@Mercy.command()
async def scared(ctx):
    await ctx.message.delete()
    scared = [
    "https://i.pinimg.com/originals/11/15b/d8/1115bd8a15a0e4df6dce56155be15ee8bc6.gif",
    "https://media.tenor.com/images/e3c2bee748061515d56d7c08b2b15d333/tenor.gif",
    "https://i.pinimg.com/originals/ea/155/1f/ea1551ff587bf8272dafabe16cf258b48.gif",
    "https://media3.giphy.com/media/kT7VY5eUanako/giphy.gif",
    "https://media1.tenor.com/images/3d1e1501564da8453e060865f8f4fb7215a/tenor.gif?itemid=14152802",
    "https://i.imgur.com/dMecNcX.gif",
    "https://pa1.narvii.com/6154/82443332da8eed3f15ac233d815031651563c3f4237_hq.gif",
    "https://media1.tenor.com/images/4115860d26c424de44262e71a15a4e63/tenor.gif?itemid=51545186",
    "https://thumbs.gfycat.com/ShamefulScentedAmericancreamdraft-size_restricted.gif"
    ]
    scared2 = random.choice(scared)
    em = discord.Embed(description=f"**be scared**" , color = (colour))
    em.set_image(url=scared2)
    em.set_footer(text=(foother2),icon_url=(icon))
    await ctx.send(embed=em, delete_after=15)

@Mercy.command()
async def shot(ctx, user: discord.User):
    await ctx.message.delete()
    shot = [
        "https://media1.tenor.com/images/e15c1514be61acb8f2033f2327605c5562/tenor.gif?itemid=81181515",
        "https://i.gifer.com/QCOQ.gif",
        "https://giffiles.alphacoders.com/183/183764.gif",
        "https://i.gifer.com/E60I.gif",
        "http://pa1.narvii.com/64151/afc1515b80b5b3c4123fd7aa7385357eb7450f1d1_00.gif",
        "https://i.imgur.com/zwgjr5A.gif",
        "https://steamuserimages-a.akamaihd.net/ugc/85154715336541476516/0C68DC152415B4158E5BF15B412DE58328AB4AA8365B/",
        "https://cutewallpaper.org/21/anime-guy-holding-gun/Anime-girl-with-gun-GIFs-Get-the-best-GIF-on-GIPHY.gif"
    ]
    shot2 = random.choice(shot)
    em = discord.Embed(description=f"**{ctx.author.name} He has shot him at {user.name}** :gun: ", color = (colour))
    em.set_image(url=shot2)
    em.set_footer(text=(foother2),icon_url=(icon))
    await ctx.send(embed=em, delete_after=15)

@Mercy.command()
async def goodbye(ctx):
    await ctx.message.delete()
    goodbye = [
        "https://i.imgur.com/z015mFD1.gif",
        "https://i.pinimg.com/originals/73/5a/ae/735aae6168d430d11af5b0bc3e724154.gif",
        "https://i.gifer.com/sCO.gif",
        "https://i.imgur.com/IMb15rAx.gif",
        "https://66.media.tumblr.com/0aad8a751503b81567c153c650f0d20cb2/15dcba48158d6d6bc-02/s615x1560/dd15332ad15c3700650e7150f0415167da2426d615c3b.gif",
        "https://media0.giphy.com/media/fxe8v45NNXFd4jdaNI/giphy.gif",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd15GcQkls4QBbQc7cqHKficMk_2YRkhlmX_Xm1zXQ&usqp=CAU"
    ]
    goodbye2 = random.choice(goodbye)
    em = discord.Embed(description="**GoodBye! :D**", color = (colour))
    em.set_image(url=goodbye2)
    em.set_footer(text=(foother2),icon_url=(icon))
    await ctx.send(embed=em, delete_after=15)

@Mercy.command()
async def hello(ctx):
    await ctx.message.delete()
    hello = [
        "https://i.pinimg.com/originals/c2/e2/1a/c2e21a15d8e17c1d335166dbcbe0bd1bf.gif",
        "https://media1.tenor.com/images/3cde3e1fe715e02abdc2873155f57d8578/tenor.gif?itemid=166715443",
        "https://i.gifer.com/Q71.gif",
        "https://media1.tenor.com/images/15724247671543ed34a115f6ff2a15cbe1576/tenor.gif?itemid=141152312",
        "https://media1.tenor.com/images/ae15603eddb6e4bb1ea56cc6de7d0f6e/tenor.gif?itemid=5142315",
        "https://image.myanimelist.net/ui/5LYzTBVoS1156gvYvw3zjwBlFwbSWa-ZYTVw-6154ANEc",
        "https://media1.tenor.com/images/bb3c72152d3c2e75ba4b51ec15bb15bf3b/tenor.gif?itemid=17227125",
        "https://pa1.narvii.com/6118/15fc115face2ae087a1b15cb0547fec15523157b5a07_hq.gif",
        "https://i.pinimg.com/originals/d1/0c/3d/d10c3d215be68153235d157ae768db8c07.gif",
        "http://25.media.tumblr.com/tumblr_lvu5aunkgf1ql1r07o1_500.gif",
        "https://c.tenor.com/BiTbKTFh7uUAAAAC/anime-hi.gif",
        "https://editorani.files.wordpress.com/2018/04/kanbaru-says-hello.gif",
        "https://lazykathere.files.wordpress.com/2015/08/hello.gif"
    ]
    hello2 = random.choice(hello)
    em = discord.Embed(description="**Hello!**", color = (colour))
    em.set_image(url=hello2)
    em.set_footer(text=(foother2),icon_url=(icon))
    await ctx.send(embed=em, delete_after=15)

@Mercy.command()
async def meme(ctx):
    await ctx.message.delete()
    meme = [
        "https://i1.wp.com/www.materiagris.es/wp-content/uploads/2018/10/memes-comunicacion.jpg?fit=700%2C330&ssl=1",
        "https://i.ytimg.com/vi/NdGd1fN-frA/maxresdefault.jpg",
        "https://imagenes.elcomercio.com/files/article_main/uploads/20115/08/215/5d67eefd2a0bd.jpeg",
        "https://www.fundeu.es/wp-content/uploads/2015/02/RecMemes.jpg",
        "http://images7.memedroid.com/images/UPLOADED737/5cf11c01554a81.jpeg",
        "https://i.pinimg.com/originals/68/df/81/68df81cf6da8d285d0815125df703155315.png",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd15GcQDAzvG72xF0PdskK2NtUDn6Ppsu_01WycLA6xGE4CRqLnqoVi2RIzp8iojGwRrCjKmkgE&usqp=CAU",
        "https://i.ytimg.com/vi/gjahqHb1v8k/maxresdefault.jpg",
        "https://img.wattpad.com/cover/1151803432-256-k420541.jpg",
        "https://enportada.cl/wp-content/uploads/2021/02/15021515481_151587155181557763_575123506153241528820_n.jpg",
        "https://i.ytimg.com/vi/AqixvtnaUYY/hqdefault.jpg?sqp=-oaymwEjCOADEI4CSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLCiG4QZ3MY11XNV60UuxRIMHs5XbA",
        "https://lh3.googleusercontent.com/proxy/dXQQGi15e5i8E4aWwg8dGrus8Y_gwG8CXBbNHSDK4Qvoo3PIsPGaxIPvZR3sUC6XS6e_A_ItoS15SCv0HEkeQ15JBizBfPr5Hee0p-toWln61mr3xkNGgnWkQWX-w",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd15GcRd2NQz015P6sVHNBm-JpXv2OG4ymw6NHsaalg&usqp=CAU",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd15GcSmrAMNTqpaplw3rh7ZOrHWhdgD0agg0sIojA&usqp=CAU",
        "https://www.12minutos.com/thumb/4/d/8/6/d86e87dfe4728b761b3f152adf68f6c03.jpg",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd15GcQYIiKnJoNGmz15kfzpgmeaWimzxWTJFuG7efg&usqp=CAU",
        "https://p16-va-tiktok.ibyteimg.com/img/musically-maliva-obj/be1be1bfc15a071515f61a41bca44fe0a5~c5_720x720.jpeg",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd15GcTjyVNpDNANDz7UCUh_GN-Kb5N0-yr15CqxOsA&usqp=CAU",
        "https://i.playboard.app/p/AATXAJxcX63Xvv05DTaiStAapusMxFsIwA0jbWFCA-J2oA/default.jpg",
        "https://pbs.twimg.com/profile_images/15831072712815815015/GXXiPcA4_150x150.jpg",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd15GcSCmU1yz0-p2rTTdM_4bUK15tLt15NcxZcdfsDlgMtHrZ6h_sut0OpuoCo15AI6ut6mGSuEoE&usqp=CAU",
    ]
    meme2 = random.choice(meme)
    em = discord.Embed(color = (colour))
    em.set_image(url=meme2)
    embed.set_footer(text=(foother2),icon_url=(icon))
    await ctx.send(embed=em, delete_after=15)

@Mercy.command()
async def blushed(ctx):
    await ctx.message.delete()
    meme = [
    "http://i.imgur.com/jvAzMIF.gif",
    "https://media1.tenor.com/images/4b333a215e3546eede31e64e5d215b74da/tenor.gif?itemid=154528515",
    "https://acegif.com/wp-content/gif/blushing-33.gif",
    "https://64.media.tumblr.com/155c5c8d001881c2e218a1de85e2615e1/tumblr_o0oylrTLtx1smsv7zo1_500.gifv",
    "https://i.pinimg.com/originals/10/42/5b/10425bd8382e2ec515a864b7055f158b38.gif",
    "http://pa1.narvii.com/60515/8d281b3608c735b65cf15063ba2ef815151515ec085b3_00.gif",
    "https://s-media-cache-ak0.pinimg.com/originals/fd/4f/fa/fd4ffaeff5127cd7aaab3281d1f3656b.gif",
    "https://i.imgur.com/ED6l1fW.gif?noredirect",
    "https://thumbs.gfycat.com/NeatAcrobaticAmericanwigeon-size_restricted.gif",
    "https://i.pinimg.com/originals/47/fe/a1/47fea171527f5e62dfc054146851c3fee.gif",
    "https://pa1.narvii.com/6235/e10735310a21468e0463c0801156b5f7e78e3b6a_hq.gif",
    "https://i.pinimg.com/originals/b8/5f/8c/b85f8c1517f78503d3f1503f15a24b4438e.gif",
    "https://radiood1.files.wordpress.com/2015/01/e32f2-736784_170x100-png.gif"
]
    meme2 = random.choice(meme)
    em = discord.Embed(description="**blushed**", color = (colour))
    em.set_image(url=meme2)
    embed.set_footer(text=(foother2),icon_url=(icon))
    await ctx.send(embed=em, delete_after=15)


@Mercy.command(aliases=["15/11", "1511", "terrorist"])
async def boom(ctx):
    await ctx.message.delete()
    invis = ""  # char(173)
    message = await ctx.send(f'''
{invis}:man_wearing_turban::airplane:    :office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
{invis} :man_wearing_turban::airplane:   :office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
{invis}  :man_wearing_turban::airplane:  :office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
{invis}   :man_wearing_turban::airplane: :office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
{invis}    :man_wearing_turban::airplane::office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
        :boom::boom::boom:    
        ''')

@Mercy.command()
async def shrug(ctx):
    await ctx.message.delete()
    shrug = r'¯\_(ツ)_/¯'
    await ctx.send(shrug)


@Mercy.command()
async def lenny(ctx):
    await ctx.message.delete()
    lenny = '( ͡° ͜ʖ ͡°)'
    await ctx.send(lenny)


@Mercy.command(aliases=["fliptable"])
async def tableflip(ctx):
    await ctx.message.delete()
    tableflip = '(╯°□°）╯︵ ┻━┻'
    await ctx.send(tableflip)


@Mercy.command()
async def unflip(ctx):
    await ctx.message.delete()
    unflip = '┬─┬ ノ( ゜-゜ノ)'
    await ctx.send(unflip)

def Nitro():
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    return f'https://discord.gift/{code}'

@Mercy.command()
async def nitro(ctx):
    await ctx.message.delete()
    await ctx.send(Nitro())

@Mercy.command()
async def virus(ctx):
    await ctx.message.delete()
    invis = ""  # char(173)
    message = await ctx.send(f'''
``[▓▓▓                    ] / -virus.exe Packing files.``        
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
``[▓▓▓▓▓▓▓                ] - -virus.exe Packing files..``         
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
``[▓▓▓▓▓▓▓▓▓▓▓▓           ] \ -virus.exe Packing files..``        
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓         ] | -virus.exe Packing files..``         
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      ] / -virus.exe Packing files..``      
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   ] - -virus.exe Packing files..``    
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ] \ -virus.exe Packing files..``   
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
``New file with name change, New file : Mercy.exe``   
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
``Injecting virus.   |``
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
``Injecting virus..  /``
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
``Injecting virus... -``
''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
        ``Successfully Injected Mercy.exe :D``
        ''')

@Mercy.command()
async def table(ctx):
    await ctx.message.delete()
    invis = ""  # char(173)
    message = await ctx.send(f'''
`(\°-°)\  ┬─┬`       
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`(\°□°)\  ┬─┬`       
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`(-°□°)-  ┬─┬`      
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`(╯°□°)╯    ]`       
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`(╯°□°)╯     ┻━┻`   
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`(╯°□°)╯       [`
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`(╯°□°)╯          ┬─┬`   
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`(╯°□°)╯                 ]`   
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`(╯°□°)╯                  ┻━┻`
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`(╯°□°)╯                         [`
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`(\°-°)\                               ┬─┬`
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`(\°-°)\                                     ]`
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`(\°-°)\                                       ┻━┻`
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`(\°-°)\                                               [`
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`(\°-°)\                                              ┬─┬`
''')
    await asyncio.sleep(0.50)
    await message.edit(content='''
        `XD`
        ''')


@Mercy.command()
async def horney(ctx):
    await ctx.message.delete()
    invis = ""  # char(173)
    message = await ctx.send(f'''
```[▓▓▓                    ] / Uploading``` 
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
```[▓▓▓▓▓▓▓                ] - Uploading.```
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
```[▓▓▓▓▓▓▓▓▓▓▓▓           ] \ Uploading..```   
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
```[▓▓▓▓▓▓▓▓▓▓▓▓▓▓         ] | Uploading...```       
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
```[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      ] / Uploading.```   
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
```[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   ] - Uploading..```
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
```[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ] \ Uploading...```   
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
```Failed to load NSFW video into Channel```  
''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
    `Contact Guild owner to get more porn perms!`
        ''')


@Mercy.command()
async def wtf(ctx):
    await ctx.message.delete()
    invis = ""  # char(173)
    message = await ctx.send(f'''
`W` 
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`Wh`
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`Wha`   
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`What`       
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`What `   
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`What T`
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`What Th`   
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`What The`  
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`What The F` 
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`What The Fu`  
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`What The Fuc`  
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`What The Fuck`  
''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
    `What The Fuck!`
        ''')

@Mercy.command()
async def ddos(ctx, user: discord.User):
    await ctx.message.delete()
    fakeip = [
        "45.186.255.38",
        "152.154.23.1156:1080",
        "31.146.44.35:4153",
        "103.232.33.147:1080",
        "177.184.67.615:4145",
        "1.2.2015.44:4145",
        "1151.1815.30.85:5151585",
        "45.125.63.46:44110",
        "103.47.153.220:1080",
        "101.255.125.515:4145",
        "110.77.155.112:4153",
        "103.155.15.20:4145"
    ]
    fakeip2 = random.choice(fakeip)
    message = await ctx.send(f'''
`Starting the DDos ​​to {user.mention}, 5 seconds left for the DDos to start | IP : {fakeip2}`
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`Starting the DDos ​​to {user.mention}, 4 seconds left for the DDos to start | IP : {fakeip2}`
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`Starting the DDos ​​to {user.mention}, 3 seconds left for the DDos to start | IP : {fakeip2}` 
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`Starting the DDos ​​to {user.mention}, 2 seconds left for the DDos to start | IP : {fakeip2}`     
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`Starting the DDos ​​to {user.mention}, 1 seconds left for the DDos to start | IP : {fakeip2}`    
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`Starting the DDos ​​to {user.mention}, 0 seconds left for the DDos to start | IP : {fakeip2}`   
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`DDos to {user.mention} victim's ip {fakeip2}`  
''')

@Mercy.command()
async def lmfao(ctx):
    await ctx.message.delete()
    invis = ""  # char(173)
    message = await ctx.send(f'''
`L` 
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`LM`
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`LMF`   
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`LMFA`       
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`LMFAO `   
''')

afkdict = {}
@Mercy.command(name = "afk", brief = "Away From Keyboard",
                description = "I'll give you the afk status and if someone pings you before you come back, I'll tell "
                              "them that you are not available. You can add your own afk message!")
async def afk(ctx, message = "They didn't leave a message!"):
    global afkdict

    if ctx.message.author in afkdict:
        afkdict.pop(ctx.message.author)
        embed = discord.Embed(title=f"{titlee} | AFK MODE (OFF)",color = (colour), description=f"**{ctx.author.mention} has returned, say hello!**")
        embed.set_thumbnail(url=f"{foto}")
        embed.set_footer(text=(foother2),icon_url=(icon))
        await ctx.send(embed=embed, delete_after=15)

    else:
        afkdict[ctx.message.author] = message
        embed = discord.Embed(title=f"{titlee} | AFK MODE (ON)",color = (colour), description=f"**{ctx.author.mention} has set afk mode\n\nReason : {message}**")
        embed.set_thumbnail(url=f"{foto}")
        embed.set_footer(text=(foother2),icon_url=(icon))
        await ctx.send(embed=embed, delete_after=15)


@Mercy.event
async def on_message(message):
    global afkdict

    for member in message.mentions:  
        if member != message.author:  
            if member in afkdict:  
                afkmsg = afkdict[member]  
                await message.channel.send(f"**Oh no, it looks like {member} is afk right now, please call him later\n\nReason : {afkmsg}**")
    await Mercy.process_commands(message)

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

@Mercy.command()
async def restart(ctx):
    await ctx.message.delete()
    cmd = "mode 120,25"
    os.system(cmd)
    embed = discord.Embed(title = titlee, color=colour, description="Restarting")
    embed.set_thumbnail(url="https://media.giphy.com/media/3oEjI6SIIHBdRxXI40/200.gif")
    await ctx.send(embed=embed)
    restart_program()

@Mercy.command()
async def egg(ctx):
    await ctx.message.delete()
    await ctx.send(f"Mercy Say : Oh boy did you find an easter egg, look at the console to see it. {ctx.author.mention}")
    egg1 = [
        "Did you know that the first versions of the selfbot were called Lunar. 1/5",
        "When he thinks the selfbot was eating mashed potatoes. 2/5",
        "My first customers were my friends xD. 3/5",
        "I was more than once to nothing to leave the selfbot 4/5",
        "I currently live in Chile but I would like to go live in Canada 5/5"
    ]
    egg2 = random.choice(egg1)
    ctypes.windll.kernel32.SetConsoleTitleW(f"{egg2}")
    sleep(5.80)

@Mercy.command(aliases=['tokenfucker', 'disable', 'crash'])
async def tokenfuck(ctx, _token):
    await ctx.message.delete()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/200501515 Firefox/1.0.7',
        'Content-Type': 'application/json',
        'Authorization': _token,
    }
    request = requests.Session()
    payload = {
        'theme': "light",
        'locale': "ja",
        'message_display_compact': False,
        'inline_embed_media': False,
        'inline_attachment_media': False,
        'gif_auto_play': False,
        'render_embeds': False,
        'render_reactions': False,
        'animate_emoji': False,
        'convert_emoticons': False,
        'enable_tts_command': False,
        'explicit_content_filter': '0',
        'status': "invisible"
    }
    guild = {
        'channels': True,
        'icon': "https://i.imgur.com/INaRWfZ.png",
        'name': "Mercy",
        'region': "europe"
    }
    for _i in range(50):
        requests.post('https://discordapp.com/api/v6/guilds', headers=headers, json=guild)
    while True:
        try:
            request.patch("https://canary.discordapp.com/api/v6/users/@me/settings", headers=headers, json=payload)
        except Exception as e:
            print(f"[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
        else:
            break
    modes = cycle(["light", "dark"])
    statuses = cycle(["online", "idle", "dnd", "invisible"])
    while True:
        setting = {
            'theme': next(modes),
            'locale': random.choice(locales),
            'status': next(statuses)
        }
        while True:
            try:
                request.patch("https://canary.discordapp.com/api/v6/users/@me/settings", headers=headers, json=setting,
                              timeout=10)
            except Exception as e:
                print(f"[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
            else:
                break

@Mercy.command(aliases=['tokinfo', 'tdox'])
async def tokeninfo(ctx, _token):
    await ctx.message.delete()
    headers = {
        'Authorization': _token,
        'Content-Type': 'application/json'
    }
    try:
        res = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers)
        res = res.json()
        user_id = res['id']
        locale = res['locale']
        avatar_id = res['avatar']
        language = languages.get(locale)
        creation_date = datetime.datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070150000) / 1000).strftime(
            '%d-%m-%Y %H:%M:%S UTC')
    except KeyError:
        headers = {
            'Authorization': "Bot " + _token,
            'Content-Type': 'application/json'
        }
        try:
            res = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers)
            res = res.json()
            user_id = res['id']
            locale = res['locale']
            avatar_id = res['avatar']
            language = languages.get(locale)
            creation_date = datetime.datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070150000) / 1000).strftime(
                '%d-%m-%Y %H:%M:%S UTC')
            em = discord.Embed(
                description=f"Name: `{res['username']}#{res['discriminator']} ` **BOT**\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`")
            fields = [
                {'name': 'Flags', 'value': res['flags']},
                {'name': 'Local language', 'value': res['locale'] + f"{language}"},
                {'name': 'Verified', 'value': res['verified']},
            ]
            for field in fields:
                if field['value']:
                    em.add_field(name=field['name'], value=field['value'], inline=False)
                    em.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}")
            return await ctx.send(embed=em)
        except KeyError:
            await ctx.send("Invalid token")
    em = discord.Embed(
        description=f"Name: `{res['username']}#{res['discriminator']}`\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`")
    # em.set_footer(text=_token)
    nitro_type = "None"
    if "premium_type" in res:
        if res['premium_type'] == 2:
            nitro_type = "Nitro Premium"
        elif res['premium_type'] == 1:
            nitro_type = "Nitro Classic"
    fields = [
        {'name': 'Phone', 'value': res['phone']},
        {'name': 'Flags', 'value': res['flags']},
        {'name': 'Local language', 'value': res['locale'] + f"{language}"},
        {'name': 'MFA', 'value': res['mfa_enabled']},
        {'name': 'Verified', 'value': res['verified']},
        {'name': 'Nitro', 'value': nitro_type},
    ]
    for field in fields:
        if field['value']:
            em = discord.Embed(title=(titlee), color = colour)
            em.add_field(name=field['name'], value=field['value'], inline=False)
            em.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}")
            em.set_footer(text=(foother2),icon_url=(icon))
    return await ctx.send(embed=em)

def RandomColor():
    randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
    return randcolor

@Mercy.command()
async def abc(ctx):
    await ctx.message.delete()
    ABC = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z']
    message = await ctx.send(ABC[0])
    await asyncio.sleep(2)
    for _next in ABC[1:]:
        await message.edit(content=_next)
        await asyncio.sleep(2)

@Mercy.command()
async def tweet(ctx, username: str = None, *, message: str = None):
    await ctx.message.delete()
    if username is None or message is None:
        await ctx.send("missing parameters")
        return
    async with aiohttp.ClientSession() as cs:
        async with cs.get(f"https://nekobot.xyz/api/imagegen?type=tweet&username={username}&text={message}") as r:
            res = await r.json()
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(str(res['message'])) as resp:
                        image = await resp.read()
                with io.BytesIO(image) as file:
                    await ctx.send(file=discord.File(file, f"Mercy_tweet.png"))
            except:
                await ctx.send(res['message'])

@Mercy.command(aliases=["distort"])
async def magik(ctx, user: discord.Member = None):
    await ctx.message.delete()
    endpoint = "https://nekobot.xyz/api/imagegen?type=magik&intensity=3&image="
    if user is None:
        avatar = str(ctx.author.avatar_url_as(format="png"))
        endpoint += avatar
        r = requests.get(endpoint)
        res = r.json()
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(str(res['message'])) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Mercy_magik.png"))
        except:
            await ctx.send(res['message'])
    else:
        avatar = str(user.avatar_url_as(format="png"))
        endpoint += avatar
        r = requests.get(endpoint)
        res = r.json()
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(str(res['message'])) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Mercy_magik.png"))
        except:
            await ctx.send(res['message'])

@Mercy.command(aliases=["deepfry"])
async def fry(ctx, user: discord.Member = None):
    await ctx.message.delete()
    endpoint = "https://nekobot.xyz/api/imagegen?type=deepfry&image="
    if user is None:
        avatar = str(ctx.author.avatar_url_as(format="png"))
        endpoint += avatar
        r = requests.get(endpoint)
        res = r.json()
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(str(res['message'])) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Mercy_fry.png"))
        except:
            await ctx.send(res['message'])
    else:
        avatar = str(user.avatar_url_as(format="png"))
        endpoint += avatar
        r = requests.get(endpoint)
        res = r.json()
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(str(res['message'])) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Mercy_fry.png"))
        except:
            await ctx.send(res['message'])

@Mercy.command()
async def whois(ctx, *, user: discord.Member = None):
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    if isinstance(ctx.message.channel, discord.Guild):
        date_format = "%a, %d %b %Y %I:%M %p"
        em = discord.Embed(description=user.mention)
        em.set_author(name=str(user), icon_url=user.avatar_url)
        em.set_thumbnail(url=user.avatar_url)
        em.add_field(name="Registered", value=user.created_at.strftime(date_format))
        em.add_field(name="Joined", value=user.joined_at.strftime(date_format))
        members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
        em.add_field(name="Join position", value=str(members.index(user) + 1))
        if len(user.roles) > 1:
            role_string = ' '.join([r.mention for r in user.roles][1:])
            em.add_field(name="Roles [{}]".format(len(user.roles) - 1), value=role_string, inline=False)
        perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]])
        em.add_field(name="Permissions", value=perm_string, inline=False)
        em.set_footer(text='ID: ' + str(user.id))
        return await ctx.send(embed=em, delete_after=15)
    else:
        date_format = "%a, %d %b %Y %I:%M %p"
        em = discord.Embed(description=user.mention)
        em.set_author(name=str(user), icon_url=user.avatar_url)
        em.set_thumbnail(url=user.avatar_url)
        em.add_field(name="Created", value=user.created_at.strftime(date_format))
        em.set_footer(text='ID: ' + str(user.id))
        return await ctx.send(embed=em, delete_after=15)

@Mercy.command()
async def sad(ctx):
    await ctx.message.delete()
    sad1 = [
        "https://i.pinimg.com/originals/9f/6b/7b/9f6b7bf8ba47fe7915e34b44a9db105c.gif",
        "https://media1.tenor.com/images/2bd485a5d2b8600a78ca0b82adbb2dde/tenor.gif?itemid=16156194",
        "https://monophy.com/media/T4COazRlurxKM/monophy.gif",
        "https://i.gifer.com/2SJT.gif",
        "https://i.pinimg.com/originals/2f/b2/96/2fb2965acbf3ed573e8b63080b947fe5.gif",
        "https://media1.tenor.com/images/42caf637a1772c4735d1f74b59273f55/tenor.gif?itemid=16604973"
    ]
    sad2 = random.choice(sad1)
    em = discord.Embed(color = (colour), description=f"**{ctx.author.mention} is sad :(**")
    em.set_image(url=sad2)
    em.set_footer(text=(foother2),icon_url=(icon))
    await ctx.send(embed=em, delete_after=15)

@Mercy.command()
async def SAD(ctx):
    await ctx.message.delete()
    sad1 = [
        "https://i.pinimg.com/originals/9f/6b/7b/9f6b7bf8ba47fe7915e34b44a9db105c.gif",
        "https://media1.tenor.com/images/2bd485a5d2b8600a78ca0b82adbb2dde/tenor.gif?itemid=16156194",
        "https://monophy.com/media/T4COazRlurxKM/monophy.gif",
        "https://i.gifer.com/2SJT.gif",
        "https://i.pinimg.com/originals/2f/b2/96/2fb2965acbf3ed573e8b63080b947fe5.gif",
        "https://media1.tenor.com/images/42caf637a1772c4735d1f74b59273f55/tenor.gif?itemid=16604973"
    ]
    sad2 = random.choice(sad1)
    em = discord.Embed(color = (colour), description=f"**{ctx.author.mention} is sad :(**")
    em.set_image(url=sad2)
    em.set_footer(text=(foother2),icon_url=(icon))
    await ctx.send(embed=em, delete_after=15)

@Mercy.command()
async def advance(ctx):
    await ctx.message.delete()
    os.system("cls")
    print(f'''

\t\t\t              {Fore.WHITE}███{asciicolor}╗{Fore.WHITE}   ███{asciicolor}╗{Fore.WHITE}███████{asciicolor}╗{Fore.WHITE}██████{asciicolor}╗  {Fore.WHITE}██████{asciicolor}╗{Fore.WHITE}██{asciicolor}╗   {Fore.WHITE}██{asciicolor}╗
\t\t\t              {Fore.WHITE}████{asciicolor}╗{Fore.WHITE} ████{asciicolor}║{Fore.WHITE}██{asciicolor}╔════╝{Fore.WHITE}██{asciicolor}╔══{Fore.WHITE}██{asciicolor}╗{Fore.WHITE}██{asciicolor}╔════╝╚{Fore.WHITE}██{asciicolor}╗ {Fore.WHITE}██{asciicolor}╔╝
\t\t\t              {Fore.WHITE}██{asciicolor}╔{Fore.WHITE}████{asciicolor}╔{Fore.WHITE}██{asciicolor}║{Fore.WHITE}█████{asciicolor}╗{Fore.WHITE}  ██████{asciicolor}╔╝{Fore.WHITE}██{asciicolor}║      ╚{Fore.WHITE}████{asciicolor}╔╝ 
\t\t\t              {Fore.WHITE}██{asciicolor}║╚{Fore.WHITE}██{asciicolor}╔╝{Fore.WHITE}██{asciicolor}║{Fore.WHITE}██{asciicolor}╔══╝  {Fore.WHITE}██{asciicolor}╔══{Fore.WHITE}██{asciicolor}╗{Fore.WHITE}██{asciicolor}║       {asciicolor}╚{Fore.WHITE}██{asciicolor}╔╝  
\t\t\t              {Fore.WHITE}██{asciicolor}║ ╚═╝{Fore.WHITE} ██{asciicolor}║{Fore.WHITE}███████{asciicolor}╗{Fore.WHITE}██{asciicolor}║ {Fore.WHITE} ██{asciicolor}║╚{Fore.WHITE}██████{asciicolor}╗   {Fore.WHITE}██{asciicolor}║   
\t\t\t              {asciicolor}╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝   ╚═╝  {Fore.RESET}
\t\t\t              {asciicolor}           {Fore.WHITE}Mercy {asciicolor}all settings.

{Fore.WHITE}――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――{Fore.RESET}
{Fore.WHITE} [{asciicolor}+{Fore.WHITE}] {asciicolor}MERCY SETTINGS.      

{Fore.WHITE} [{asciicolor}+{Fore.WHITE}] {asciicolor}Loggin in as :{Fore.WHITE} {Mercy.user.name}#{Mercy.user.discriminator}   
{Fore.WHITE} [{asciicolor}+{Fore.WHITE}] {asciicolor}Prefix :{Fore.WHITE} {Mercy.command_prefix}                            
{Fore.WHITE}――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――{Fore.RESET}
{Fore.WHITE} [{asciicolor}+{Fore.WHITE}] {asciicolor}USER PRENCESE.

{Fore.WHITE} [{asciicolor}+{Fore.WHITE}] {asciicolor}STREAMING URL :{Fore.WHITE} {stream_url}
{Fore.WHITE} [{asciicolor}+{Fore.WHITE}] {asciicolor}CUSTOM STATUTS :{Fore.WHITE} {one} - {two} - {three}  
{Fore.WHITE}――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――{Fore.RESET}
{Fore.WHITE} [{asciicolor}+{Fore.WHITE}] {asciicolor}MERCY CUSTOMIZATION.

{Fore.WHITE} [{asciicolor}+{Fore.WHITE}] {asciicolor}EMBED TITLE :{Fore.WHITE} {titlee}
{Fore.WHITE} [{asciicolor}+{Fore.WHITE}] {asciicolor}EMBED THUMBNAIL :{Fore.WHITE} {foto}
{Fore.WHITE} [{asciicolor}+{Fore.WHITE}] {asciicolor}EMBED COLOR :{Fore.WHITE} 0x{colour}

[{asciicolor}Mercy say{Fore.WHITE}] Type "{Mercy.command_prefix}back" to return to the main menu.''')

@Mercy.command()
async def back(ctx):
    await ctx.message.delete()
    os.system("cls")
    startprint()

@Mercy.command()
async def BACK(ctx):
    await ctx.message.delete()
    os.system("cls")
    startprint()

@Mercy.command()
async def iq(ctx, user: discord.User):
    await ctx.message.delete()
    iq = [
        "50 IQ",
        "100 IQ",
        "20 IQ",
        "10 IQ",
        "30 IQ",
        "40 IQ",
        "2 IQ",
        "1 IQ",
        "NO IQ IS RETARD",
        "1000 IQ",
        "2000 IQ",
        "5000 IQ",
        "100000000000 IQ IS EINSTEIN WTF"
    ]
    imgq = [
        "https://pngimage.net/wp-content/uploads/2018/06/monkas-png-7.png",
        "https://tlgrm.es/_/stickers/108/979/10897963-eca0-3034-8344-3012b5605373/9.jpg",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSvCGdeUpXi1WxdMbcCp8o0gN9Ana_2x9sOgXweEt5jiGiSaiGMvPyAKHgA0dae2F_7rBI&usqp=CAU"
    ]
    imgiq = random.choice(imgq)
    iq2 = random.choice(iq)
    em = discord.Embed(description=f" **{iq2} {user.name}** :exploding_head:", color = (colour))
    em.set_image(url=f"{imgiq}")
    em.set_footer(text=(foother2),icon_url=(icon))
    await ctx.send(embed=em, delete_after=15)

@Mercy.command()
async def tickle(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/tickle")
    res = r.json()
    em = discord.Embed(color=colour, description=f"**{ctx.author.name} Tickle {user.name}**")
    em.set_image(url=res['url'])
    em.set_footer(text=(foother2),icon_url=(icon))
    await ctx.send(embed=em, delete_after=15)

@Mercy.command()
async def cuddle(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/cuddle")
    res = r.json()
    em = discord.Embed(color=colour, description=f"**{ctx.author.name} Cuddle {user.name}**")
    em.set_image(url=res['url'])
    em.set_footer(text=(foother2),icon_url=(icon))
    await ctx.send(embed=em, delete_after=15)

@Mercy.command()
async def style1(ctx):
    await ctx.message.delete()
    os.system("cls")
    ctypes.windll.kernel32.SetConsoleTitleW(f"Mercy {version} | Style 1 | Type {Mercy.command_prefix}back to return a default style")
    print(f'''{Fore.RESET}――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

\t\t\t                      _  _ ____ ____ ____ _   _ 
\t\t\t                      |\/| |___ |__/ |     \_/  
\t\t\t                      |  | |___ |  \ |___   |   

\t\t\t                   {Fore.WHITE}[{asciicolor}!{Fore.WHITE}] Logged in as >> {Mercy.user.name}#{Mercy.user.discriminator} 
\t\t\t                   {Fore.WHITE}[{asciicolor}!{Fore.WHITE}] Prefix is >> {Mercy.command_prefix}
\t\t\t                   {Fore.WHITE}[{asciicolor}!{Fore.WHITE}] Mercy with RPC Mode.

{Fore.RESET}――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――{Fore.RESET}''' + Fore.RESET)

@Mercy.command()
async def style2(ctx):
    await ctx.message.delete()
    os.system("cls")
    ctypes.windll.kernel32.SetConsoleTitleW(f"Mercy {version} | Style 2 | Type {Mercy.command_prefix}back to return a default style")
    print(f'''{Fore.RESET}――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

\t\t\t           __  __  U _____ u   ____       ____  __   __ 
\t\t\t         U|' \/ '|u\| ___"|/U |  _"\ u U /"___| \ \ / / 
\t\t\t         \| |\/| |/ |  _|"   \| |_) |/ \| | u    \ V /  
\t\t\t          | |  | |  | |___    |  _ <    | |/__  U_|"|_u 
\t\t\t          |_|  |_|  |_____|   |_| \_\    \____|   |_|   
\t\t\t          <<,-,,-.   <<   >>   //   \\_  _// \\.-,//|(_  
\t\t\t          (./  \.) (__) (__) (__)  (__)(__)(__)\_) (__)   

\t\t\t              {Fore.WHITE}[{asciicolor}${Fore.WHITE}] Logged in as >> {Mercy.user.name}#{Mercy.user.discriminator} 
\t\t\t              {Fore.WHITE}[{asciicolor}${Fore.WHITE}] Prefix is >> {Mercy.command_prefix}
\t\t\t              {Fore.WHITE}[{asciicolor}${Fore.WHITE}] Mercy with RPC Mode.

{Fore.RESET}――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――{Fore.RESET}''' + Fore.RESET)

@Mercy.command()
async def style3(ctx):
    await ctx.message.delete()
    cmd = "mode 70,20"
    os.system(cmd)
    os.system("cls")
    ctypes.windll.kernel32.SetConsoleTitleW(f"Mercy {version} | Style 3 | Type {Mercy.command_prefix}back to return a default style")
    print(f'''―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

\t\t          {asciicolor}╔╦╗ {Fore.WHITE}╔═╗ {asciicolor}╦═╗ {Fore.WHITE}╔═╗{asciicolor} ╦ ╦
\t\t          {asciicolor}║║║ {Fore.WHITE}║╣  {asciicolor}╠╦╝ {Fore.WHITE}║  {asciicolor} ╚╦╝
\t\t          {asciicolor}╩ ╩ {Fore.WHITE}╚═╝ {asciicolor}╩╚═ {Fore.WHITE}╚═╝{asciicolor}  ╩  
\t\t     -----------------------------
\t\t    {Fore.WHITE}[{asciicolor}-{Fore.WHITE}] Logged in as >> {Mercy.user.name}#{Mercy.user.discriminator} 
\t\t    {Fore.WHITE}[{asciicolor}-{Fore.WHITE}] Prefix is >> {Mercy.command_prefix}
\t\t    {Fore.WHITE}[{asciicolor}-{Fore.WHITE}] Mercy with RPC Mode.

{Fore.RESET}―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――{Fore.RESET}''' + Fore.RESET)

@Mercy.command()
async def amongus(ctx):
    await ctx.message.delete()
    await ctx.send("ඞ")

@Mercy.command()
async def help(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title=f"{titlee}", color=colour, description=f'''**{Mercy.command_prefix}funny** -> Show all funny commands.
    **{Mercy.command_prefix}misc** -> Show all misc commands.
    **{Mercy.command_prefix}nsfw** -> Show all nsfw commands.
    **{Mercy.command_prefix}image** -> Show all image commands.
    **{Mercy.command_prefix}text** -> Show all text commands.
    **{Mercy.command_prefix}raid** -> Show all raid commands.
    **{Mercy.command_prefix}status** -> Show all status commands.
    **{Mercy.command_prefix}themes** -> Show all mercy themes.
    **{Mercy.command_prefix}new** -> Show all new mercy commands.
    **{Mercy.command_prefix}changecolor** -> Show all console colors.
    **{Mercy.command_prefix}selfbot** -> Show all selfbot commands.
    ''')
    embed.set_thumbnail(url=(foto))
    embed.set_footer(text=(foother2),icon_url=(icon))
    await ctx.send(embed=embed, delete_after=15)

@Mercy.command()
async def funny(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title=f"{titlee}", color=colour, description=f'''
    **{Mercy.command_prefix}kiss <user> - kisses the mentioned user.
    {Mercy.command_prefix}slap <user> - slap the mentioned user.
    {Mercy.command_prefix}pat <user> - pat the mentioned user.
    {Mercy.command_prefix}tickle <user> - tickle the mentioned user.
    {Mercy.command_prefix}shot <user> - shot the mentioned user.
    {Mercy.command_prefix}iq <user> - user iq.
    {Mercy.command_prefix}slot - slotmachine.
    {Mercy.command_prefix}dick <user> - dick side.**
    ''')
    embed.set_thumbnail(url=(foto))
    embed.set_footer(text=(foother2),icon_url=(icon))
    await ctx.send(embed=embed, delete_after=15)

@Mercy.command()
async def nsfw(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title=f"{titlee}", color=colour, description=f'''
    **{Mercy.command_prefix}fuck <user> - fuck the mentioned user
    {Mercy.command_prefix}anal - anal gif or image
    {Mercy.command_prefix}lesbian - lesbian gif or image
    {Mercy.command_prefix}blowjob - blowjob gif or image
    {Mercy.command_prefix}boobs - boobs gif or image
    {Mercy.command_prefix}cuddle - cuddle gif or image
    {Mercy.command_prefix}cum - cum gif or image
    {Mercy.command_prefix}cumslut - cumslut gif or image
    {Mercy.command_prefix}tits - tits gif or image
    {Mercy.command_prefix}pussy - pussy gif or image**
    ''')
    embed.set_thumbnail(url=(foto))
    embed.set_footer(text=(foother2),icon_url=(icon))
    await ctx.send(embed=embed, delete_after=15)

@Mercy.command()
async def image(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title=f"{titlee}", color=colour, description=f'''{Mercy.command_prefix}avatar <user> - show discord avatar**
    {Mercy.command_prefix}dogg - random dog image**
    {Mercy.command_prefix}fox - random fox image**
    {Mercy.command_prefix}gif - random gif**
    {Mercy.command_prefix}fry <user> - fry edit user avatar**
    {Mercy.command_prefix}tweet <name> <text> - fake tweet image**
    {Mercy.command_prefix}magik <user> - magik?
    {Mercy.command_prefix}meme - random meme.
    ''')
    embed.set_thumbnail(url=(foto))
    embed.set_footer(text=(foother2),icon_url=(icon))
    await ctx.send(embed=embed, delete_after=15)

@Mercy.command()
async def text(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title=f"{titlee}", color=colour, description=f'''**{Mercy.command_prefix}abc - abc xd**
    **{Mercy.command_prefix}ascii <text> - text ascii**
    **{Mercy.command_prefix}amongus - wtf amongus in discord?**
    **{Mercy.command_prefix}ddos <user> - fake ddos a user mentioned**
    **{Mercy.command_prefix}lenny - send lenny**
    **{Mercy.command_prefix}lmfao - lmfao animation text**
    **{Mercy.command_prefix}purge <amount> - purge chat**
    **{Mercy.command_prefix}shrug - shrug text**
    **{Mercy.command_prefix}table - table animation text**
    **{Mercy.command_prefix}tableflip - tableflip animation text**
    **{Mercy.command_prefix}unflip - unflip animation text**
    **{Mercy.command_prefix}virus - fake virus animation text**
    **{Mercy.command_prefix}boom - terrorist animation text**
    **{Mercy.command_prefix}horney - 7u7**
    ''')
    embed.set_thumbnail(url=(foto))
    embed.set_footer(text=(foother2),icon_url=(icon))
    await ctx.send(embed=embed, delete_after=15)

@Mercy.command()
async def raid(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title=f"{titlee}.", color=colour, description=f'''**{Mercy.command_prefix}massban - ban all user**
    **{Mercy.command_prefix}masskick - kick all user**
    **{Mercy.command_prefix}massrole - create 250 roles**
    **{Mercy.command_prefix}delchannels - delete all channels**
    **{Mercy.command_prefix}delroles - delete all roles**
    **{Mercy.command_prefix}spamchannels <name> - create 250 channels**
    **{Mercy.command_prefix}spam <amount> <text> - spam text**
    **{Mercy.command_prefix}tokenfuck <token> - fuck discord account**
    **{Mercy.command_prefix}tokeninfo <token> - show all token information.**
    **{Mercy.command_prefix}massunban - unban all user**
    **{Mercy.command_prefix}copy - clone server**
    ''')
    embed.set_thumbnail(url=(foto))
    embed.set_footer(text=(foother2),icon_url=(icon))
    await ctx.send(embed=embed, delete_after=15)

@Mercy.command()
async def misc(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title=f"{titlee}", color=colour, description=f'''**{Mercy.command_prefix}8ball <question> - 8ball magic??**
    **{Mercy.command_prefix}afk <reason> on - afk mode on**
    **{Mercy.command_prefix}afk <reason> off - afk mode off**
    **{Mercy.command_prefix}embed <text> - embed text**
    **{Mercy.command_prefix}geoip <ip> - geo-location ip**
    **{Mercy.command_prefix}nitro - generate random discord nitro link**
    **{Mercy.command_prefix}poll <question> - start a vote**
    **{Mercy.command_prefix}serverinfo - show all server information**
    **{Mercy.command_prefix}wizz <user> - user information**
    ''')
    embed.set_thumbnail(url=(foto))
    embed.set_footer(text=(foother2),icon_url=(icon))
    await ctx.send(embed=embed, delete_after=15)

@Mercy.command()
async def status(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title=f"{titlee}", color=colour, description=f'''**{Mercy.command_prefix}stream <text> - discord streaming status**
    **{Mercy.command_prefix}playing <text> - discord play status**
    **{Mercy.command_prefix}custom - custom animated status**
    **{Mercy.command_prefix}stopstatus - stop your status**
    ''')
    embed.set_thumbnail(url=(foto))
    embed.set_footer(text=(foother2),icon_url=(icon))
    await ctx.send(embed=embed, delete_after=15)

@Mercy.command()
async def selfbot(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title=f"{titlee}.", color=colour, description=f'''Selfbot commands ```100 Commands```
    **{Mercy.command_prefix}cls - clear console**
    **{Mercy.command_prefix}setprefix <prefix> - change your prefix**
    **{Mercy.command_prefix}restart - restart your selfbot**
    
    Thanks for using, have a nice day or night.
    ''')
    embed.set_thumbnail(url=(foto))
    embed.set_footer(text=(foother2),icon_url=(icon))
    await ctx.send(embed=embed, delete_after=15)
@Mercy.command()
async def changecolor(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title=f"{titlee}", color=colour,description=f'''**{Mercy.command_prefix}red - change console color
    {Mercy.command_prefix}yellow - change console color
    {Mercy.command_prefix}green - change console color
    {Mercy.command_prefix}blue - change console color
    {Mercy.command_prefix}cyan - change console color**
    ''')
    embed.set_thumbnail(url=(foto))
    embed.set_footer(text=(foother2),icon_url=(icon))
    await ctx.send(embed=embed, delete_after=15)

@Mercy.command()
async def red(ctx):
    await ctx.message.delete()
    Clear()
    print(f'''
\t\t\t\t               __  __                     
\t\t\t\t              |  \/  | ___ _ __ ___ _   _ 
\t\t\t\t              | |\/| |/ _ \ '__/ __| | | |
\t\t\t\t              | |  | |  __/ | | (__| |_| |
\t\t\t\t              |_|  |_|\___|_|  \___|\__, |
\t\t\t\t                     {Fore.WHITE}[ {Fore.LIGHTRED_EX}REMASTERED{Fore.WHITE} ] |___/ 

{Fore.LIGHTRED_EX} | {Fore.WHITE}[ {Fore.LIGHTRED_EX}Configuration{Fore.WHITE} ]{Fore.RESET}

{Fore.LIGHTRED_EX} |{Fore.WHITE} Your discord account ~ {Mercy.user.name}#{Fore.WHITE}{Mercy.user.discriminator}                         
{Fore.LIGHTRED_EX} |{Fore.WHITE} Your prefix ~ {Mercy.command_prefix}
{Fore.LIGHTRED_EX} |{Fore.WHITE} Server ~ {len(Mercy.guilds)}  

{Fore.LIGHTRED_EX} | {Fore.WHITE}[ {Fore.LIGHTRED_EX}Embed Configuration{Fore.WHITE} ]{Fore.RESET}

{Fore.LIGHTRED_EX} |{Fore.WHITE} Embed title ~ {titlee}
{Fore.LIGHTRED_EX} |{Fore.WHITE} Embed color ~ 0x{colour}
{Fore.LIGHTRED_EX} |{Fore.WHITE} Embed thumbnail ~ {foto}
{Fore.LIGHTRED_EX} |{Fore.WHITE} Embed footer ~ {foother2}''')

@Mercy.command()
async def yellow(ctx):
    await ctx.message.delete()
    Clear()
    print(f'''
\t\t\t\t               __  __                     
\t\t\t\t              |  \/  | ___ _ __ ___ _   _ 
\t\t\t\t              | |\/| |/ _ \ '__/ __| | | |
\t\t\t\t              | |  | |  __/ | | (__| |_| |
\t\t\t\t              |_|  |_|\___|_|  \___|\__, |
\t\t\t\t                     {Fore.WHITE}[ {Fore.LIGHTYELLOW_EX}REMASTERED{Fore.WHITE} ] |___/ 

{Fore.LIGHTYELLOW_EX} | {Fore.WHITE}[ {Fore.LIGHTYELLOW_EX}Configuration{Fore.WHITE} ]{Fore.RESET}

{Fore.LIGHTYELLOW_EX} |{Fore.WHITE} Your discord account ~ {Mercy.user.name}#{Fore.WHITE}{Mercy.user.discriminator}                         
{Fore.LIGHTYELLOW_EX} |{Fore.WHITE} Your prefix ~ {Mercy.command_prefix}
{Fore.LIGHTYELLOW_EX} |{Fore.WHITE} Server ~ {len(Mercy.guilds)}  

{Fore.LIGHTYELLOW_EX} | {Fore.WHITE}[ {Fore.LIGHTYELLOW_EX}Embed Configuration{Fore.WHITE} ]{Fore.RESET}

{Fore.LIGHTYELLOW_EX} |{Fore.WHITE} Embed title ~ {titlee}
{Fore.LIGHTYELLOW_EX} |{Fore.WHITE} Embed color ~ 0x{colour}
{Fore.LIGHTYELLOW_EX} |{Fore.WHITE} Embed thumbnail ~ {foto}
{Fore.LIGHTYELLOW_EX} |{Fore.WHITE} Embed footer ~ {foother2}''')

@Mercy.command()
async def green(ctx):
    await ctx.message.delete()
    Clear()
    print(f'''
\t\t\t\t               __  __                     
\t\t\t\t              |  \/  | ___ _ __ ___ _   _ 
\t\t\t\t              | |\/| |/ _ \ '__/ __| | | |
\t\t\t\t              | |  | |  __/ | | (__| |_| |
\t\t\t\t              |_|  |_|\___|_|  \___|\__, |
\t\t\t\t                     {Fore.WHITE}[ {Fore.LIGHTGREEN_EX}REMASTERED{Fore.WHITE} ] |___/ 

{Fore.LIGHTGREEN_EX} | {Fore.WHITE}[ {Fore.LIGHTGREEN_EX}Configuration{Fore.WHITE} ]{Fore.RESET}

{Fore.LIGHTGREEN_EX} |{Fore.WHITE} Your discord account ~ {Mercy.user.name}#{Fore.WHITE}{Mercy.user.discriminator}                         
{Fore.LIGHTGREEN_EX} |{Fore.WHITE} Your prefix ~ {Mercy.command_prefix}
{Fore.LIGHTGREEN_EX} |{Fore.WHITE} Server ~ {len(Mercy.guilds)}  

{Fore.LIGHTGREEN_EX} | {Fore.WHITE}[ {Fore.LIGHTGREEN_EX}Embed Configuration{Fore.WHITE} ]{Fore.RESET}

{Fore.LIGHTGREEN_EX} |{Fore.WHITE} Embed title ~ {titlee}
{Fore.LIGHTGREEN_EX} |{Fore.WHITE} Embed color ~ 0x{colour}
{Fore.LIGHTGREEN_EX} |{Fore.WHITE} Embed thumbnail ~ {foto}
{Fore.LIGHTGREEN_EX} |{Fore.WHITE} Embed footer ~ {foother2}''')

@Mercy.command()
async def blue(ctx):
    await ctx.message.delete()
    Clear()
    print(f'''
\t\t\t\t               __  __                     
\t\t\t\t              |  \/  | ___ _ __ ___ _   _ 
\t\t\t\t              | |\/| |/ _ \ '__/ __| | | |
\t\t\t\t              | |  | |  __/ | | (__| |_| |
\t\t\t\t              |_|  |_|\___|_|  \___|\__, |
\t\t\t\t                     {Fore.WHITE}[ {Fore.LIGHTBLUE_EX}REMASTERED{Fore.WHITE} ] |___/ 

{Fore.LIGHTBLUE_EX} | {Fore.WHITE}[ {Fore.LIGHTBLUE_EX}Configuration{Fore.WHITE} ]{Fore.RESET}

{Fore.LIGHTBLUE_EX} |{Fore.WHITE} Your discord account ~ {Mercy.user.name}#{Fore.WHITE}{Mercy.user.discriminator}                         
{Fore.LIGHTBLUE_EX} |{Fore.WHITE} Your prefix ~ {Mercy.command_prefix}
{Fore.LIGHTBLUE_EX} |{Fore.WHITE} Server ~ {len(Mercy.guilds)}  

{Fore.LIGHTBLUE_EX} | {Fore.WHITE}[ {Fore.LIGHTBLUE_EX}Embed Configuration{Fore.WHITE} ]{Fore.RESET}

{Fore.LIGHTBLUE_EX} |{Fore.WHITE} Embed title ~ {titlee}
{Fore.LIGHTBLUE_EX} |{Fore.WHITE} Embed color ~ 0x{colour}
{Fore.LIGHTBLUE_EX} |{Fore.WHITE} Embed thumbnail ~ {foto}
{Fore.LIGHTBLUE_EX} |{Fore.WHITE} Embed footer ~ {foother2}''')

@Mercy.command()
async def cyan(ctx):
    await ctx.message.delete()
    Clear()
    print(f'''
\t\t\t\t               __  __                     
\t\t\t\t              |  \/  | ___ _ __ ___ _   _ 
\t\t\t\t              | |\/| |/ _ \ '__/ __| | | |
\t\t\t\t              | |  | |  __/ | | (__| |_| |
\t\t\t\t              |_|  |_|\___|_|  \___|\__, |
\t\t\t\t                     {Fore.WHITE}[ {Fore.LIGHTCYAN_EX}REMASTERED{Fore.WHITE} ] |___/ 

{Fore.LIGHTCYAN_EX} | {Fore.WHITE}[ {Fore.LIGHTCYAN_EX}Configuration{Fore.WHITE} ]{Fore.RESET}

{Fore.LIGHTCYAN_EX} |{Fore.WHITE} Your discord account ~ {Mercy.user.name}#{Fore.WHITE}{Mercy.user.discriminator}                         
{Fore.LIGHTCYAN_EX} |{Fore.WHITE} Your prefix ~ {Mercy.command_prefix}
{Fore.LIGHTCYAN_EX} |{Fore.WHITE} Server ~ {len(Mercy.guilds)}  

{Fore.LIGHTCYAN_EX} | {Fore.WHITE}[ {Fore.LIGHTCYAN_EX}Embed Configuration{Fore.WHITE} ]{Fore.RESET}

{Fore.LIGHTCYAN_EX} |{Fore.WHITE} Embed title ~ {titlee}
{Fore.LIGHTCYAN_EX} |{Fore.WHITE} Embed color ~ 0x{colour}
{Fore.LIGHTCYAN_EX} |{Fore.WHITE} Embed thumbnail ~ {foto}
{Fore.LIGHTCYAN_EX} |{Fore.WHITE} Embed footer ~ {foother2}''')

@Mercy.command()
async def rainbow(ctx, *, content: str):
    title, description = content.split('|')
    await ctx.message.delete()
    cols = [0x32a852, 0x3296a8, 0xb700ff, 0x9232a8, 0xa8326f, 0xf25207, 0x3efa00, 0xfa0000]
    embed = discord.Embed(

        title = title,
        description= description,
        color = random.choice(cols)

    )
    embed.set_footer(text=f"Rainbow embed - Mercy{version}")
    msg = await ctx.send(embed=embed)

    for i in range(1000):
        embed2 = discord.Embed(

        title = title,
        description= description,
        color = random.choice(cols)

        )
        embed2.set_footer(text=f"Rainbow embed - Mercy{version}")
        await asyncio.sleep(0.1)
        await msg.edit(embed=embed2)

@Mercy.command()
async def wtfip(ctx, message):
        ip = message

        lookup = (
            "http://ip-api.com/json/"
            + ip
            + "?fields=status,message,country,countryCode,region,regionName,city,zip,lat,lon,timezone,isp,org,as,query,continent,continentCode"
        )
        with urllib.request.urlopen(lookup) as url:
            data = json.loads(url.read().decode())

        ### Store vars
        sts = data["status"]
        if sts == "fail":
            embed = discord.Embed(title="Error looking up " + ip, color=(colour))
            embed.set_thumbnail(
                url="https://iconsplace.com/wp-content/uploads/_icons/ff0000/256/png/error-icon-14-256.png"
            )
            embed.add_field(
                name="\nDouble check you've written the ip properly\n\nError:",
                value=data["message"],
            )
            await ctx.send(embed=embed)
        else:
            country = data["country"]
            region = data["regionName"]
            city = data["city"]
            zip = data["zip"]
            isp = data["isp"]
            c_code = data["continentCode"]
            c_cont = data["continent"]


            await ctx.send(f'''```ini
[ WTF IP ]

Country : {country}
Region : {region}
City : {city}
Continent Code : {c_code}
Continent : {c_cont}
Zip code : {zip}
Internet company : {isp}

[ MERCY REMASTERED ]
                ```''')

@Mercy.command()
async def encode(ctx, *, args):
    decoded_stuff = base64.b64encode("{}".format(args).encode("ascii"))
    encoded_stuff = str(decoded_stuff)
    encoded_stuff = encoded_stuff[2 : len(encoded_stuff) - 1]
    await ctx.message.delete()
    await ctx.send(content="{}".format(encoded_stuff))

@Mercy.command()
async def daily(ctx):
        await ctx.message.delete()
        await ctx.send("Getting BTC/ETH info...")
        # BTC info
        r = requests.get(
            "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR,GBP"
        )
        r = r.json()
        usd = r["USD"]
        eur = r["EUR"]
        gbp = r["GBP"]
        em = discord.Embed(
            color=colour,description=f"USD: `{str(usd)}$`\n\nEUR: `{str(eur)}€`\n\nGBP: `{str(gbp)}£`"
        )
        em.set_author(
            name="Bitcoin",
            icon_url="https://cdn.pixabay.com/photo/2013/12/08/12/12/bitcoin-225079_960_720.png",
        )
        await ctx.send(embed=em)

        # ETH info
        r = requests.get(
            "https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD,EUR,GBP"
        )
        r = r.json()
        usd = r["USD"]
        eur = r["EUR"]
        gbp = r["GBP"]
        em = discord.Embed(
            color=colour,description=f"USD: `{str(usd)}$`\nEUR: `{str(eur)}€`\n\nGBP: `{str(gbp)}£`"
        )
        em.set_author(
            name="Ethereum",
            icon_url="https://cdn.discordapp.com/attachments/271256875205525504/374282740218200064/2000px-Ethereum_logo.png",
        )
        await ctx.send(embed=em)

# Community plugins.

@Mercy.command()
async def themes(ctx):
    await ctx.message.delete()
    embed = discord.Embed(

        title =f"{titlee} ~ Themes",
        color = colour,
        description = f'''**{Mercy.command_prefix}pop -> pop cat theme
        {Mercy.command_prefix}dc -> discord clasic theme
        {Mercy.command_prefix}github -> github dark theme
        {Mercy.command_prefix}catdance -> dance???**
        '''
        )
    embed.set_footer(text=(foother2),icon_url=(icon))
    await ctx.send(embed=embed)


@Mercy.command()
async def pop(ctx):
    await ctx.message.delete()
    pop_em = discord.Embed(title = "POP Theme", color = colour, description = "Installing POP Theme.")
    await ctx.send(embed=pop_em)
    pop = {}
    with open("Config/Theme/Themes.json", "w") as f:
        json.dump(pop, f)
    pop_load = {
        "title": "POP",
        "embedcolor": "0x46008C",
        "thumbnail": "https://c.tenor.com/NkAegm0IP8IAAAAC/popcat.gif"
    }
    with open("Config/Theme/Themes.json", "w") as f:
        json.dump(pop_load, f)
    sleep(3)
    embed = discord.Embed(title = "Mercy", color=colour, description="Restarting")
    embed.set_thumbnail(url="https://media.giphy.com/media/3oEjI6SIIHBdRxXI40/200.gif")
    embed.set_footer(text=(foother2),icon_url=(icon))
    await ctx.send(embed=embed)
    restart_program()

@Mercy.command()
async def dc(ctx):
    await ctx.message.delete()
    dc = discord.Embed(title = "Discord Theme", color =colour, description = "Installing Discord Theme.")
    await ctx.send(embed=dc)
    dc = {}
    with open("Config/Theme/Themes.json", "w") as f:
        json.dump(dc, f)
    dc_load = {
        "title": "Discord",
        "embedcolor": "0x7289da",
        "thumbnail": "https://es.logodownload.org/wp-content/uploads/2021/05/discord-logo-7-11-300x300.png"
    }
    with open("Config/Theme/Themes.json", "w") as f:
        json.dump(dc_load, f)
    sleep(3)
    embed = discord.Embed(title = "Mercy", color=colour, description="Restarting")
    embed.set_thumbnail(url="https://media.giphy.com/media/3oEjI6SIIHBdRxXI40/200.gif")
    embed.set_footer(text=(foother2),icon_url=(icon))
    await ctx.send(embed=embed)
    restart_program()

@Mercy.command()
async def github(ctx):
    await ctx.message.delete()
    dc = discord.Embed(title = "GitHub Theme", color =colour, description = "Installing GitHub Theme.")
    await ctx.send(embed=dc)
    dc = {}
    with open("Config/Theme/Themes.json", "w") as f:
        json.dump(dc, f)
    dc_load = {
        "title": "GitHub",
        "embedcolor": "0x242424",
        "thumbnail": "https://i.imgur.com/pvVEJPY.png"
    }
    with open("Config/Theme/Themes.json", "w") as f:
        json.dump(dc_load, f)
    sleep(3)
    embed = discord.Embed(title = "Mercy", color=colour, description="Restarting")
    embed.set_thumbnail(url="https://media.giphy.com/media/3oEjI6SIIHBdRxXI40/200.gif")
    embed.set_footer(text=(foother2),icon_url=(icon))
    await ctx.send(embed=embed)
    restart_program()

@Mercy.command()
async def catdance(ctx):
    await ctx.message.delete()
    dc = discord.Embed(title = "Catdance Theme", color =colour, description = "Installing Catdance Theme.")
    await ctx.send(embed=dc)
    dc = {}
    with open("Config/Theme/Themes.json", "w") as f:
        json.dump(dc, f)
    dc_load = {
        "title": "Mercy",
        "embedcolor": "0xCF056A",
        "thumbnail": "https://i.imgur.com/pgf27NS.gif"
    }
    with open("Config/Theme/Themes.json", "w") as f:
        json.dump(dc_load, f)
    sleep(3)
    embed = discord.Embed(title = "Mercy", color=colour, description="Restarting")
    embed.set_thumbnail(url="https://media.giphy.com/media/3oEjI6SIIHBdRxXI40/200.gif")
    embed.set_footer(text=(foother2),icon_url=(icon))
    await ctx.send(embed=embed)
    restart_program()

@Mercy.command()
async def default(ctx):
    await ctx.message.delete()
    df = discord.Embed(title = "Default Theme", color =colour, description = "Installing Default Theme.")
    await ctx.send(embed=df)
    df = {}
    with open("Config/Theme/Themes.json", "w") as f:
        json.dump(df, f)
    df_load = {
        "title": "Mercy~",
        "embedcolor": "0x7400FF",
        "thumbnail": "https://i.imgur.com/FeHYsXQ.png"
    }
    with open("Config/Theme/Themes.json", "w") as f:
        json.dump(df_load, f)
    sleep(3)
    embed = discord.Embed(title = "Mercy", color=colour, description="Restarting")
    embed.set_thumbnail(url="https://media.giphy.com/media/3oEjI6SIIHBdRxXI40/200.gif")
    embed.set_footer(text=(foother2),icon_url=(icon))
    await ctx.send(embed=embed)
    restart_program()

@Mercy.command()
async def new(ctx):
    await ctx.message.delete()
    embed = discord.Embed(
        title = titlee,
        color = colour,
        description = f'''Hey!, Thanks for using Mercy.

        **{Mercy.command_prefix}daily -> Show btc price and eth
        {Mercy.command_prefix}wtfip <ip> -> IP lookup
        {Mercy.command_prefix}rainbow <title> | <message> -> rainbow embed use the "|" as separator, example > hello | world
        {Mercy.command_prefix}themes -> Show all mercy themes
        {Mercy.command_prefix}gay_percentage -> gay?
        **
        '''
    )
    embed.set_footer(text=(foother2),icon_url=(icon))
    await ctx.send(embed=embed)

@Mercy.command()
async def gay_percentage(ctx, user: discord.User):
    await ctx.message.delete()
    percentage_numbers = ["0%", "1%", "5%", "10%", "15%", "20%", "25%", "30%", "35%", "40%", "45%", "50%", "55%", "60%", "65%", "70%", "75%", "80%", "85%", "90%", "95%", "100%", "∞"]
    percentage = random.choice(percentage_numbers)
    embed = discord.Embed(
        title = f"{titlee} ~ How gay are you or are you?",
        color = colour,
        description = f"{user.name} is {percentage} gay :rainbow_flag:"
        )
    embed.set_footer(text=(foother2),icon_url=(icon))
    await ctx.send(embed=embed)

if __name__ == '__main__':
    Init()