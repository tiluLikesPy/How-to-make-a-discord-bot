import discord #importing discord
from discord.ext import commands #importing a spezial funktion from discord.py

bot = commands.Bot(commands_prefix="!") #There, where the ! is, you can set you prefix in, like ?, $, %, ...

@bot.event                                    #this is a event
async def on_ready():                         #this start the logging
  print(f"Hey, I'm ready as {bot.user.name}") #this log, that the bot is online
  

  
@bot.command() #the event for the command
async def embed(ctx): #Where embed is, you can change it to your command
  embed = discord.Embed(title=""here your title",
                        description="here you can set the description of the embed",
                        color=0x000000) #where the 000000 is, you can paste the hexa color code
  await ctx.send("hi") # here you send a message but not a embed
  await ctx.send(embed=embed) #here you send the embed from line 14



bot.run("") #in the "" you paste your token. Now you can start the file
#I hope i help you :)
