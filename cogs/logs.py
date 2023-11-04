import nextcord, cfg
from nextcord.ext import commands
from nextcord.utils import get
from datetime import datetime


class Logs(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member):
        embed = nextcord.Embed(title="Участник присоединился",description=f"{member.name} зашел на сервер", timestamp=datetime.utcnow(), color=nextcord.Color.green())
        embed.set_thumbnail(url=member.avatar.url)
        await member.guild.system_channel.send(embed=embed)


def setup(client):
    client.add_cog(Logs(client))