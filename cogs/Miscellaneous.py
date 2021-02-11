import datetime
from discord.ext import commands
import discord
import os
from dotenv import load_dotenv
load_dotenv()
intents = discord.Intents.default()
intents.members = True


client = discord.Client(intents=intents)
currenttime = datetime.datetime.now()
guild = discord.guild


class Miscellaneous(commands.Cog):

    # Events
    def __init__(self, bot):
        self.bot = bot

# says when bot is online
    @commands.Cog.listener()
    async def on_ready(self):
        print('Miscellaneous cog is online.\n')

    # genecho and botecho are channel specific echo commands that notify you if somebody uses it. Will switch to using checks eventually, for now I'm just using an if statement though.
    @commands.command(hidden=True)
    async def genecho(self, ctx, *, arg):
        """echoes your input in general of rocketcat"""
        message = ctx.message
        # add your user ID to usersend to be notified when someone uses the command.
        usersend = self.bot.get_user(329377582476951552)
        # add a friend's user ID below for them to be notified when someone uses the command.
        user2send = self.bot.get_user(477639802171424788)
        # add the channel ID for the channel you would like the message to be sent in below
        channelsend = self.bot.get_channel(788803275155177502)
        # IMPORTANT: if you do not add your user ID here and your friend's user ID below, then the command will not work.
        # if you do not want to add a friend, remove the comment on the line below, delete the if statement that says "(329377582476951552, 477639802171424788):" and remove all instances of "user2send"
        # if message.author.id = 329377582476951552
        if message.author.id in (329377582476951552, 477639802171424788):
            await channelsend.send(f'{arg}')
            # the code below this comment is irrelevant, the only thing needed is the await channel.send and if you want you could keep that else and put a return statement after it.
            await usersend.send(f'<@{329377582476951552}>**,**\n<@{message.author.id}>** sent **`"{arg}"`** in **<#{788803275155177502}>**.**')
            await user2send.send(f'<@{477639802171424788}>**,**\n<@{message.author.id}>** sent **`"{arg}"`** in **<#{788803275155177502}>**.**')
            print(f'\n\nIMPORTANT\n{message.author} sent "{arg}" in {channelsend}.\nIMPORTANT\n')
        else:
            await usersend.send(f'<@{329377582476951552}>**,**\n<@{message.author.id}>** tried to send **`"{arg}"`** in **<#{788803275155177502}>**.**')
            await user2send.send(f'<@{477639802171424788}>**,**\n<@{message.author.id}>** tried to send **`"{arg}"`** in **<#{788803275155177502}>**.**')
            print(f'\n\nIMPORTANT\n{message.author} tried to send "{arg}" in {channelsend}.\nIMPORTANT\n')

    @commands.command(hidden=True)
    async def botecho(self, ctx, *, arg):
        """echoes your input in bot commands of rocketcat"""
        message = ctx.message
        # add your user ID to usersend to be notified when someone uses the command.
        usersend = self.bot.get_user(329377582476951552)
        # add a friend's user ID below for them to be notified when someone uses the command.
        user2send = self.bot.get_user(477639802171424788)
        # add the channel ID for the channel you would like the message to be sent in below
        channelsend = self.bot.get_channel(788825205039824907)
        # IMPORTANT: if you do not add your user ID here and your friend's user ID below, then the command will not work.
        # if you do not want to add a friend, remove the comment on the line below, delete the if statement that says "(329377582476951552, 477639802171424788):" and remove all instances of "user2send"
        # if message.author.id = 329377582476951552
        if message.author.id in (329377582476951552, 477639802171424788):
            await channelsend.send(f'{arg}')
            # the code below this comment is irrelevant, the only thing needed is the await channel.send and if you want you could keep that else and put a return statement after it.
            await usersend.send(f'<@329377582476951552>**,**\n<@{message.author.id}>** sent **`"{arg}"`** in **<#788825205039824907>**.**\n')
            await user2send.send(f'<@477639802171424788>**,**\n<@{message.author.id}>** sent **`"{arg}"`** in **<#788825205039824907>**.**\n')
            print(f'\n\nIMPORTANT\n{message.author} sent "{arg}" in {channelsend}.\nIMPORTANT\n')
        else:
            await usersend.send(f'<@329377582476951552>**,**\n<@{message.author.id}>** tried to send **`"{arg}"`** in **<#788825205039824907>**.**\n')
            await user2send.send(f'<@477639802171424788>**,**\n<@{message.author.id}>** tried to send **`"{arg}"`** in **<#788825205039824907>**.**\n')
            print(f'\n\nIMPORTANT\n{message.author} tried to send "{arg}" in {channelsend}.\nIMPORTANT\n')

    #   command to dm users, as far as I know it doesn't work and I don't care enough to fix it
    @commands.command(hidden=True)
    async def dmuser(self, ctx, arg, *userid):
        """command used to dm other users through b1nzy. usage: $dmuser "message" "user id" - cannot recieve replies."""
        user = self.bot.get_user(userid)
        await user.send(arg)

    #   equivelant of genecho and botecho but everyone can use it. - Broken
    @commands.command(hidden=True)
    async def echo(self, ctx, arg, *channelid):
        """allows you to talk as b1nzy. - usage: $echo "message" "channel id" - If you don't use the quotes it won't work."""
        channel = self.bot.get_channel(channelid)
        await channel.send(f'{arg}')

    #   command to receive suggestions because I can't think of new features for my bot.
    @commands.command(aliases=['suggestion'])
    async def suggest(self, ctx, *, suggestion):
        """submit ideas for new features!"""
        message = ctx.message
        user = self.bot.get_user(329377582476951552)
        f = open("cogs/suggestions.txt", "a")
        await user.send(f'<@{message.author.id}> suggested: ```"{suggestion}"```')
        await ctx.send(f'Your submission has been recieved, I will contact you with some questions if it is accepted.')
        f.write(f'{message.author} - <@{message.author.id}> suggested: "{suggestion}"\n')

    # credits for the bot, sends embed containing anybody that helped to directly, or indirectly, make b1nzyBot.
    @commands.command()
    async def credits(self, ctx):
        """displays the bot's credits. included is anybody who helped me make this bot and any code that was copied from other bots."""
        embed = discord.Embed(title='Credits',
                              description="credits, anybody listed here helped me either directly or indirectly in the making of this bot.",
                              colour=0x7289DA)
        embed.set_author(name='B1nzyBot',
                         url='https://takeb1nzyto.space',
                         icon_url='https://cdn.discordapp.com/attachments/794323054317928478/794385737235562506/image.png')

        embed.add_field(name='Inspiration', value='[Click here](https://github.com/twotxh)')
        embed.add_field(name='More inspiration', value='[Click here](https://b1nzy.com)')

        await ctx.send(embed=embed)

    # sends invite link for b1nzyBot.
    @commands.command()
    async def invite(self, ctx):
        """sends an invite link for b1nzyBot."""
        await ctx.send('https://discord.com/api/oauth2/authorize?client_id=788978875287470091&permissions=8&redirect_uri=https%3A%2F%2Fdiscord.com%2Fapi%2Foauth2%2Fauthorize&scope=bot')

    # useless command used to index emotes in servers the bot is in for use in messages.
    @commands.command(hidden=True)
    @commands.is_owner()
    async def emoteids(self, ctx):
        """prints all the emote details of a server in the console."""
        await ctx.channel.purge(limit=1)
        print(f'{ctx.guild.emojis}')

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


# set up all command categories
def setup(bot):
    bot.add_cog(Miscellaneous(bot))
