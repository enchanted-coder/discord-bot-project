import discord
from discord.ext import commands

class Mod(commands.Cog):

    def __init__(self, client):
        self.client = client
#events
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.__class__.__name__} Cog has been loaded\n-----')
#commands
#kick
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def  kick(self, ctx, member: discord.Member, *, reason='No reason'):
        await member.send('You have been kicked from Avatar Gaang for '+reason)
        await member.kick(reason=reason)
        

        embed = discord.Embed(colour=ctx.author.color, description=f'{member.mention} was kicked by {ctx.author.mention}. Reason {reason}')
        #embed.add_field(name=kick, value=str(reason))
        embed.title = "kicked"
        #embed.set_thumbnail(url='https://tenor.com/view/bane-no-banned-and-you-are-explode-gif-16047504')
        await ctx.send(embed=embed)

#ban
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def  ban(self, ctx, member: discord.Member, *, reason='No reason'):
        await member.send('You have been banned from Avatar Gaang for '+reason)
        await member.ban(reason=reason)
        

        embed = discord.Embed(colour=ctx.author.color, description=f'{member.mention} was banned by {ctx.author.mention}. Reason {reason}')
        embed.title = "banned"
        embed.set_thumbnail(url='https://tenor.com/view/bane-no-banned-and-you-are-explode-gif-16047504')
        await ctx.send(embed=embed)


#clear/purge
    @commands.command(aliases=['c'])
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount + 1)
        #await ctx.send(f'{amount} messages have been purged')

        embed = discord.Embed(colour=ctx.author.color, description=f'{amount} messages have been purged')
    
        await ctx.send(embed=embed)
        await ctx.channel.purge(limit = 1)

def setup(client):
    client.add_cog(Mod(client))