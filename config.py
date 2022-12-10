import discord
from discord.ext import commands
from youtube_dl import YoutubeDL
from Logger import Logger


class Settings:
    token = 'MTA0NTY5MDkxMTM3MzQwNjMzOQ.GhrVmB.tF11qXomyaZn-pcbJOOXOwPz2itzKDIDboeS_Q'
    bot = 'Botyra'
    id = 1045690911373406339
    prefix = '>'


intents = discord.Intents.default()
intents.message_content = True

YDL_OPTIONS = {'format': 'worstaudio/best', 'noplaylist': 'False', 'simulate': 'True',
               'preferredquality': '192', 'preferredcodec': 'mp3', 'key': 'FFmpegExtractAudio'}


FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
