import discord
from discord.ext import commands
import os
import datetime
import aiohttp
import random

class Economy(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Economy Cog Has Been Loaded")


def setup(client):
    client.add_cog(Economy(client))