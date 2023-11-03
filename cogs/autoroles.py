import nextcord, cfg
from nextcord.ext import commands
from nextcord.utils import get


class AutoRoles(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member):
        for role_id in cfg.start_roles_id:
            role = get(member.guild.roles, id=role_id)
            await member.add_roles(role)
        


def setup(client):
    client.add_cog(AutoRoles(client))