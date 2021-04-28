import datetime
from discord.ext import commands
import discord
import os
from dotenv import load_dotenv
from termcolor import cprint
from pytz import timezone

from cogs.Fun import randomhex

load_dotenv()
intents = discord.Intents.default()
intents.members = True


client = discord.Client(intents=intents)
currenttime = datetime.datetime.now()
guild = discord.guild

INSULT_USER_ID = int(os.getenv('INSULT_USER_ID'))
YOUR_USER_ID = int(os.getenv('YOUR_USER_ID'))
FRIEND_USER_ID = int(os.getenv('FRIEND_USER_ID'))
SERVER_GENERAL = int(os.getenv('SERVER_GENERAL'))
SERVER_BOT_COMMANDS = int(os.getenv('SERVER_BOT_COMMANDS'))


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
        usersend = self.bot.get_user(YOUR_USER_ID)
        # add a friend's user ID below for them to be notified when someone uses the command.
        user2send = self.bot.get_user(FRIEND_USER_ID)
        # add the channel ID for the channel you would like the message to be sent in below
        channelsend = self.bot.get_channel(SERVER_GENERAL)
        # IMPORTANT: if you do not add your user ID here and your friend's user ID below, then the command will not work.
        # if you do not want to add a friend, remove the comment on the line below, delete the if statement that says "(YOUR_USER_ID, FRIEND_USER_ID):" and remove all instances of "user2send"
        # if message.author.id = YOUR_USER_ID
        if message.author.id in (YOUR_USER_ID, FRIEND_USER_ID):
            await channelsend.send(f'{arg}')
            # the code below this comment is irrelevant, the only thing needed is the await channel.send and if you want you could keep that else and put a return statement after it.
            usersentembed = discord.Embed(colour=randomhex(hex))

            usersentembed.set_footer(text='User sent')

            usersentembed.set_author(name='b1nzy', icon_url='https://cdn.discordapp.com/attachments/794323054317928478/794385737235562506/image.png')

            usersentembed.add_field(name='Author:', value=f'<@{message.author.id}>')
            usersentembed.add_field(name='Message:', value=f'{arg}')

            usersentembed.add_field(name='Channel:', value=f'<#{SERVER_GENERAL}>')
            await usersend.send(embed=usersentembed)
            await user2send.send(embed=usersentembed)
            print(f'\n\nIMPORTANT\n{message.author} sent "{arg}" in {channelsend}.\nIMPORTANT\n')
        else:
            usersentembed = discord.Embed(colour=randomhex(hex))

            usersentembed.set_footer(text='User tried to send')

            usersentembed.set_author(name='b1nzy', icon_url='https://cdn.discordapp.com/attachments/794323054317928478/794385737235562506/image.png')

            usersentembed.add_field(name='Author:', value=f'<@{message.author.id}>')
            usersentembed.add_field(name='Message:', value=f'{arg}')

            usersentembed.add_field(name='Channel:', value=f'<#{SERVER_GENERAL}>')
            await usersend.send(embed=usersentembed)
            await user2send.send(embed=usersentembed)
            print(f'\n\nIMPORTANT\n{message.author} tried to send "{arg}" in {channelsend}.\nIMPORTANT\n')

    @commands.command(hidden=True)
    async def botecho(self, ctx, *, arg):
        """echoes your input in bot commands of rocketcat"""
        message = ctx.message
        # add your user ID to usersend to be notified when someone uses the command.
        usersend = self.bot.get_user(YOUR_USER_ID)
        # add a friend's user ID below for them to be notified when someone uses the command.
        user2send = self.bot.get_user(FRIEND_USER_ID)
        # add the channel ID for the channel you would like the message to be sent in below
        channelsend = self.bot.get_channel(SERVER_BOT_COMMANDS)
        # IMPORTANT: if you do not add your user ID here and your friend's user ID below, then the command will not work.
        # if you do not want to add a friend, remove the comment on the line below, delete the if statement that says "(YOUR_USER_ID, FRIEND_USER_ID):" and remove all instances of "user2send"
        # if message.author.id = YOUR_USER_ID
        if message.author.id in (YOUR_USER_ID, FRIEND_USER_ID):
            await channelsend.send(f'{arg}')
            # the code below this comment is irrelevant, the only thing needed is the await channel.send and if you want you could keep that else and put a return statement after it.
            usersentembed = discord.Embed(colour=randomhex(hex))

            usersentembed.set_footer(text='User sent')

            usersentembed.set_author(name='b1nzy', icon_url='https://cdn.discordapp.com/attachments/794323054317928478/794385737235562506/image.png')

            usersentembed.add_field(name='Author:', value=f'<@{message.author.id}>')
            usersentembed.add_field(name='Message:', value=f'{arg}')

            usersentembed.add_field(name='Channel:', value=f'<#{SERVER_BOT_COMMANDS}>')
            await usersend.send(embed=usersentembed)
            await user2send.send(embed=usersentembed)
            print(f'\n\nIMPORTANT\n{message.author} sent "{arg}" in {channelsend}.\nIMPORTANT\n')
        else:
            usersentembed = discord.Embed(colour=randomhex(hex))

            usersentembed.set_footer(text='User tried to send')

            usersentembed.set_author(name='b1nzy', icon_url='https://cdn.discordapp.com/attachments/794323054317928478/794385737235562506/image.png')

            usersentembed.add_field(name='Author:', value=f'<@{message.author.id}>')
            usersentembed.add_field(name='Message:', value=f'{arg}')

            usersentembed.add_field(name='Channel:', value=f'<#{SERVER_BOT_COMMANDS}>')
            await usersend.send(embed=usersentembed)
            await user2send.send(embed=usersentembed)
            print(f'\n\nIMPORTANT\n{message.author} tried to send "{arg}" in {channelsend}.\nIMPORTANT\n')

    #   command to receive suggestions because I can't think of new features for my bot.
    @commands.command(aliases=['suggestion'])
    async def suggest(self, ctx, *, suggestion):
        """submit ideas for new features!"""
        message = ctx.message
        user = self.bot.get_user(YOUR_USER_ID)
        guild = ctx.message.guild
        f = open("cogs/suggestions.txt", "a")
        embed = discord.Embed(colour=randomhex(hex))
        embed.add_field(name=f'**Author:** <@{message.author.id}> - {message.author.id}', value=f'\uFEFF')
        embed.add_field(name=f'**Server:** {guild.name} - {guild.id}', value=f'\uFEFF')
        embed.add_field(name=f'**Suggestion:** {suggestion}', value=f'\uFEFF')
        await user.send(embed=embed)
        await ctx.send(f'Your submission has been recieved, I may contact you with some questions if it is accepted.')
        f.write(f'{message.author} - <@{message.author.id}> suggested: "{suggestion}"\n')

    # credits for the bot, sends embed containing anybody that helped to directly, or indirectly, make b1nzyBot.
    @commands.command(aliases=['credit'])
    async def credits(self, ctx):
        """displays the bot's credits. included is anybody who helped me make this bot and any code that was copied from other bots."""
        embed = discord.Embed(title='Credits',
                              description="credits, anybody listed here helped me either directly or indirectly in the making of this bot.",
                              colour=randomhex(hex))
        embed.set_author(name='B1nzyBot',
                         url='https://takeb1nzyto.space',
                         icon_url='https://cdn.discordapp.com/attachments/794323054317928478/794385737235562506/image.png')

        embed.add_field(name='Inspiration', value='[Click here](https://github.com/twotxh)')
        embed.add_field(name='More inspiration', value='[Click here](https://takeb1nzyto.space)')

        await ctx.send(embed=embed)

    @commands.command(hidden=True)
    @commands.is_owner()
    async def botstats(self, ctx):
        """sends fake bot stats cuz I don't know how to make it send real ones and it looks really cool so why not."""
        await ctx.send("```css\n┌───────────────────────────────────────────┐\n│Info and stats                             │\n├─────────────────────┬─────────────────────┤\n│Bot version          │v2.7.10              │\n│Library version      │JDA 3.8.3_d7c83d3    │\n│JVM version          │11.0.7+10            │\n│                     │(AdoptOpenJDK)       │\n│Available guilds     │12723                │\n│Shard                │Shard [6 / 15] (837) │\n│Uptime               │32:46                │\n│Events received      │123148               │\n│Commands executed    │120243               │\n│Audio connections    │0                    │\n│(curr. shard)        │                     │\n│CPU usage            │0%                   │\n│Memory usage         │Free: 10161MB        │\n│                     │Allocated: 12288MB   │\n│                     │Used: 2127MB         │\n│                     │Last GC: ???         │\n└─────────────────────┴─────────────────────┘\n```")

    # sends invite link for b1nzyBot.
    @commands.command()
    async def invite(self, ctx):
        """sends an invite link for b1nzyBot."""
        await ctx.send('https://discord.com/api/oauth2/authorize?client_id=788978875287470091&permissions=1916267615&redirect_uri=https%3A%2F%2Fdiscord.com%2Fapi%2Foauth2%2Fauthorize&scope=bot%20applications.commands')

    # useless command used to index emotes in servers the bot is in for use in messages.
    @commands.command(hidden=True)
    @commands.is_owner()
    async def emoteids(self, ctx):
        """prints all the emote details of a server in the console."""
        await ctx.channel.purge(limit=1)
        print(f'{ctx.guild.emojis}')

    @commands.command(aliases=['code', 'opensource', 'sourcecode', 'source'])
    async def github(self, ctx):
        await ctx.send('https://github.com/jbsparrow/b1nzyBotPy')

    @commands.Cog.listener()
    async def on_message(self, message):
        messageguild = message.guild.id
        guildname = message.guild.name

        if not messageguild == 110373943822540800:
            channelname = message.channel
            tz = timezone('US/Eastern')
            c_time = datetime.datetime.now(tz)
            authorid = message.author.id
            user = message.author.name
            msg = message.content

            if message.author == self.bot.user:
                return

            #   Logging in different colours because it looks nice and makes it easier to scan through messages from different servers and users faster.
            cprint(f"<{c_time.strftime('%I:%M%p')}>", 'cyan', end='')
            cprint(f" guild:{guildname}", 'green', end='')
            cprint(f" channel:#{channelname}", 'blue', end='')
            cprint(f" {user}(id:{authorid}):", 'yellow', end='')
            cprint(f" {msg}", 'magenta')


#   set up all command category
def setup(bot):
    bot.add_cog(Miscellaneous(bot))
