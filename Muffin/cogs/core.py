import discord
from discord.ext import commands
import os
import datetime
import aiohttp
import random

class Core(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Core Cog Has Been Loaded")

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(
        title="Ruby's Commands",
        colour=discord.Colour(0xf55151),
        description="Greetings! I'm Ruby. A multi-purpose discord bot that sorts out all of your needs from Moderation to Fun, Music, Misc, etc.\nMy prefix is `$`"
        )
        embed.set_author(
        name="Ruby",
        icon_url="https://images-ext-2.discordapp.net/external/CS2gA44mvHUs7yB3DCyaNufJjDoMwNXooARImWeZHsM/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/707590565453234276/0f5f288203c25adfb09fab5439d1aa9a.webp?width=406&height=406"
        )
        embed.add_field(
        name="Core",
        value="`ping | help |` ",
        inline=False
        )
        embed.add_field(
        name="Fun",
        value="`8ball | joke` ",
        inline=False
        )
        embed.add_field(
        name="Economy",
        value="*Coming Soon*",
        inline=False
        )
        embed.add_field(
        name="Images",
        value="`meme | cat | dog | avatar |` ",
        inline=False
        )
        embed.add_field(
        name="Moderation",
        value="`ban <@user> reason | kick <@user> <reason> | mute <@user> <reason> | unmute <@user> | addrole <@user> <role> | removerole <@user> <role> | lockdown #channel | unlock #channel`",
        inline=False
        )
        embed.add_field(
        name="Info",
        value="`avatar | info | serverinfo | userinfo`",
        inline=False
        )
        embed.add_field(
        name="Text",
        value="`embed | say | ascii`",
        inline=False
        )
        embed.add_field(
        name="Support",
        value="`contact | support`",
        inline=False
        )
        embed.set_footer(
            text="Ruby",
            icon_url="https://images-ext-2.discordapp.net/external/CS2gA44mvHUs7yB3DCyaNufJjDoMwNXooARImWeZHsM/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/707590565453234276/0f5f288203c25adfb09fab5439d1aa9a.webp?width=406&height=406"
        )
        await ctx.send(
        content="These are my commands",
        embed=embed
    )


def setup(client):
    client.add_cog(Core(client))
