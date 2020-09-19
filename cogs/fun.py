import discord
import random
from discord.ext import commands
from discord.utils import get
class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client
#events
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.__class__.__name__} Cog has been loaded\n-----')
    
   

#commands
    #say command
    @commands.command(aliases = ['s'])
    @commands.has_permissions(mention_everyone=True)
    async def say(self, ctx, *, message):   
        await ctx.message.delete()
        await ctx.send(message)


    #8ball
    @commands.command(aliases = ['8ball'])
    async def eightball(self, ctx, *, question):
        responses = ['Do you really care?',
                 'I dont know, you tell me',
                 'Maybe one day youll be lucky enough to find out',
                 'I have no way of knowing',
                 'Do I have to answer',
                 'Thank you for asking, though you can judge for yourself',
                 'I dunno. Is it Friday yet?',
                 'I’ll leave that up to your imagination',
                 'Do you want the short or long version?',
                 'In order to answer the question, I need to take you back about ten years. Do you have a moment?',
                 'How much will you pay me if I tell you?',
                 'I promised myself I would kill the next person who asked me that question, but I like you so I will let you live.',
                 'Not today, Satan!',
                 'Wouldnt you like to know']
        await ctx.send(f'{random.choice(responses)}')

        #roast
    @commands.command(aliases=['insult'])
    async def roast(self, ctx, member : discord.Member):
        responses = ['Mirrors cant talk. lucky for you, the cant laugh either.',
                 'If i had a face like yours, id sue my parents',
                 'Your only chance of getting laid is to crawl up a chickens butt and wait',
                 'You must have been born on a highway coz thats where most accidents happen',
                 'is your ass jealous of the amount of shit that just came out of your mouth',
                 'When you were born, the doctor threw you out the window and the window threw you back',
                 'I guess those penis enlargement pills are working, youre twice the dick you were yesterday',
                 'if your parents were to divorce, would they still be brother and sister?',
                 'How many wrinkles does an asshole have? Smile! ill count them.',
                 'Remember to look both ways before you go fuck yourself',
                 'you are like the top piece of bread. Everybody touches you, but nobody wants you.',
                 'The last time i saw something like you... i fllushed it',
                 'Two wrongs dont make a right. Take your parents for example',
                 'Dont be ashamed of who you are. Thats your parents job.',
                 'So tell me... is yout ass aware that your head has moved in?',
                 'If you were a cookie, youd be a whoreo',
                 'I could eat a can of alphabet soup and shit a better argument than yours',
                 'I dont hate you. i just hope your next period happens in a shark tank',
                 'I would slap you but shit splatters',
                 'If i wanted to kill myself i would climb up to your ego and jump to your IQ',
                 'Keep rolling your eyes. Maybe youll find a brain back there',
                 'Being a dick wont make yours any bigger',
                 'The smartest thing that ever came out of your mouth was a penis',
                 'You are as useful as a flat vibrator',
                 'I was going to give you a nasty look... but i see you already have one',
                 'Im typing this with my middle finger',
                 'You look like a before picture',
                 'If you spoke your mind, youd be speechless',


                 ]
        await ctx.message.delete()
        await ctx.send(f'{member.mention} {random.choice(responses)}')

        #ask command
    @commands.command(aliases = ['yn'])
    async def ask(self, ctx, *, question):
        responses = ['yes!',
                 'No!']
        await ctx.send(f'{random.choice(responses)}')

        #coinflip
    @commands.command(aliases=['ht'])
    async def coin(self, ctx):
        choices = ['heads', 'tails']
        rancoin = random.choice(choices)
        await ctx.send(rancoin)

    #ping
    @commands.command()
    @commands.has_permissions(mention_everyone=True)
    async def annoy(self, ctx):
        Events = get(ctx.guild.roles, name='Black Lotus')
        await ctx.send(f'{Events.mention}  losers')

def setup(client):
    client.add_cog(Fun(client))