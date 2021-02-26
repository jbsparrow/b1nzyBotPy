import datetime
from discord.ext import commands
import asyncio
import discord
import mtranslate
import os
from dotenv import load_dotenv


load_dotenv()

YOUR_USER_ID = int(os.getenv('YOUR_USER_ID'))


intents = discord.Intents.default()
intents.members = True
intents.messages = True
client = discord.Client(intents=intents)
currenttime = datetime.datetime.now()
guild = discord.guild


class Utilities(commands.Cog):

    # This category has a bunch of commands that are actually *somewhat* useful.
    def __init__(self, bot):
        self.bot = bot

    # Says when bot is online
    @commands.Cog.listener()
    async def on_ready(self):
        print('Utilities cog is online.\n')

    # Sends suggestion logs.
    @commands.command(aliases=['suggestlog', 'suggestions'], hidden=True)
    @commands.is_owner()
    async def suggestlogs(self, ctx):
        # put your user ID below to have logs sent to you.
        user = self.bot.get_user(YOUR_USER_ID)
        await user.send(file=discord.File("cogs/suggestions.txt"))

    #   Translate the inputted text to english.
    @commands.command()
    async def translate(self, ctx, *,  untranslated):
        """Translates the inputted text."""
        #   translate the text into english.
        #   Currently not translating into other languages as this library takes shorthands for languages and I don't want to write something to convert the user's language of choice into a shorthand at the moment.
        translated = mtranslate.translate(untranslated, "en", "auto")
        await ctx.send(translated)

    @commands.command(hidden=True)
    # checks to see if user has proper perms
    @commands.has_permissions(manage_channels=True)
    async def createtextchannel(self, ctx, *, newchannelname):
        """creates a text channel with the specified name."""
        guild = ctx.message.guild
        #   Replace spaces in the channel name with dashes so that discord allows it.
        newchannelname = newchannelname.replace(" ", "-")
        #   Create the text channel
        await guild.create_text_channel(newchannelname)

    @commands.command(hidden=True)
    # Checks to see if user has proper perms
    @commands.has_permissions(manage_channels=True)
    async def createvoicechannel(self, ctx, *, newchannelname):
        """creates a voice channel with the specified name."""
        guild = ctx.message.guild
        #   Create the voice channel
        await guild.create_voice_channel(newchannelname)

    @commands.command(hidden=True)
    # Checks to see if user has proper perms
    @commands.has_permissions(manage_channels=True)
    async def createcategory(self, ctx, *, newcategoryname):
        """creates a category with the specified name."""
        guild = ctx.message.guild
        #   Create the category
        await guild.create_category(newcategoryname)

    @commands.command(hidden=True)
    # Checks to see if user has proper perms
    @commands.has_permissions(manage_roles=True)
    async def createrole(self, ctx, newrolename, reason):
        """creates a role with the specified name."""
        guild = ctx.message.guild
        #   Create the role
        await guild.create_role(name=newrolename, mentionable=False, hoist=False, reason=reason, colour=discord.Colour(0x7289DA))

    #   Send b1nzy's ping
    @commands.command()
    async def ping(self, ctx):
        """shows b1nzyBot's ping."""
        await ctx.send(f'Pong! b1nzy\'s ping is {round(self.bot.latency * 1000)}ms.')

    @commands.command(aliases=['purge'])
    #   Check to see if user has proper perms
    @commands.has_permissions(manage_messages=True)
    #   Clear 10 messages if no number is specified.
    async def clear(self, ctx, amount=10):
        """clears the specified number of messages, default is 10."""
        #   Add 1 to the clear so that the invocation command is also cleared.
        await ctx.channel.purge(limit=amount + 1)
        #   Say that the messages were cleared (useless)
        await ctx.send(f'Successfully cleared {amount} messages.')
        #   Sleep for 2 seconds and then clear the message saying that the messages were successfully cleared.
        await asyncio.sleep(2)
        await ctx.channel.purge(limit=1)

        # error handling
    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.errors.MissingPermissions):
            await ctx.send('You do not have the required permissions to use this.')
        elif isinstance(error, commands.errors.BotMissingPermissions):
            await ctx.send('I do not have the required permissions to use this.')

    @commands.command(hidden=True)
    # checks to see if user has proper perms
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        """kicks the specified user."""
        await member.kick(reason=reason)
        await ctx.send(f'Kicked {member.mention}')

        # error handling
    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.errors.MissingPermissions):
            await ctx.send('You do not have the required permissions to use this.')
        elif isinstance(error, commands.errors.BotMissingPermissions):
            await ctx.send('I do not have the required permissions to use this.')

    @commands.command(hidden=True)
    # checks to see if user has proper perms
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        """bans the specified user."""
        await member.ban(reason=reason)
        await ctx.send(f'Banned {member.mention}')

        # error handling
    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.errors.MissingPermissions):
            await ctx.send('You do not have the required permissions to use this.')
        elif isinstance(error, commands.errors.BotMissingPermissions):
            await ctx.send('I do not have the required permissions to use this.')

    @commands.command(hidden=True)
    # checks to see if user has proper perms
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        """unbans the specified user."""
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.mention}')
                return

            # error handling
    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, commands.errors.MissingPermissions):
            await ctx.send('You do not have the required permissions to use this.')
        elif isinstance(error, commands.errors.BotMissingPermissions):
            await ctx.send('I do not have the required permissions to use this.')


def setup(bot):
    bot.add_cog(Utilities(bot))
