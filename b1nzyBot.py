from itertools import cycle
import random
import os
from dotenv import load_dotenv
import discord
from discord.ext import commands, tasks
intents = discord.Intents.default()
intents.members = True
Guild = discord.guild.Guild

load_dotenv()
PRIVATE_BOT_TOKEN = os.getenv('PRIVATE_BOT_TOKEN')


def get_prefix(bot, message):



    prefixes = ['$', 'b1nzy ']

    # prefix stuff, allows mentioning the bot as a prefix
    return commands.when_mentioned_or(*prefixes)(bot, message)

# loads cogs upon bot start.
initial_extensions = ['cogs.Miscellaneous',
                      'cogs.Utilities',
                      'cogs.Members',
                      'cogs.Simple',
                      'cogs.Voice',
                      'cogs.Owner',
                      'cogs.Fun']

bot = commands.Bot(command_prefix=get_prefix, intents=intents)



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
    logs.start()
    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n\n{bot.user} has connected to Discord and has a ping of {round(bot.latency * 1000)}ms.\n')


# status change loop
@tasks.loop(seconds=30)
async def change_status():
    await bot.change_presence(activity=discord.Game(next(status)))


# random user died loop
@tasks.loop(hours=3)
async def death():
    autopsy = ['died from stupidity', 'died from embarrassment', 'got hit by a frog and died from sliminess', 'fell off a cliff', 'died from eating too many children', 'died from not wearing a mask']
# put the channel id of the channel you want death messages to send in below.
    channel = bot.get_channel(788803275155177502)
    user = [member.id for member in channel.guild.members]
    await channel.send(f'<@{random.choice(user)}> {random.choice(autopsy)}.')


# save suggestions and logs loop
@tasks.loop(hours=24)
async def logs():
# put your user ID below
    user = bot.get_user(329377582476951552)
    await user.send(file=discord.File("cogs/suggestions.txt"))


bot.run('PRIVATE_BOT_TOKEN', bot=True, reconnect=True)
