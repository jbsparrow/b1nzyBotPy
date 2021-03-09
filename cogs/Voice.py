import datetime
import discord
from discord import FFmpegPCMAudio
from discord.ext import commands
from discord.utils import get
intents = discord.Intents.default()
intents.members = True

OPUS_LIBS = ['libopus-0.x86.dll', 'libopus-0.x64.dll', 'libopus-0.dll', 'libopus.so.0', 'libopus.0.dylib']


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
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        if not voice:
            await ctx.send("I am not in a voice channel.")
            return
        await voice.disconnect()

    @commands.command(aliases=['connect'])
    async def join(self, ctx):
        channel = ctx.message.author.voice.channel
        await channel.connect()

    @commands.is_owner()
    @commands.command(aliases=['p'])
    async def play(self, ctx):
        def musictest():
            pass

        """joins the voice channel the user is in at time of command initiation."""
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        voice.play(FFmpegPCMAudio("test.mp3"), after=lambda e: musictest())
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 0.07


def setup(bot):
    bot.add_cog(Voice(bot))
