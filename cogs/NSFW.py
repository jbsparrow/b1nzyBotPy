import os
import random
import datetime
from discord.ext import commands
import discord
intents = discord.Intents.default()
intents.members = True


client = discord.Client(intents=intents)
currenttime = datetime.datetime.now()
guild = discord.guild


class NSFW(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # says when bot is online
    @commands.Cog.listener()
    async def on_ready(self):
        print('MkDir cog is online.\n')

    @commands.command()
    @commands.is_nsfw()
    async def ahegao(self, ctx):
        """Ahegao."""
        await ctx.send(file=discord.File("cogs/Special/Ahegao/"+(random.choice(os.listdir("cogs/Special/Ahegao")))))

    @commands.command()
    @commands.is_nsfw()
    async def trap(self, ctx):
        """Traps."""
        await ctx.send(file=discord.File("cogs/Special/Traps/"+(random.choice(os.listdir("cogs/Special/Traps")))))

        # general error handling.
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.errors.NSFWChannelRequired):
            await ctx.send(f'This command can only be used in NSFW channels.')


def setup(bot):
    bot.add_cog(NSFW(bot))
