import nextcord, sqlite3, cfg, asyncio, os
from nextcord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")
intents = nextcord.Intents.all()
client = commands.Bot(intents=intents, command_prefix="!")



@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
    

async def loadAll():
    for fn in os.listdir("./cogs"):
        if fn.endswith(".py"):
            client.load_extension(f"cogs.{fn[:-3]}")
            print(f"{fn[:-3]} extension loaded")

@client.command()
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")
    await ctx.send(f"Loaded {extension} successfully")

@client.command()
async def unload(ctx, extension):
    client.unload_extensionload_extension(f"cogs.{extension}")
    await ctx.send(f"Unloaded {extension} successfully")

@client.command()
async def reload(ctx, extension):
    client.reload_extension(f"cogs.{extension}")
    await ctx.send(f"Reloaded [{extension}] successfully")


async def main():
    await loadAll()
    await client.start(TOKEN)

asyncio.run(main())