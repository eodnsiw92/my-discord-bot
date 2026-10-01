import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot is ready: {bot.user}')
    
    channel_id = 1554578576932610219
    channel = bot.get_channel(channel_id)
    if channel:
        await channel.send('محمد بضان')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

bot.run('MTU1NTE3MTMyMzMzMzMzMzM5NQ.GDJ8yc.lZj5j-vL-aJ8SdRIJloMoni2-cT75-Rv3cmCRQ')
