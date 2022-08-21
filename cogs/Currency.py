import datetime
from discord.ext import commands
import discord
import json
import random
from termcolor import cprint
intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)
currenttime = datetime.datetime.now()
guild = discord.guild
amounts = {}


def _save():
    with open('amounts.json', 'w') as f:
        json.dump(amounts, f)


class Currency(commands.Cog):
    # this category works, but I can't get opus to work so this is pretty useless.

    def __init__(self, bot):
        self.bot = bot

    # says when bot is online
    @commands.Cog.listener()
    async def on_ready(self):
        print('Currency cog is online.\n')
        global amounts
        try:
            with open('amounts.json') as f:
                amounts = json.load(f)
                cprint('amounts.json', 'yellow', end='')
                print(' is loaded\n')
        except FileNotFoundError:
            cprint("Could not load amounts.json", 'red')
            amounts = {}

    @commands.command(pass_context=True, aliases=['bal'])
    async def balance(self, ctx):
        id = str(ctx.message.author.id)
        if id in amounts:
            await ctx.send(f"You have ${amounts[id]} in the bank")
            _save()
        elif id not in amounts:
            amounts[id] = 100
            await ctx.send(f"You have ${amounts[id]} in the bank")
            _save()

    @commands.cooldown(1, 30, commands.BucketType.user)
    @commands.command(pass_context=True)
    async def work(self, ctx):
        id = str(ctx.message.author.id)
        income = int(random.randint(75, 150))
        if id in amounts:
            amounts[id] = amounts[id] + income
            await ctx.send(f'You shook your ass on stage and got **${income}**. Your total is now **${amounts[id]}**.')
            _save()
        elif id not in amounts:
            amounts[id] = 100 + income
            await ctx.send(f'You shook your ass on stage and got **${income}**. Your total is now **${amounts[id]}**.')
            _save()

    @work.error
    async def work_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"This command is on cooldown for {error.retry_after} more seconds.")
        else:
            raise error

    @commands.command(pass_context=True, aliases=['give', 'pay'])
    async def transfer(self, ctx, other: discord.Member, amount: int):
        primary_id = str(ctx.message.author.id)
        other_id = str(other.id)
        if primary_id not in amounts:
            await ctx.send("You do not have an account")
            _save()
        elif other_id not in amounts:
            await ctx.send("The other party does not have an account")
            _save()
        elif amounts[primary_id] < amount:
            await ctx.send("You cannot afford this transaction")
            _save()
        else:
            amounts[primary_id] -= amount
            amounts[other_id] += amount
            await ctx.send("Transaction complete")
        _save()

    @commands.is_owner()
    @commands.command(hidden=True)
    async def save(self):
        _save()


def setup(bot):
    bot.add_cog(Currency(bot))
