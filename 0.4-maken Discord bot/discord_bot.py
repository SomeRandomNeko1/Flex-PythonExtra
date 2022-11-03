from email.mime import image
from http import client
import discord
from discord.ext.commands import Bot
from discord import Intents
from random import choice
import requests

client = Bot(
    command_prefix="+",
    intents= Intents.all()
)

@client.command()
async def ping(ctx):
    await ctx.send("pong!")

@client.command()
async def memes(ctx):
    req= requests.get("https://meme-api.herokuapp.com/gimme")
    data= req.json()

    embed = discord.Embed()
    embed.set_image(url=data["url"])

    await ctx.send(embed=embed) 



client.run("....")

