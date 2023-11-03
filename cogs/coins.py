import nextcord, sqlite3, cfg
from nextcord.ext import commands
from nextcord import Interaction


class Coin(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        db = sqlite3.connect("database.db")
        sql = db.cursor() 

        sql.execute("""CREATE TABLE IF NOT EXISTS coins (
            id BIGINT PRIMARY KEY,
            coins INTEGER
        )""")
        db.commit()

        for guild in self.client.guilds:
            for member in guild.members:
                if member.bot:
                    pass
                else:
                    sql.execute("SELECT * FROM coins WHERE id=?", (member.id,))
                    result = sql.fetchone()
                    if result is None:
                        sql.execute("INSERT INTO coins VALUES (?,?)", (member.id, 0))
                        print(member.name + " added to db")
        db.commit()

    # @nextcord.slash_command(name="give_coins")
    # async def give_coins(self, interaction: Interaction):
    #     if interaction.user.id == cfg.owner_id:
    #         await interaction.response.send_message("Successfully", ephemeral=True)
    #     else:
    #         await interaction.response.send_message("You dont't have permisions to use it", ephemeral=True)

        

def setup(client):
    client.add_cog(Coin(client))