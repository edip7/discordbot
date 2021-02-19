import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('.help \n Made by Vybez.'))
    print('Bot is ready. ')

@client.command()
async def bothelp(ctx):
    await ctx.send('To use the bot: Enter a . and a feeling word next to it to get a lenny face emoticon. Enjoy the bot!')

@client.command()
async def gm(ctx):
    await ctx.send('Does gm stands for good morning or get money?')


@client.command()
async def happy(ctx):
    await ctx.send('( ͡ᵔ ͜ʖ ͡ᵔ )')

@client.command()
async def wink(ctx):
    await ctx.send('( ͡~ ͜ʖ ͡°)')

@client.command()
async def excuseme(ctx):
    await ctx.send('( ͡◉◞ ͜ʖ◟ ͡◉)')

@client.command()
async def chillin(ctx):
    await ctx.send('(⌐■ ͜ʖ■)')

@client.command()
async def flex(ctx):
    await ctx.send('ᕦ( ͡° ͜ʖ ͡°)ᕤ')

@client.command()
async def WTF(ctx):
    await ctx.send('ლ(ಠ益ಠლ)')

@client.command()
async def idk(ctx):
    await ctx.send('¯\_(ツ)_/¯')

@client.command()
async def excited(ctx):
    await ctx.send('⍲‿⍲')

@client.command()
async def fight(ctx):
    await ctx.send('(ง''́)ง')

@client.command()
async def rich(ctx):
    await ctx.send('[̲̅$̲̅(̲̅ ͡° ͜ʖ ͡°̲̅)̲̅$̲̅]')

@client.command()
async def bro(ctx):
    await ctx.send('( ̿ ̿ ̿ ̿ ̿ ̿ ̿ ̿°̿ ̿ ̿ ̿ ̿ ͜ʖ ̿ ̿ ̿ ̿ ̿ ̿ ̿°̿ ̿ ̿ ̿ ̿ ̿ ̿ )')

@client.command()
async def doge(ctx):
    await ctx.send('( ͡° ᴥ ͡°)')

@client.command()
async def annoyed(ctx):
    await ctx.send('(#｀へ´#)')

@client.command()
async def sad(ctx):
    await ctx.send('༼⍨༽')

@client.command()
async def bruh(ctx):
    await ctx.send('( ‾ʖ̫‾)')

@client.command()
async def fyou(ctx):
    await ctx.send('( ͡° ͜つ ͡°)╭∩╮')

@client.command()
async def die(ctx):
    await ctx.send('̿̿ ̿̿ ̿̿ ̿''=( ͠° ͟ʖ ͡°)=ε/̵͇̿̿/ ̿ ̿ ̿ ̿ ̿  ')

@client.command()
async def blush(ctx):
    await ctx.send('(* ͡° ͜ʖ ͡°*)')

@client.command()
async def confused(ctx):
    await ctx.send('( ͡° ◇ ͡°)?')

@client.command()
async def yowhat(ctx):
    await ctx.send('(◉͜ʖ◉)')

@client.command()
async def dissaprove(ctx):
    await ctx.send('ヽ( ͡ಠ ʖ̯ ͡ಠ)ﾉ')

@client.command()
async def ragequit(ctx):
    await ctx.send('(╯ຈل͜ຈ) ╯︵ ┻━┻')

@client.command()
async def spooky(ctx):
    await ctx.send('/╲/\╭( ͡° ͡° ͜ʖ ͡° ͡°)╮/\╱')

@client.command()
async def love(ctx):
    await ctx.send('( ͡° ♥ ͡°)')

@client.command()
async def hide(ctx):
    await ctx.send('( ͡° ͜ʖ├┬┴┬)')

@client.command()
async def hug(ctx):
    await ctx.send('(つ ♡ ͜ʖ ♡)つ')

@client.command()
async def kiss(ctx):
    await ctx.send('( ͡°Ɛ ͡°)')

@client.command()
async def run(ctx):
    await ctx.send('┌(° ͜ʖ͡°)┘')

@client.command()
async def weird(ctx):
    await ctx.send('( ͡ ͡° ͡° ʖ ͡° ͡°)')






client.run('[DISCORD BOT KEY]')
