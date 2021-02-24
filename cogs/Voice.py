import datetime
from discord.ext import commands
import discord
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
        vc = ctx.voice_client
        if not vc:
            await ctx.send("I am not in a voice channel.")
            return
        await vc.disconnect()

    @commands.command(aliases=['connect'])
    async def join(self, ctx):
        """joins the voice channel the user is in at time of command initiation."""
        channel = ctx.message.author.voice.channel
        voice_client: discord.VoiceClient = discord.utils.get(self.bot.voice_clients, guild=guild)
        audio_source = discord.FFmpegPCMAudio('audio.mp3')
        await channel.connect()
        voice_client.play(audio_source, after=None)


def setup(bot):
    bot.add_cog(Voice(bot))
