import nextcord, sqlite3, cfg, asyncio, os
from nextcord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")
intents = nextcord.Intents.all()
client = commands.Bot(intents=intents, command_prefix="m!")



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
    if ctx.author.id == cfg.owner_id:
        client.load_extension(f"cogs.{extension}")
        print((f"Loaded [{extension}] successfully"))
    else:
        print(f'someone tried to unload {extension}')

@client.command()
async def unload(ctx, extension):
    if ctx.author.id == cfg.owner_id:
        client.unload_extensionload_extension(f"cogs.{extension}")
        print((f"Unloaded [{extension}] successfully"))
    else:
        print(f'someone tried to unload {extension}')

@client.command()
async def reload(ctx, extension):
    if ctx.author.id == cfg.owner_id:
        client.reload_extension(f"cogs.{extension}")
        print((f"Reloaded [{extension}] successfully"))
    else:
        print(f'someone tried to reload {extension}')


async def main():
    await loadAll()
    await client.start(TOKEN)

asyncio.run(main())