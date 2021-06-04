import discord, asyncio
from discord.ext import commands
from random import randint, choice
from datetime import datetime
from secret import token

bot = commands.Bot(command_prefix="r!", case_insensitive=True)
bot.remove_command("help")

def noValidNum():
    return "❌ That is not a valid number"
def onlyNum(var):
    var.lower()
    if var.islower():
        return False
    return True

@bot.event
async def on_ready():
    print(f"\nBot is online\nCurrent ping: {int(round(bot.latency,3) * 1000)}ms")
    await bot.change_presence(activity=discord.Game(name="r!help | Still in Beta 0.5"))

"""          NOTE: This remove commandnotfound function can't log error messages          """
# @bot.event
# async def on_command_error(ctx, error):
    # if isinstance(error, commands.CommandNotFound):
    #     pass

@bot.command(name="help", aliases=["h", "?"])
async def help(ctx, message=None):
    embed = discord.Embed(title="Rens Commands", color=0x0172ff)
    embed.set_author(name="Rens Help")
    embed.set_thumbnail(url="https://i.ibb.co/nD793MT/rens-logo.jpg")
    embed.add_field(name="r!help", value="Shows this message", inline=True)
    embed.add_field(name="r!random / r!r", value="Sends a random number", inline=True)
    embed.add_field(name="r!m8ball / r!m8", value="Got a question?\nAsk the magic 8 ball!", inline=True)
    embed.add_field(name="r!ping", value="Shows the bot latency", inline=True)
    embed.set_footer(text="‎\nBot made by: rens#4472\nVersion: Beta 0.5")
    user = bot.get_user(ctx.message.author.id)
    await ctx.author.send(embed=embed)
    await ctx.message.add_reaction("📩")
    print(f"{datetime.today().strftime('%Y-%m-%d %H:%M:%S')}> {ctx.message.author.id} ({ctx.message.author.name}) called the \"help\" command")
    await asyncio.sleep(5)
    await ctx.message.delete()
@bot.command()
@commands.guild_only()
async def ping(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title="**Ping**", description=f"🏓 Pong! `{int(round(bot.latency,3) * 1000)}ms`", color=0xff0000)
    await ctx.send(embed=embed)
    print(f"{datetime.today().strftime('%Y-%m-%d %H:%M:%S')}> {ctx.message.author.id} ({ctx.message.author.name}) called the \"ping\" command")
@bot.command(name="m8ball", aliases=["m8", "8ball", "8b"])
async def m8ball(ctx, *, message=None):
    await ctx.message.delete()
    answers = [
        "Try again later.",
        "Maybe...",
        "Ask another question.",
        "Definitely yes!",
        "Definitely no!",
        "Yes!",
        "No."
    ]
    embed = discord.Embed(description=f"What's <@{ctx.message.author.id}> question today?", color=0x9900ff)
    embed.set_author(name="Magic 8 Ball", icon_url="https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/8-Ball_Pool.svg/1024px-8-Ball_Pool.svg.png")
    embed.add_field(name="Question", value=f"{message}", inline=True)
    embed.add_field(name="Answer", value=f"{choice(answers)}", inline=True)
    await ctx.send(embed=embed)@bot.command()
    print(f"{datetime.today().strftime('%Y-%m-%d %H:%M:%S')}> {ctx.message.author.id} ({ctx.message.author.name}) called the \"m8ball\" command")
@bot.command(name="random", aliases=["r"])
async def random(ctx, minnum=None, maxnum=None):
    await ctx.message.delete()
    if minnum and maxnum:
        if onlyNum(minnum) and onlyNum(maxnum):
            if int(maxnum) > int(minnum) and int(minnum) > 0 and int(maxnum) > 0 and int(maxnum) <= 999999999999999:
                embed = discord.Embed(title="❓ Random Number", description=f"Random Number: **{randint(int(minnum), int(maxnum))}**\n`{minnum} to {maxnum}`", color=0x00ffaa)
                await ctx.send(embed=embed)
            else:
                await ctx.send(noValidNum(), delete_after=1)
        else:
            await ctx.send(noValidNum(), delete_after=1)
    else:
        if minnum and maxnum==None:
            if onlyNum(minnum):
                if int(minnum) > 0 and int(minnum) < 999999999999999:
                    embed = discord.Embed(title="❓ Random Number", description=f"Random Number: **{randint(1, int(minnum))}**\n`1 to {minnum}`", color=0x00ffaa)
                    await ctx.send(embed=embed)
                else:
                    await ctx.send(noValidNum(), delete_after=1)
            else:
                await ctx.send(noValidNum(), delete_after=1)
        else:
            embed = discord.Embed(title="❓ Random Number", description=f"Random Number: **{randint(1, 10)}**\n`1 to 10`", color=0x00ffaa)
            embed.set_footer(text="Hint: You can add min and max value (  !random 1 50  )")
            await ctx.send(embed=embed)
    print(f"{datetime.today().strftime('%Y-%m-%d %H:%M:%S')}> {ctx.message.author.id} ({ctx.message.author.name}) called the \"random\" command")

bot.run(token)