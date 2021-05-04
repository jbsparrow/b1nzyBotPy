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
        _save()
    elif command not in usagecount:
        usagecount[command] = 1
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

    @commands.command(aliases=['spread', 'americaneagle', 'eagle', 'spreadwide'])
    @commands.is_nsfw()
    async def spreading(self, ctx, pictureid='random'):
        """Spreading."""
        timesused("spreading")
        if pictureid == "random":
            filename = random.choice(os.listdir("cogs/NSFW/Spreading"))
            file = discord.File("cogs/NSFW/Spreading/" + filename, filename="image.png")
            embed = discord.Embed(colour=randomhex(hex))
            embed.set_image(url="attachment://image.png")
            embed.set_footer(text=f'This command has been used {usagecount["spreading"]} times.\nID: {filename.replace(".png", "")}')
            await ctx.send(file=file, embed=embed)
        else:
            picturepath = pictureid + ".png"
            if picturepath in (os.listdir("cogs/NSFW/Spreading")):
                file = discord.File("cogs/NSFW/Spreading/" + picturepath, filename="image.png")
                embed = discord.Embed(colour=randomhex(hex))
                embed.set_image(url="attachment://image.png")
                embed.set_footer(text=f'This command has been used {usagecount["spreading"]} times.')
                await ctx.send(file=file, embed=embed)
            else:
                imagelist = os.listdir("cogs/NSFW/Spreading")
                imagecount = len(imagelist)
                await ctx.send(f'That image ID is invalid. Please try a number from 1 to {imagecount}.')

    @commands.command(aliases=['boobjob', 'tittyfuck', 'titdick', 'dicktit', 'titdicks', 'dicktits'])
    @commands.is_nsfw()
    async def titfuck(self, ctx, pictureid='random'):
        """Tit fucking."""
        timesused("titfuck")
        if pictureid == "random":
            filename = random.choice(os.listdir("cogs/NSFW/BoobJobs"))
            file = discord.File("cogs/NSFW/BoobJobs/" + filename, filename="image.png")
            embed = discord.Embed(colour=randomhex(hex))
            embed.set_image(url="attachment://image.png")
            embed.set_footer(text=f'This command has been used {usagecount["titfuck"]} times.\nID: {filename.replace(".png", "")}')
            await ctx.send(file=file, embed=embed)
        else:
            picturepath = pictureid + ".png"
            if picturepath in (os.listdir("cogs/NSFW/BoobJobs")):
                file = discord.File("cogs/NSFW/BoobJobs/" + picturepath, filename="image.png")
                embed = discord.Embed(colour=randomhex(hex))
                embed.set_image(url="attachment://image.png")
                embed.set_footer(text=f'This command has been used {usagecount["titfuck"]} times.')
                await ctx.send(file=file, embed=embed)
            else:
                imagelist = os.listdir("cogs/NSFW/BoobJobs")
                imagecount = len(imagelist)
                await ctx.send(f'That image ID is invalid. Please try a number from 1 to {imagecount}.')

    @commands.command(aliases=['aheago', 'ahegaos', 'aheagos'])
    @commands.is_nsfw()
    async def ahegao(self, ctx, pictureid='random'):
        """Ahegao."""
        timesused("ahegao")
        if pictureid == "random":
            filename = random.choice(os.listdir("cogs/NSFW/Ahegao"))
            file = discord.File("cogs/NSFW/Ahegao/" + filename, filename="image.png")
            embed = discord.Embed(colour=randomhex(hex))
            embed.set_image(url="attachment://image.png")
            embed.set_footer(text=f'This command has been used {usagecount["ahegao"]} times.\nID: {filename.replace(".png", "")}')
            await ctx.send(file=file, embed=embed)
        else:
            picturepath = pictureid + ".png"
            if picturepath in (os.listdir("cogs/NSFW/Ahegao")):
                file = discord.File("cogs/NSFW/Ahegao/" + picturepath, filename="image.png")
                embed = discord.Embed(colour=randomhex(hex))
                embed.set_image(url="attachment://image.png")
                embed.set_footer(text=f'This command has been used {usagecount["ahegao"]} times.')
                await ctx.send(file=file, embed=embed)
            else:
                imagelist = os.listdir("cogs/NSFW/Ahegao")
                imagecount = len(imagelist)
                await ctx.send(f'That image ID is invalid. Please try a number from 1 to {imagecount}.')

    @commands.command(aliases=['hentais'])
    @commands.is_nsfw()
    async def hentai(self, ctx, pictureid='random'):
        """Hentai."""
        timesused("hentai")
        if pictureid == "random":
            filename = random.choice(os.listdir("cogs/NSFW/Hentai"))
            file = discord.File("cogs/NSFW/Hentai/" + filename, filename="image.png")
            embed = discord.Embed(colour=randomhex(hex))
            embed.set_image(url="attachment://image.png")
            embed.set_footer(text=f'This command has been used {usagecount["hentai"]} times.\nID: {filename.replace(".png", "")}')
            await ctx.send(file=file, embed=embed)
        else:
            picturepath = pictureid + ".png"
            if picturepath in (os.listdir("cogs/NSFW/Hentai")):
                file = discord.File("cogs/NSFW/Hentai/" + picturepath, filename="image.png")
                embed = discord.Embed(colour=randomhex(hex))
                embed.set_image(url="attachment://image.png")
                embed.set_footer(text=f'This command has been used {usagecount["hentai"]} times.')
                await ctx.send(file=file, embed=embed)
            else:
                imagelist = os.listdir("cogs/NSFW/Hentai")
                imagecount = len(imagelist)
                await ctx.send(f'That image ID is invalid. Please try a number from 1 to {imagecount}.')

    @commands.command(aliases=['ubanis'])
    @commands.is_nsfw()
    async def ubani(self, ctx, pictureid='random'):
        """Ubanis."""
        timesused("ubani")
        if pictureid == "random":
            filename = random.choice(os.listdir("cogs/NSFW/Ubanis"))
            file = discord.File("cogs/NSFW/Ubanis/" + filename, filename="image.png")
            embed = discord.Embed(colour=randomhex(hex))
            embed.set_image(url="attachment://image.png")
            embed.set_footer(text=f'This command has been used {usagecount["ubani"]} times.\nID: {filename.replace(".png", "")}')
            await ctx.send(file=file, embed=embed)
        else:
            picturepath = pictureid + ".png"
            if picturepath in (os.listdir("cogs/NSFW/Ubanis")):
                file = discord.File("cogs/NSFW/Ubanis/" + picturepath, filename="image.png")
                embed = discord.Embed(colour=randomhex(hex))
                embed.set_image(url="attachment://image.png")
                embed.set_footer(text=f'This command has been used {usagecount["ubani"]} times.')
                await ctx.send(file=file, embed=embed)
            else:
                imagelist = os.listdir("cogs/NSFW/Ubanis")
                imagecount = len(imagelist)
                await ctx.send(f'That image ID is invalid. Please try a number from 1 to {imagecount}.')

    @commands.command(aliases=['bunnies', 'bunnysuit', 'bunnygirl', 'bunnygirlsuit', 'bunnysuitgirl'])
    @commands.is_nsfw()
    async def bunny(self, ctx, pictureid='random'):
        """Bunny girls."""
        timesused("bunny")
        if pictureid == "random":
            filename = random.choice(os.listdir("cogs/NSFW/BunnySuits"))
            file = discord.File("cogs/NSFW/BunnySuits/" + filename, filename="image.png")
            embed = discord.Embed(colour=randomhex(hex))
            embed.set_image(url="attachment://image.png")
            embed.set_footer(text=f'This command has been used {usagecount["bunny"]} times.\nID: {filename.replace(".png", "")}')
            await ctx.send(file=file, embed=embed)
        else:
            picturepath = pictureid + ".png"
            if picturepath in (os.listdir("cogs/NSFW/BunnySuits")):
                file = discord.File("cogs/NSFW/BunnySuits/" + picturepath, filename="image.png")
                embed = discord.Embed(colour=randomhex(hex))
                embed.set_image(url="attachment://image.png")
                embed.set_footer(text=f'This command has been used {usagecount["bunny"]} times.')
                await ctx.send(file=file, embed=embed)
            else:
                imagelist = os.listdir("cogs/NSFW/BunnySuits")
                imagecount = len(imagelist)
                await ctx.send(f'That image ID is invalid. Please try a number from 1 to {imagecount}.')

    @commands.command(aliases=['analsex', 'buttfuck', 'buttstuff'])
    @commands.is_nsfw()
    async def anal(self, ctx, pictureid='random'):
        """Anal."""
        timesused("anal")
        if pictureid == "random":
            filename = random.choice(os.listdir("cogs/NSFW/Anal"))
            file = discord.File("cogs/NSFW/Anal/" + filename, filename="image.png")
            embed = discord.Embed(colour=randomhex(hex))
            embed.set_image(url="attachment://image.png")
            embed.set_footer(text=f'This command has been used {usagecount["anal"]} times.\nID: {filename.replace(".png", "")}')
            await ctx.send(file=file, embed=embed)
        else:
            picturepath = pictureid + ".png"
            if picturepath in (os.listdir("cogs/NSFW/Anal")):
                file = discord.File("cogs/NSFW/Anal/" + picturepath, filename="image.png")
                embed = discord.Embed(colour=randomhex(hex))
                embed.set_image(url="attachment://image.png")
                embed.set_footer(text=f'This command has been used {usagecount["anal"]} times.')
                await ctx.send(file=file, embed=embed)
            else:
                imagelist = os.listdir("cogs/NSFW/Booty")
                imagecount = len(imagelist)
                await ctx.send(f'That image ID is invalid. Please try a number from 1 to {imagecount}.')

    @commands.command(aliases=['boobs', 'titties', 'honkers', 'mommymilkers'])
    @commands.is_nsfw()
    async def tits(self, ctx, pictureid='random'):
        """Boobs."""
        timesused("tits")
        if pictureid == "random":
            filename = random.choice(os.listdir("cogs/NSFW/Boobs"))
            file = discord.File("cogs/NSFW/Boobs/" + filename, filename="image.png")
            embed = discord.Embed(colour=randomhex(hex))
            embed.set_image(url="attachment://image.png")
            embed.set_footer(text=f'This command has been used {usagecount["tits"]} times.\nID: {filename.replace(".png", "")}')
            await ctx.send(file=file, embed=embed)
        else:
            picturepath = pictureid + ".png"
            if picturepath in (os.listdir("cogs/NSFW/Boobs")):
                file = discord.File("cogs/NSFW/Boobs/" + picturepath, filename="image.png")
                embed = discord.Embed(colour=randomhex(hex))
                embed.set_image(url="attachment://image.png")
                embed.set_footer(text=f'This command has been used {usagecount["tits"]} times.')
                await ctx.send(file=file, embed=embed)
            else:
                imagelist = os.listdir("cogs/NSFW/Boobs")
                imagecount = len(imagelist)
                await ctx.send(f'That image ID is invalid. Please try a number from 1 to {imagecount}.')

    @commands.command(aliases=['traps', 'femboy', 'femboys'])
    @commands.is_nsfw()
    async def trap(self, ctx, pictureid='random'):
        """Traps."""
        timesused("trap")
        if pictureid == "random":
            filename = random.choice(os.listdir("cogs/NSFW/Traps"))
            file = discord.File("cogs/NSFW/Traps/" + filename, filename="image.png")
            embed = discord.Embed(colour=randomhex(hex))
            embed.set_image(url="attachment://image.png")
            embed.set_footer(text=f'This command has been used {usagecount["trap"]} times.\nID: {filename.replace(".png", "")}')
            await ctx.send(file=file, embed=embed)
        else:
            picturepath = pictureid + ".png"
            if picturepath in (os.listdir("cogs/NSFW/Traps")):
                file = discord.File("cogs/NSFW/Traps/" + picturepath, filename="image.png")
                embed = discord.Embed(colour=randomhex(hex))
                embed.set_image(url="attachment://image.png")
                embed.set_footer(text=f'This command has been used {usagecount["trap"]} times.')
                await ctx.send(file=file, embed=embed)
            else:
                imagelist = os.listdir("cogs/NSFW/Traps")
                imagecount = len(imagelist)
                await ctx.send(f'That image ID is invalid. Please try a number from 1 to {imagecount}.')

    @commands.command(aliases=['nekos'])
    @commands.is_nsfw()
    async def neko(self, ctx, pictureid='random'):
        """Nekos."""
        timesused("trap")
        if pictureid == "random":
            filename = random.choice(os.listdir("cogs/NSFW/Nekos"))
            file = discord.File("cogs/NSFW/Nekos/" + filename, filename="image.png")
            embed = discord.Embed(colour=randomhex(hex))
            embed.set_image(url="attachment://image.png")
            embed.set_footer(text=f'This command has been used {usagecount["neko"]} times.\nID: {filename.replace(".png", "")}')
            await ctx.send(file=file, embed=embed)
        else:
            picturepath = pictureid + ".png"
            if picturepath in (os.listdir("cogs/NSFW/Nekos")):
                file = discord.File("cogs/NSFW/Nekos/" + picturepath, filename="image.png")
                embed = discord.Embed(colour=randomhex(hex))
                embed.set_image(url="attachment://image.png")
                embed.set_footer(text=f'This command has been used {usagecount["neko"]} times.')
                await ctx.send(file=file, embed=embed)
            else:
                imagelist = os.listdir("cogs/NSFW/Nekos")
                imagecount = len(imagelist)
                await ctx.send(f'That image ID is invalid. Please try a number from 1 to {imagecount}.')

    @commands.command(aliases=['booty', 'asscheeks', 'bootycheeks', 'dumptruck', 'badonkadonk'])
    @commands.is_nsfw()
    async def ass(self, ctx, pictureid='random'):
        """Ass."""
        timesused("ass")
        if pictureid == "random":
            filename = random.choice(os.listdir("cogs/NSFW/Booty"))
            file = discord.File("cogs/NSFW/Booty/" + filename, filename="image.png")
            embed = discord.Embed(colour=randomhex(hex))
            embed.set_image(url="attachment://image.png")
            embed.set_footer(text=f'This command has been used {usagecount["ass"]} times.\nID: {filename.replace(".png", "")}')
            await ctx.send(file=file, embed=embed)
        else:
            picturepath = pictureid + ".png"
            if picturepath in (os.listdir("cogs/NSFW/Booty")):
                file = discord.File("cogs/NSFW/Booty/" + picturepath, filename="image.png")
                embed = discord.Embed(colour=randomhex(hex))
                embed.set_image(url="attachment://image.png")
                embed.set_footer(text=f'This command has been used {usagecount["ass"]} times.')
                await ctx.send(file=file, embed=embed)
            else:
                imagelist = os.listdir("cogs/NSFW/Booty")
                imagecount = len(imagelist)
                await ctx.send(f'That image ID is invalid. Please try a number from 1 to {imagecount}.')

        # general error handling.
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.errors.NSFWChannelRequired):
            await ctx.send(f'This command can only be used in NSFW channels.')


def setup(bot):
    bot.add_cog(NSFW(bot))
