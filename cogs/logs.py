import nextcord, cfg
from nextcord.ext import commands
from nextcord.utils import get


class Logs(commands.Cog):
    def __init__(self, client):
        self.client = client

        


def setup(client):
    client.add_cog(Logs(client))