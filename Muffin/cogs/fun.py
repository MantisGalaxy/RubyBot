import discord
from discord.ext import commands
import os
import datetime
import aiohttp
import random

class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Fun Cog Has Been Loaded")


def setup(client):
    client.add_cog(Fun(client))