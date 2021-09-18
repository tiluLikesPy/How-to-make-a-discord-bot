import discord #importing discord
from discord.ext import commands #importing a spezial funktion from discord.py

bot = commands.Bot(commands_prefix="!") #There, where the ! is, you can set you prefix in, like ?, $, %, ...

@bot.event                                    #this is a event
async def on_ready():                         #this start the logging
  print(f"Hey, I'm ready as {bot.user.name}") #this log, that the bot is online
  

  
@bot.command() #the event for the command
async def embed(ctx): #Where embed is, you can change it to your command
  embed = discord.Embed(description="here you can set the description of the embed"
