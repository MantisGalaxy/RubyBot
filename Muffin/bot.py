import discord
from discord.ext import commands
import os
import datetime
import aiohttp
import random

client = commands.Bot(command_prefix = "$")
global_color = 0xf55151
client.remove_command("help")

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have enough permissions to do that!")

    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please, inform all the parameters!')

    if isinstance(error, commands.BotMissingPermissions):
        await ctx.send("I don't have enough permissions to do that")

    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Command Not Found!")

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Me Getting Developed!"))
    print(f"{client.user} is ready!")

@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! `{round(client.latency * 1000)}ms.`")

start_time = datetime.datetime.utcnow()
@client.command()
async def uptime(ctx: commands.Context):
    now = datetime.datetime.utcnow() # Timestamp of when uptime function is run
    delta = now - start_time
    hours, remainder = divmod(int(delta.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)
    if days:
        time_format = "**{d}** days, **{h}** hours, **{m}** minutes, and **{s}** seconds."
    else:
        time_format = "**{h}** hours, **{m}** minutes, and **{s}** seconds."
    uptime_stamp = time_format.format(d=days, h=hours, m=minutes, s=seconds)

    await ctx.send(f"I've been online for {uptime_stamp}")

@client.command()
async def load(ctx, extension):
    if not ctx.message.author.id == 331451561387753472:
        return await ctx.send("You cannot do this command!", delete_after=3)
    ''' Loads a Cog '''
    client.load_extension(f"cogs.{extension}")
    await ctx.send(f"cogs.{extension} has been loaded!")

@client.command()
async def unload(ctx, extension):
    if not ctx.message.author.id == 331451561387753472:
        return await ctx.send("You cannot do this command!", delete_after=3)
    ''' Unloads A Cog '''
    client.unload_extension(f"cogs.{extension}")
    await ctx.send(f"cogs.{extension} has been unloaded!")

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")


client.run("NzA3NTkwNTY1NDUzMjM0Mjc2.XrLBNA.OVlRtOEr_CRNKdv6fcbqJ-0-r7Q")

