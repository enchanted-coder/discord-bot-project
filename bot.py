import discord
import json
import asyncio
import shutil
import traceback
import sys
import os
import random
from discord.utils import get
from discord.ext import commands
import wikipedia,os
from chatbot import Chat, register_call
import datetime






client = commands.Bot(
    command_prefix = '!kuv ',
    case_insensitive=True,
    owner_id=621299153322115093
    #help_commands=None
    )


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Streaming(name='.gg/gaang | !kuv help', url='https://www.twitch.tv/avatar_gaang'))
    print('Bot is online')

#client.remove_command('help')

#cogs
@client.command(hidden=True)
async def enable(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    em = discord.Embed(color=ctx.author.color, description=f'{extension} extension has been enabled', timestamp=ctx.message.created_at)
    await ctx.send(embed = em)

    #await ctx.send(f'{extension}been enanled extension has ')

@client.command(hidden=True)
async def disable(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    em = discord.Embed(color=ctx.author.color, description=f'{extension} extension has been disabled', timestamp=ctx.message.created_at)
    await ctx.send(embed = em)


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
        
@register_call('whoIs')
def who_is(query, session_id='general'):
    try:
        return wikipedia.summary(query)
    except Exception:
        for new_query in wikipedia.search(query):
            try:
                return wikipedia.summary(new_query)
            except Exception:
                pass
    return 'I dont know about '+query
template_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'chatbotTemplate','chatbottemplate.template')
chat=Chat(template_file_path)

@client.command()
async def chatter(ctx, *, message):
    result = chat.respond(message)
    if(len(result)<=2048):
        embed=discord.Embed(title="Kuvira The Great", description = result, color = (0xF48D1))
        await ctx.send(embed=embed)
    else:
        embedList = []
        n=2048
        embedList = [result[i:i+n] for i in range(0, len(result), n)]
        for num, item in enumerate(embedList, start = 1):
            if(num == 1):
                embed = discord.Embed(title="Kuvira The Great", description = item, color = (0xF48D1))
                embed.set_footer(text="Page{}".format(num))
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(description = item, color = (0xF48D1))
                embed.set_footer(text = "Page {}".format(num))
                await ctx.send(embed = embed)

#getlatency
@client.command(hidden=True)
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

#nuke
@client.command(hidden=True)
@commands.has_permissions(ban_members=True)
async def nuke(ctx):
    
    await ctx.send(f'Nuking server in: 60 seconds!! THIS ACTION CANNOT BE STOPPED!!')

@client.command(hidden=True)
@commands.has_permissions(ban_members=True)
async def defuse(ctx):
    await ctx.send(f'Nuke has been stopped')
    
    

#errorhandling
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('please pass in all required arguments')
#uncomment these if doesnt work properly
#@clear.error
#async def clear_error(ctx, error):

client.run(os.environ['TOKEN'])
