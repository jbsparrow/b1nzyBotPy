import datetime
from discord.ext import commands
import discord
intents = discord.Intents.default()
intents.members = True


client = discord.Client(intents=intents)
currenttime = datetime.datetime.now()
guild = discord.guild


class Voice(commands.Cog):
    # this category works, but I can't get opus to work so this is pretty useless.

    def __init__(self, bot):
        self.bot = bot

    # says when bot is online
    @commands.Cog.listener()
    async def on_ready(self):
        print('Voice cog is online.\n')

    @commands.command(aliases=['dc', 'fuckoff', 'leave'])
    async def disconnect(self, ctx):
        """leaves the voice channel that b1nzyBot is currently in."""
        vc = ctx.voice_client
        if not vc:
            await ctx.send("I am not in a voice channel.")
            return
        await vc.disconnect()

    @commands.command(aliases=['connect'])
    async def join(self, ctx):
        """joins the voice channel the user is in at time of command initiation."""
        channel = ctx.message.author.voice.channel
        await channel.connect()

        # general error handling.
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.UserInputError):
            await ctx.send(f'Incorrect arguments passed, please try again.')
            if isinstance(error, commands.CommandNotFound):
                await ctx.send(f'That command does not exist.')
            if isinstance(error, commands.MissingPermissions):
                await ctx.send(f'<@{ctx.author.id}>, You do not have the required permissions to do that.')
            if isinstance(error, commands.CommandOnCooldown):
                await ctx.send(f'<@{ctx.author.id}>, this command is on cooldown for you!')


def setup(bot):
    bot.add_cog(Voice(bot))
