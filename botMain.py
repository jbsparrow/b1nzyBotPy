from itertools import cycle
import random
import discord
import os
from discord.ext import commands, tasks
from discord_slash import SlashCommand
from dotenv import load_dotenv
from cogs.Currency import _save


load_dotenv()

YOUR_USER_ID = int(os.getenv('YOUR_USER_ID'))
SERVER_GENERAL = int(os.getenv('SERVER_GENERAL'))
TOKEN = os.getenv('TOKEN')

intents = discord.Intents.all()
Guild = discord.guild.Guild


def get_prefix(bot, message):

    prefixes = ['$', 'b1nzy ']

    # prefix stuff, allows mentioning the bot as a prefix
    return commands.when_mentioned_or(*prefixes)(bot, message)


bot = commands.Bot(command_prefix=get_prefix, intents=intents.all(), case_insensitive=True)
slash = SlashCommand(bot, sync_commands=True)

bot.remove_command('help')


# loads cogs upon bot start.
initial_extensions = ['cogs.Miscellaneous',
                      'cogs.Utilities',
                      'cogs.Currency',
                      'cogs.Members',
                      'cogs.Simple',
                      'cogs.Voice',
                      'cogs.Owner',
                      'cogs.NSFW',
                      'cogs.Help',
                      'cogs.Fun']


if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)


client = discord.Client(intents=intents)
# list of bot statuses, some custom, most from discord loading messages, most of which have been removed :(
status = cycle(['Error 404: Joke not found', 'Is this thing on...?', 'I solemnly swear that I am up to no good', 'Baby Eating Simulator - Deluxe Edition', '[A MEME]', 'Insert coin to continue', 'Scaling Bananas...', 'Cheat code activated', 'Generating terrain...', 'Resurrecting dead memes...', 'Preparing the Chungus-inator...', 'Removing pen from pineapple', 'Dispatching carrier pigeons', 'Preparing Final Form', 'Pressing random buttons', 'Rushing B', 'Clicking circles (to the beat!)', 'Building Lore', 'Activating Witch Time...', 'Watching Https://twitch.tv/JoocyLad', 'https://dis.gd/threads'])


# starts loops and prints in terminal that b1nzyBot is live.
@bot.event
async def on_ready():
    change_status.start()
    death.start()
    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n\n{bot.user} has connected to Discord and has a ping of {round(bot.latency * 1000)}ms.\n')


# status change loop
@tasks.loop(seconds=30)
async def change_status():
    await bot.change_presence(activity=discord.Game(next(status)))


# random user died loop
@tasks.loop(hours=3)
async def death():
    # put the Channel ID of the channel you want death messages to send in below.
    channel = bot.get_channel(SERVER_GENERAL)
    user = [member.id for member in channel.guild.members]
    autopsy = [f'<@{random.choice(user)}> died from stupidity.', f'<@{random.choice(user)}> died from embarrassment.', f'<@{random.choice(user)}> got hit by a frog and died from sliminess.', f'<@{random.choice(user)}> fell off a cliff.', f'<@{random.choice(user)}> died from eating too many children.', f'<@{random.choice(user)}> died from not wearing a mask.', f'<@{random.choice(user)}> was poisoned by <@{random.choice(user)}>.', f'<@{random.choice(user)}> had all their blood drained by <@{random.choice(user)}>.', f'<@{random.choice(user)}> was suffocated by <@{random.choice(user)}>.', f'<@{random.choice(user)}> was decapitated.', f'<@{random.choice(user)}> was publically executed.', f'was poisoned by <@{random.choice(user)}>.', f'<@{random.choice(user)}> ripped <@{random.choice(user)}>\'s head off.', f'<@{random.choice(user)}> massacred <@{random.choice(user)}>, <@{random.choice(user)}>, <@{random.choice(user)}>, <@{random.choice(user)}>, <@{random.choice(user)}>, and <@{random.choice(user)}>.', f'<@{random.choice(user)}> snapped <@{random.choice(user)}> into {random.randint(3, 7)} pieces like a twig.']
    await channel.send(f'{random.choice(autopsy)}')
    _save()


#   Slash commands
#   Command that does simple math.
@slash.slash(name='math', description='Does simple math, Allowed operators: +, -, *, /')
async def _math(ctx, num1, operator, num2):
    #   Check for operator, can only do simple math, by simple math, that means no square roots, but it can do math with extremely large numbers.
    if operator == "+":
        num1 = int(num1)
        num2 = int(num2)
        msg = num1+num2
        await ctx.send(str(msg))
    if operator == "-":
        num1 = int(num1)
        num2 = int(num2)
        msg = num1-num2
        await ctx.send(str(msg))
    if operator == "*":
        num1 = int(num1)
        num2 = int(num2)
        msg = num1*num2
        await ctx.send(str(msg))
    if operator == "/":
        num1 = int(num1)
        num2 = int(num2)
        msg = num1/num2
        await ctx.send(str(msg))


bot.run(f'{TOKEN}', bot=True, reconnect=True)
