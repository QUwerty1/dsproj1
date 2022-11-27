import discord
from config import Settings
from discord.ext import commands
from youtube_dl import YoutubeDL

intents = discord.Intents.default()
intents.message_content = True


YDL_OPTIONS = {'format': 'worstaudio/best', 'noplaylist': 'False', 'simulate': 'True',
               'preferredquality': '192', 'preferredcodec': 'mp3', 'key': 'FFmpegExtractAudio'}
FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

bot = commands.Bot(command_prefix=Settings.prefix, intents=intents)

vc = ''

@bot.command()
async def ping(ctx):
    await ctx.send('pong')



@bot.command()
async def resume(ctx):
    vc.resume()


@bot.command()
async def pause(ctx):
    vc.pause()


@bot.command()
async def music(ctx, *, arg):
    if not('vc' in locals()):
        global vc
        vc = await connect(ctx)
    print(locals())
    if 'pause' in arg:
        vc.pause()
    else:
        with YoutubeDL(YDL_OPTIONS) as ydl:
            if 'https://' in arg:
                info = ydl.extract_info(arg, download=False)
            else:
                info = ydl.extract_info(f"ytsearch:{arg}", download=False)['entries'][0]

        url = info['formats'][0]['url']
        vc.play(discord.FFmpegPCMAudio(executable="ffmpeg\\ffmpeg.exe", source=url, **FFMPEG_OPTIONS))


@bot.command()
async def connect(ctx):
    vc = await ctx.message.author.voice.channel.connect()
    return vc


# @bot.event
# async def on_ready():
#     print('We have been logged in as {0.user}'.format(bot))
#
#
# @bot.event
# async def on_message(message):
#     with open('logs/' + message.channel.name + '.txt', mode='a') as f:
#         f.write(f'{message.author.name}: {message.content} \n')
#     print(f'{message.author.name}: {message.content}')
#     if message.author == bot.user:
#         return
#     if message.content.startswith('Botyra'):
#         await message.channel.send(f'Hi! {message.author.mention}')

bot.run(Settings.token)

