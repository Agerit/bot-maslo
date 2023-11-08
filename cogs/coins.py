import nextcord, sqlite3, cfg
from nextcord.ext import commands
from nextcord import Interaction


class Coin(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_ready(self):
        try:
            with sqlite3.connect("database.db") as db:
                sql = db.cursor() 

                sql.execute("""CREATE TABLE IF NOT EXISTS coins (
                    id BIGINT PRIMARY KEY,
                    coins INTEGER
                )""")
                db.commit()

                for guild in self.client.guilds:
                    for member in guild.members:
                        if member.bot == False:
                            sql.execute("SELECT * FROM coins WHERE id=?", (member.id,))
                            result = sql.fetchone()
                            if result is None:
                                sql.execute("INSERT INTO coins VALUES (?,?)", (member.id, 0))
                                print(member.name + " added to db")
                db.commit()
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")




    @nextcord.slash_command(name="give_coins", guild_ids=[cfg.guild_id])
    async def give_coins(self, interaction: Interaction, user: nextcord.User, coins: int):
        if interaction.user.id == cfg.owner_id:
            try:
                with sqlite3.connect('database.db') as db:
                    sql = db.cursor()

                    # Отримуємо поточний баланс користувача
                    sql.execute("SELECT coins FROM coins WHERE id=?", (user.id,))
                    result = sql.fetchone()
                    if result is None:
                        current_coins = 0
                    else:
                        current_coins = result[0]

                    # Додаємо нові монети до поточного балансу
                    new_coins = current_coins + coins

                    # Оновлюємо баланс користувача в базі даних
                    sql.execute("UPDATE coins SET coins = ? WHERE id = ?", (new_coins, user.id))
                    db.commit()

                    await interaction.response.send_message(f"Successfully gave {coins} coins to {user.name}. They now have {new_coins} coins.", ephemeral=True)
            except sqlite3.Error as e:
                print(f"An error occurred: {e}")
        else:
            await interaction.response.send_message("You don't have permissions to use it", ephemeral=True)




        @nextcord.slash_command(name="take_coins", guild_ids=[cfg.guild_id])
        async def take_coins(self, interaction: Interaction, user: nextcord.User, coins: int):
            if interaction.user.id == cfg.owner_id:
                try:
                    with sqlite3.connect('database.db') as db:
                        sql = db.cursor()

                        # Отримуємо поточний баланс користувача
                        sql.execute("SELECT coins FROM coins WHERE id=?", (user.id,))
                        result = sql.fetchone()
                        if result is None:
                            current_coins = 0
                        else:
                            current_coins = result[0]

                        # Віднімаємо монети від поточного балансу
                        new_coins = current_coins - coins

                        # Оновлюємо баланс користувача в базі даних
                        sql.execute("UPDATE coins SET coins = ? WHERE id = ?", (new_coins, user.id))
                        db.commit()

                        await interaction.response.send_message(f"Successfully took {coins} coins from {user.name}. They now have {new_coins} coins.", ephemeral=True)
                except sqlite3.Error as e:
                    print(f"An error occurred: {e}")
            else:
                await interaction.response.send_message("You don't have permissions to use it", ephemeral=True)


        @nextcord.slash_command(name="set_coins", guild_ids=[cfg.guild_id])
        async def set_coins(self, interaction: Interaction, user: nextcord.User, coins: int):
            if interaction.user.id == cfg.owner_id:
                try:
                    with sqlite3.connect('database.db') as db:
                        sql = db.cursor()

                        # Встановлюємо баланс користувача на вказане число монет
                        sql.execute("UPDATE coins SET coins = ? WHERE id = ?", (coins, user.id))
                        db.commit()

                        await interaction.response.send_message(f"Successfully set {user.name}'s coins to {coins}.", ephemeral=True)
                except sqlite3.Error as e:
                    print(f"An error occurred: {e}")
            else:
                await interaction.response.send_message("You don't have permissions to use it", ephemeral=True)


        @nextcord.slash_command(name="check_coins", guild_ids=[cfg.guild_id])
        async def check_coins(self, interaction: Interaction):
            try:
                with sqlite3.connect("database.db") as db:
                    sql = db.cursor()

                    sql.execute("SELECT coins FROM coins WHERE id=?", (interaction.user.id))
                    result = sql.fetchone()
                    if result is None:
                        current_coins = 0
                    else:
                        current_coins = result[0]

                    interaction.response.send_message(f"You have {current_coins} coins ")
            except sqlite3.Error as e:
                print(f"An error occurred: {e}")
                await interaction.response.send_message("An error occurred. Try another time.")



        

def setup(client):
    client.add_cog(Coin(client))