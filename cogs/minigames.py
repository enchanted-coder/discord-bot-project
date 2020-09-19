import discord
from discord.ext import commands
from discord.utils import get

class Minigames(commands.Cog):

    def __init__(self, client):
        self.client = client
#events
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.__class__.__name__} Cog has been loaded\n-----')
#commands
  #gambling ring
    @commands.command()
    @commands.has_permissions(mention_everyone=True)
    async def gambling_ring(self, ctx):
        Events = get(ctx.guild.roles, name='Games & Events')
        await ctx.send(f'{Events.mention} Gambling ring is now open! No losses and everyone wins, so come and play')

    @commands.command()
    async def paranoia(self, ctx):
        await ctx.send(f' this game is still in development')



def setup(client):
    client.add_cog(Minigames(client))