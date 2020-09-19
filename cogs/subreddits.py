import discord
import random
import praw
from discord.utils import get
from discord.ext import commands

reddit = praw.Reddit(client_id = "nlbVe1qRb47TaQ",
                    client_secret = "suHhQAaWUWHFTk1rQyMs9whLk8U",
                    username = "dd0n3",
                    password = "changemenow5216",
                    user_agent = "pythonpraw")

class Subreddits(commands.Cog):

    def __init__(self, client):
        self.client = client
#events
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.__class__.__name__} Cog has been loaded\n-----')
#commands
 #food
    @commands.command()
    async def food(self, ctx):
        subreddit = reddit.subreddit("food")
        all_subs = []


        new = subreddit.new(limit = 100)

        for submission in new:
            all_subs.append(submission)

            random_sub = random.choice(all_subs)

            name = random_sub.title
            url = random_sub.url

            em = discord.Embed(title=name, color=ctx.author.color, timestamp=ctx.message.created_at)

            em.set_image(url = url)

            await ctx.send(embed = em)

#avatarkyoshi
    @commands.command()
    async def kyoshi(self, ctx):
        subreddit = reddit.subreddit("Avatar_Kyoshi")
        all_subs = []


        new = subreddit.new(limit = 500)

        for submission in new:
            all_subs.append(submission)

        random_sub = random.choice(all_subs)

        name = random_sub.title
        url = random_sub.url

        em = discord.Embed(title=name, color=ctx.author.color, timestamp=ctx.message.created_at)

        em.set_image(url = url)

        await ctx.send(embed = em)

#avatarmemes
    @commands.command()
    async def atlameme(self, ctx):
        subreddit = reddit.subreddit("AvatarMemes")
        all_subs = []


        new = subreddit.new(limit = 500)

        for submission in new:
            all_subs.append(submission)

        random_sub = random.choice(all_subs)

        name = random_sub.title
        url = random_sub.url

        em = discord.Embed(title=name, color=ctx.author.color, timestamp=ctx.message.created_at)

        em.set_image(url = url)

        await ctx.send(embed = em)

 
#avatar
    @commands.command()
    async def atla(self, ctx):
        subreddit = reddit.subreddit("TheLastAirbender")
        all_subs = []


        top = subreddit.top(limit = 500)

        for submission in top:
            all_subs.append(submission)

        random_sub = random.choice(all_subs)

        name = random_sub.title
        url = random_sub.url

        em = discord.Embed(title=name, color=ctx.author.color, timestamp=ctx.message.created_at)

        em.set_image(url = url)

        await ctx.send(embed = em)
#LOK
    @commands.command()
    async def lok(self, ctx):
            subreddit = reddit.subreddit("legendofkorra")
            all_subs = []


            top = subreddit.top(limit = 500)

            for submission in top:
                all_subs.append(submission)

            random_sub = random.choice(all_subs)

            name = random_sub.title
            url = random_sub.url

            em = discord.Embed(title=name, color=ctx.author.color, timestamp=ctx.message.created_at)

            em.set_image(url = url)

            await ctx.send(embed = em)

#korrasami
    @commands.command()
    async def korrasami(self, ctx):
            subreddit = reddit.subreddit("korrasami")
            all_subs = []


            new = subreddit.new(limit = 500)

            for submission in new:
                all_subs.append(submission)

            random_sub = random.choice(all_subs)

            name = random_sub.title
            url = random_sub.url

            em = discord.Embed(title=name, color=ctx.author.color, timestamp=ctx.message.created_at)

            em.set_image(url = url)

            await ctx.send(embed = em)

#kataang
    @commands.command()
    async def kataang(self, ctx):
            subreddit = reddit.subreddit("Kataang")
            all_subs = []


            new = subreddit.new(limit = 500)

            for submission in new:
                all_subs.append(submission)

            random_sub = random.choice(all_subs)

            name = random_sub.title
            url = random_sub.url

            em = discord.Embed(title=name, color=ctx.author.color, timestamp=ctx.message.created_at)

            em.set_image(url = url)

            await ctx.send(embed = em)

#zutara
    @commands.command()
    async def zutara(self, ctx):
            subreddit = reddit.subreddit("ZutaraNation")
            all_subs = []


            new = subreddit.new(limit = 500)

            for submission in new:
                all_subs.append(submission)

            random_sub = random.choice(all_subs)

            name = random_sub.title
            url = random_sub.url

            em = discord.Embed(title=name, color=ctx.author.color, timestamp=ctx.message.created_at)

            em.set_image(url = url)

            await ctx.send(embed = em)

#sukka
    @commands.command()
    async def sukka(self, ctx):
            subreddit = reddit.subreddit("sukka")
            all_subs = []


            new = subreddit.new(limit = 500)

            for submission in new:
                all_subs.append(submission)

            random_sub = random.choice(all_subs)

            name = random_sub.title
            url = random_sub.url

            em = discord.Embed(title=name, color=ctx.author.color, timestamp=ctx.message.created_at)

            em.set_image(url = url)

            await ctx.send(embed = em)

#meme
    @commands.command()
    async def meme(self, ctx):
        subreddit = reddit.subreddit("memes")
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

#cats
    @commands.command()
    async def cats(self, ctx):
        subreddit = reddit.subreddit("cats")
        all_subs = []


        top = subreddit.top(limit = 500)

        for submission in top:
            all_subs.append(submission)

        random_sub = random.choice(all_subs)

        name = random_sub.title
        url = random_sub.url

        em = discord.Embed(title=name, color=ctx.author.color, timestamp=ctx.message.created_at)

        em.set_image(url = url)

        await ctx.send(embed = em)

def setup(client):
    client.add_cog(Subreddits(client))