import discord
from discord.ext import commands


class Members(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    #   say when cog is online
    @commands.Cog.listener()
    async def on_ready(self):
        print('Members cog is online.\n')

    #   Tells the user when a member joined.
    @commands.command()
    @commands.guild_only()
    async def joined(self, ctx, *, member: discord.Member):
        """says when a member joined"""
        await ctx.send(f'{member.display_name} joined on {member.joined_at}')

    #   Shows the user's top role in the role heirarchy.
    @commands.command(name='top_role', aliases=['toprole'])
    @commands.guild_only()
    async def show_toprole(self, ctx, *, member: discord.Member = None):
        """command that shows the members Top Role."""
        #   If no member is specified, use the command invoker.
        if member is None:
            member = ctx.author
        await ctx.send(f'The top role for {member.display_name} is {member.top_role.name}')

    #   Checks the permissions of the specified user.
    @commands.command(name='perms', aliases=['perms_for', 'permissions'])
    @commands.guild_only()
    async def check_permissions(self, ctx, *, member: discord.Member = None):
        """Command that checks a members Guild Permissions.
        If member is not provided, the author will be checked."""
        #   If no user is specified, use the command invoker.
        if not member:
            member = ctx.author
        # checks for perms
        perms = '\n'.join(perm for perm, value in member.guild_permissions if value)
        embed = discord.Embed(title='Permissions for:', description=ctx.guild.name, colour=member.colour)
        embed.set_author(icon_url=member.avatar_url, name=str(member))
        # shit that allows me to have an empty space
        embed.add_field(name='\uFEFF', value=perms)
        await ctx.send(content=None, embed=embed)


def setup(bot):
    bot.add_cog(Members(bot))
