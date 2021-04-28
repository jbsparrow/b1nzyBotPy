import datetime
import json
import os
import random

import discord
from discord.ext import commands
from termcolor import cprint

from cogs.Fun import randomhex

intents = discord.Intents.default()
intents.members = True


client = discord.Client(intents=intents)
currenttime = datetime.datetime.now()
guild = discord.guild

usagecount = {}


def _save():
    with open('cogs/usagecount.json', 'w') as f:
        json.dump(usagecount, f)


def timesused(x):
    command = x
    if command in usagecount:
        usagecount[command] = usagecount[command] + 1
        cprint(f'the ', 'green', end='')
        cprint(f'{command} ', 'blue', end='')
        cprint(f'command has been used {usagecount[command]} times.', 'green')
        _save()
    elif command not in usagecount:
        usagecount[command] = 1
        print("You\'re the first person to use this command! {} usage so far!".format(usagecount[command]))
        _save()


class NSFW(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # says when bot is online
    @commands.Cog.listener()
    async def on_ready(self):
        print('NSFW cog is online.\n')
        global usagecount
        try:
            with open('cogs/usagecount.json') as f:
                usagecount = json.load(f)
                cprint('usagecount.json', 'yellow', end='')
                print(' is loaded\n')
        except FileNotFoundError:
            print("Could not load usagecount.json")
            usagecount = {}

    @commands.command(aliases=['aheago', 'ahegaos', 'aheagos'])
    @commands.is_nsfw()
    async def ahegao(self, ctx):
        """Ahegao."""
        timesused('ahegao')
        file = discord.File("cogs/NSFW/Ahegao/"+(random.choice(os.listdir("cogs/NSFW/Ahegao"))), filename="image.png")
        embed = discord.Embed(colour=randomhex(hex))
        embed.set_image(url="attachment://image.png")
        embed.set_footer(text=f'This command has been used {usagecount["ahegao"]} times.')
        await ctx.send(file=file, embed=embed)

    @commands.command(aliases=['traps', 'femboy', 'femboys'])
    @commands.is_nsfw()
    async def trap(self, ctx):
        """Traps."""
        timesused('trap')
        file = discord.File("cogs/NSFW/Traps/"+(random.choice(os.listdir("cogs/NSFW/Traps"))), filename="image.png")
        embed = discord.Embed(colour=randomhex(hex))
        embed.set_image(url="attachment://image.png")
        embed.set_footer(text=f'This command has been used {usagecount["trap"]} times.')
        await ctx.send(file=file, embed=embed)

    @commands.command(aliases=['ubanis'])
    @commands.is_nsfw()
    async def ubani(self, ctx):
        """Ubanis."""
        timesused('ubani')
        file = discord.File("cogs/NSFW/Ubanis/"+(random.choice(os.listdir("cogs/NSFW/Ubanis"))), filename="image.png")
        embed = discord.Embed(colour=randomhex(hex))
        embed.set_image(url="attachment://image.png")
        embed.set_footer(text=f'This command has been used {usagecount["ubani"]} times.')
        await ctx.send(file=file, embed=embed)

    @commands.command(aliases=['hentais'])
    @commands.is_nsfw()
    async def hentai(self, ctx):
        """Hentai."""
        timesused('hentai')
        file = discord.File("cogs/NSFW/Hentai/"+(random.choice(os.listdir("cogs/NSFW/Hentai"))), filename="image.png")
        embed = discord.Embed(colour=randomhex(hex))
        embed.set_image(url="attachment://image.png")
        embed.set_footer(text=f'This command has been used {usagecount["hentai"]} times.')
        await ctx.send(file=file, embed=embed)

    @commands.command(aliases=['nekos'])
    @commands.is_nsfw()
    async def neko(self, ctx):
        """Nekos."""
        timesused('neko')
        file = discord.File("cogs/NSFW/Nekos/" + (random.choice(os.listdir("cogs/NSFW/Nekos"))), filename="image.png")
        embed = discord.Embed(colour=randomhex(hex))
        embed.set_image(url="attachment://image.png")
        embed.set_footer(text=f'This command has been used {usagecount["neko"]} times.')
        await ctx.send(file=file, embed=embed)

    @commands.command(aliases=['bunnies', 'bunnysuit', 'bunnygirl', 'bunnygirlsuit', 'bunnysuitgirl'])
    @commands.is_nsfw()
    async def bunny(self, ctx):
        """Bunny girls."""
        timesused('bunny')
        file = discord.File("cogs/NSFW/BunnySuits/" + (random.choice(os.listdir("cogs/NSFW/BunnySuits"))), filename="image.png")
        embed = discord.Embed(colour=randomhex(hex))
        embed.set_image(url="attachment://image.png")
        embed.set_footer(text=f'This command has been used {usagecount["bunny"]} times.')
        await ctx.send(file=file, embed=embed)

    @commands.command(aliases=['boobjob', 'tittyfuck', 'titdick', 'dicktit', 'titdicks', 'dicktits'])
    @commands.is_nsfw()
    async def titfuck(self, ctx):
        """Tit fucking."""
        timesused('titfuck')
        file = discord.File("cogs/NSFW/BoobJobs/" + (random.choice(os.listdir("cogs/NSFW/BoobJobs"))), filename="image.png")
        embed = discord.Embed(colour=randomhex(hex))
        embed.set_image(url="attachment://image.png")
        embed.set_footer(text=f'This command has been used {usagecount["titfuck"]} times.')
        await ctx.send(file=file, embed=embed)

    @commands.command(aliases=['booty', 'asscheeks', 'bootycheeks', 'dumptruck', 'badonkadonk'])
    @commands.is_nsfw()
    async def ass(self, ctx):
        """Ass."""
        timesused('ass')
        file = discord.File("cogs/NSFW/Booty/" + (random.choice(os.listdir("cogs/NSFW/Booty"))), filename="image.png")
        embed = discord.Embed(colour=randomhex(hex))
        embed.set_image(url="attachment://image.png")
        embed.set_footer(text=f'This command has been used {usagecount["ass"]} times.')
        await ctx.send(file=file, embed=embed)

    @commands.command(aliases=['banggang'])
    @commands.is_nsfw()
    async def gangbang(self, ctx):
        """Gangbangs."""
        timesused('gangbang')
        file = discord.File("cogs/NSFW/Gangbangs/" + (random.choice(os.listdir("cogs/NSFW/Gangbangs"))), filename="image.png")
        embed = discord.Embed(colour=randomhex(hex))
        embed.set_image(url="attachment://image.png")
        embed.set_footer(text=f'This command has been used {usagecount["gangbang"]} times.')
        await ctx.send(file=file, embed=embed)

    @commands.command(aliases=['boobs', 'titties', 'honkers'])
    @commands.is_nsfw()
    async def tits(self, ctx):
        """Boobs."""
        timesused('tits')
        file = discord.File("cogs/NSFW/Boobs/" + (random.choice(os.listdir("cogs/NSFW/Boobs"))), filename="image.png")
        embed = discord.Embed(colour=randomhex(hex))
        embed.set_image(url="attachment://image.png")
        embed.set_footer(text=f'This command has been used {usagecount["tits"]} times.')
        await ctx.send(file=file, embed=embed)

    @commands.command(aliases=['analsex', 'buttfuck', 'buttstuff'])
    @commands.is_nsfw()
    async def anal(self, ctx):
        """Anal."""
        timesused('anal')
        file = discord.File("cogs/NSFW/Anal/" + (random.choice(os.listdir("cogs/NSFW/Anal"))),  filename="image.png")
        embed = discord.Embed(colour=randomhex(hex))
        embed.set_image(url="attachment://image.png")
        embed.set_footer(text=f'This command has been used {usagecount["anal"]} times.')
        await ctx.send(file=file, embed=embed)

    @commands.command(aliases=['spread', 'americaneagle', 'eagle', 'spreadwide'])
    @commands.is_nsfw()
    async def spreading(self, ctx):
        """Spreading."""
        timesused('spreading')
        file = discord.File("cogs/NSFW/Spreading/" + (random.choice(os.listdir("cogs/NSFW/Spreading"))), filename="image.png")
        embed = discord.Embed(colour=randomhex(hex))
        embed.set_image(url="attachment://image.png")
        embed.set_footer(text=f'This command has been used {usagecount["spreading"]} times.')
        await ctx.send(file=file, embed=embed)

    @commands.command()
    async def savecounter(self, ctx):
        _save()
        print('Saved!')

        # general error handling.
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.errors.NSFWChannelRequired):
            await ctx.send(f'This command can only be used in NSFW channels.')


def setup(bot):
    bot.add_cog(NSFW(bot))
