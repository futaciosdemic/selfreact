import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True
intents.reactions = True

client = commands.Bot(command_prefix='!', intents=intents) # this is the prefix u can change it whenever u want(u can also change the client)

self_react_enabled = False

@client.command()
async def selfreact(ctx, emoji):
    global self_react_enabled
    self_react_enabled = True
    await ctx.send(f"# Your selfreact started with the emoji: {emoji}")
    await ctx.message.delete()

@client.command()
async def stop_selfreact(ctx):
    global self_react_enabled
    self_react_enabled = False
    await ctx.send("# Selfreact stopped")
    await ctx.message.delete()

@client.event
async def on_message(message):
    global self_react_enabled
    if self_react_enabled and message.author == client.user:
        await message.add_reaction(emoji)
    await client.process_commands(message)

# exemple
# !selfreact 😂
# Your selfreact started with the emoji: 😂
