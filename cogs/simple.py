import discord
from discord.ext import commands


class Simple(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    #   prints in console that the cog is online.
    @commands.Cog.listener()
    async def on_ready(self):
        print('Simple cog is online.\n')

    #   Command that does simple math.
    @commands.command()
    async def math(self, ctx, num1, operator, num2):
        """Does simple math."""
        #   Check for operator, can only do simple math, by simple math, that means no square roots, but it can do math with extremely large numbers.
        if operator == "+":
            num1 = int(num1)
            num2 = int(num2)
            msg = num1+num2
            print(msg)
            await ctx.send(str(msg))
        if operator == "-":
            num1 = int(num1)
            num2 = int(num2)
            msg = num1-num2
            print(msg)
            await ctx.send(str(msg))
        if operator == "*":
            num1 = int(num1)
            num2 = int(num2)
            msg = num1*num2
            print(msg)
            await ctx.send(str(msg))
        if operator == "/":
            num1 = int(num1)
            num2 = int(num2)
            msg = num1/num2
            print(msg)
            await ctx.send(str(msg))

    #   Prints in console when a user is banned from a server the bot is in.
    @commands.Cog.listener()
    async def on_member_ban(self, guild, user):
        print(f'{user.name}-{user.id} was banned from {guild.name}-{guild.id}')

    #   Prints in console when a member of the guild is kicked.
    @commands.Cog.listener()
    async def on_member_kick(self, guild, user):
        print(f'{user.name}-{user.id} was kicked from {guild.name}-{guild.id}')

    #   Prints in console when a user is unbanned from a server the bot is in.
    @commands.Cog.listener()
    async def on_member_unban(self, guild, user):
        print(f'{user.name}-{user.id} was unbanned from {guild.name}-{guild.id}')


def setup(bot):
    bot.add_cog(Simple(bot))
