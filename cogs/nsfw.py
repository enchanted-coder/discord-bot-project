import discord
import praw
import random
from discord.utils import get
from discord.ext import commands

reddit = praw.Reddit(client_id = "nlbVe1qRb47TaQ",
                    client_secret = "suHhQAaWUWHFTk1rQyMs9whLk8U",
                    username = "dd0n3",
                    password = "changemenow5216",
                    user_agent = "pythonpraw")

class Nsfw(commands.Cog):

    def __init__(self, client):
        self.client = client
#events
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.__class__.__name__} Cog has been loaded\n-----')
#commands

    @commands.group()
    async def nsfw(self, ctx):
        if ctx.invoked_subcommand is None:
            if ctx.channel.is_nsfw():
                await ctx.send("This is only the first command layer")
            else:
                await ctx.send("You need to be in an nsfw channel to use this command")

    @nsfw.group()
    async def help(self, ctx):
        if ctx.channel.is_nsfw():
            
            em = discord.Embed(color=ctx.author.color, description='Commands in this category are: \navatar\ncandy\nporn\nteen\nass\nfemdom\nbdsm\nceleb', timestamp=ctx.message.created_at)
            
            await ctx.send(embed = em)
        else:
            await ctx.send(f"U can't use that command!")

  #r/avatarporn
    @nsfw.group(hidden=True)
    async def avatar(self, ctx):
        if ctx.channel.is_nsfw():
            subreddit = reddit.subreddit("AvatarPorn")
            all_subs = []
            top = subreddit.top(limit = 50)
            for submission in top:
                all_subs.append(submission)
            random_sub = random.choice(all_subs)
            name = random_sub.title
            url = random_sub.url
            em = discord.Embed(title=name, color=ctx.author.color, timestamp=ctx.message.created_at)
            em.set_image(url = url)
            await ctx.send(embed = em)
        else:
            await ctx.send(f"U can't use that command!")

#r/nsfw
    @nsfw.group(hidden=True)
    async def candy(self, ctx):
        if ctx.channel.is_nsfw():
            subreddit = reddit.subreddit("nsfw")
            all_subs = []
            top = subreddit.top(limit = 50)
            for submission in top:
                all_subs.append(submission)
            random_sub = random.choice(all_subs)
            name = random_sub.title
            url = random_sub.url
            em = discord.Embed(title=name, color=ctx.author.color, timestamp=ctx.message.created_at)
            em.set_image(url = url)
            await ctx.send(embed = em)
        else:
            await ctx.send(f"U can't use that command!")

#r/porn
    @nsfw.group(hidden=True)
    async def porn(self, ctx):
        if ctx.channel.is_nsfw():
            subreddit = reddit.subreddit("porn")
            all_subs = []
            top = subreddit.top(limit = 50)
            for submission in top:
                all_subs.append(submission)
            random_sub = random.choice(all_subs)
            name = random_sub.title
            url = random_sub.url
            em = discord.Embed(title=name, color=ctx.author.color, timestamp=ctx.message.created_at)
            em.set_image(url = url)
            await ctx.send(embed = em)
        else:
            await ctx.send(f"U can't use that command!")

#r/LegalTeens
    @nsfw.group(hidden=True)
    async def teen(self, ctx):
        if ctx.channel.is_nsfw():
            subreddit = reddit.subreddit("teen")
            all_subs = []
            top = subreddit.top(limit = 50)
            for submission in top:
                all_subs.append(submission)
            random_sub = random.choice(all_subs)
            name = random_sub.title
            url = random_sub.url
            em = discord.Embed(title=name, color=ctx.author.color, timestamp=ctx.message.created_at)
            em.set_image(url = url)
            await ctx.send(embed = em)
        else:
            await ctx.send(f"U can't use that command!")

#r/ass
    @nsfw.group(hidden=True)
    async def ass(self, ctx):
        if ctx.channel.is_nsfw():
            subreddit = reddit.subreddit("ass")
            all_subs = []
            top = subreddit.top(limit = 50)
            for submission in top:
                all_subs.append(submission)
            random_sub = random.choice(all_subs)
            name = random_sub.title
            url = random_sub.url
            em = discord.Embed(title=name, color=ctx.author.color, timestamp=ctx.message.created_at)
            em.set_image(url = url)
            await ctx.send(embed = em)
        else:
            await ctx.send(f"U can't use that command!")

#r/Femdom
    @nsfw.group(hidden=True)
    async def femdom(self, ctx):
        if ctx.channel.is_nsfw():
            subreddit = reddit.subreddit("Femdom")
            all_subs = []
            top = subreddit.top(limit = 50)
            for submission in top:
                all_subs.append(submission)
            random_sub = random.choice(all_subs)
            name = random_sub.title
            url = random_sub.url
            em = discord.Embed(title=name, color=ctx.author.color, timestamp=ctx.message.created_at)
            em.set_image(url = url)
            await ctx.send(embed = em)
        else:
            await ctx.send(f"U can't use that command!")

#r/bdsm
    @nsfw.group(hidden=True)
    async def bdsm(self, ctx):
        if ctx.channel.is_nsfw():
            subreddit = reddit.subreddit("bdsm")
            all_subs = []
            top = subreddit.top(limit = 50)
            for submission in top:
                all_subs.append(submission)
            random_sub = random.choice(all_subs)
            name = random_sub.title
            url = random_sub.url
            em = discord.Embed(title=name, color=ctx.author.color, timestamp=ctx.message.created_at)
            em.set_image(url = url)
            await ctx.send(embed = em)
        else:
            await ctx.send(f"U can't use that command!")

#r/NudeCelebs
    @nsfw.group(hidden=True)
    async def celeb(self, ctx):
        if ctx.channel.is_nsfw():
            subreddit = reddit.subreddit("NudeCelebs")
            all_subs = []
            top = subreddit.top(limit = 50)
            for submission in top:
                all_subs.append(submission)
            random_sub = random.choice(all_subs)
            name = random_sub.title
            url = random_sub.url
            em = discord.Embed(title=name, color=ctx.author.color, timestamp=ctx.message.created_at)
            em.set_image(url = url)
            await ctx.send(embed = em)
        else:
            await ctx.send(f"U can't use that command!")

   

def setup(client):
    client.add_cog(Nsfw(client))