from config import *

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=Settings.prefix, intents=intents)

vc = ''


@bot.command()
async def discon(ctx):
    await vc.disconnect()


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
    global vc
    if not(type(vc) == discord.VoiceClient):
        await connect(ctx)
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
    global vc
    vc = await ctx.message.author.voice.channel.connect()


@bot.event
async def on_ready():
    print('We have been logged in as {0.user}'.format(bot))

logger = Logger()

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    logger.log(message)
    print(message.content)

bot.run(Settings.token)

