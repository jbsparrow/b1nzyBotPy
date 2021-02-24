from discord.ext import commands
import discord

from cogs.Currency import _save

client = discord.Client()


class OwnerCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Owner commands cog is online.\n')

    #   Command to load cogs, hidden so nobody can see it.
    @commands.command(name='load', hidden=True)
    #   is_owner check to see if the user invoking the command is the bot owner.
    @commands.is_owner()
    async def cogload(self, ctx, *, cog: str):
        """Command which Loads a Module.
        must be loaded like: cogs.owner"""

        try:
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')

    #   Command to unload cogs, hidden so nobody can see it.
    @commands.command(name='unload', hidden=True)
    #   is_owner check to see if the user invoking the command is the bot owner.
    @commands.is_owner()
    async def cogunload(self, ctx, *, cog: str):
        """Command which Unloads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        try:
            self.bot.unload_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')

    #   Command to reload cogs, hidden so nobody can see it.
    @commands.command(name='reload', hidden=True)
    #   is_owner check to see if the user invoking the command is the bot owner.
    @commands.is_owner()
    async def cogreload(self, ctx, *, cog: str):
        """Command which Reloads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        try:
            self.bot.unload_extension(cog)
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')

    #   Command to shut down b1nzyBot, hidden so nobody can see it.
    @commands.command(name='shutdown', hidden=True, aliases=['logoff', 'signoff', 'signout'])
    #   is_owner check to see if the user invoking the command is the bot owner.
    @commands.is_owner()
    async def logoff(self, ctx):
        _save()
        user = self.bot.get_user(329377582476951552)
        #   Send logs as a backup.
        await user.send(file=discord.File("cogs/logs.txt"))
        await user.send(file=discord.File("cogs/suggestions.txt"))
        await user.send('logging off bot.')
        await self.bot.close()



def setup(bot):
    bot.add_cog(OwnerCog(bot))
