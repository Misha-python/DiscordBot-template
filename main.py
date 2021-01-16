import discord
from discord.ext import commands

from config import settings
from style import *

TOKEN = settings ['token']
ver = '0.0.0'
build_info = 'Non - govnocode build' #It's a specific Russian joke

bot = commands.Bot (command_prefix = settings ['prefix'])

def add_command (name): # Only to add to special dict
    def adder (func):
        add_command.commands_dict [name] = func

        return func
    return adder

def add_egg (name): #Easter eggs like a classic commands, but without prefix see more in documentation (???)
    def adder_ (func):
        add_egg.egg_dict [name] = func

        return func
    return adder_

add_command.commands_dict = {}
add_egg.egg_dict = {}
    
@add_command ('help') #Example how to do commands with my framework
async def help (ctx):
    ctx.send ('Help message')
    
@bot.event 
async def on_message (message): 
    if message.author.bot:
        return

    if message.content.lower () == 'help':
        await message.channel.send (f'Type `{settings ["prefix"]}help` to get help')

        return

    check = lambda val: message.content.lower().startswith (settings ["prefix"] + val)

    if check (''):
        for command_name in add_command.commands_dict:
            if check (command_name):
                await add_command.commands_dict [command_name] (bot.get_context (message))

                break

        else:
            await message.channel.send ('unknow command')

        return

    else:
        for egg in add_egg.egg_dict:
            if message.content.startswith (egg):
                await add_egg.egg_dict [egg] (bot.get_context (message))

                return

bot.run (TOKEN)
