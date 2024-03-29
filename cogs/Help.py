import discord
from discord.ext import commands
from cogs.Fun import randomhex

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)


class Help(commands.Cog):

    # useless but nice commands.
    def __init__(self, bot):
        self.bot = bot

    # says when cog is online
    @commands.Cog.listener()
    async def on_ready(self):
        print('Help cog is online.\n')

    #   Help command
    @commands.group()
    async def help(self, ctx):
        if ctx.invoked_subcommand is None:
            embed = discord.Embed(colour=randomhex(), title='Categories')

            embed.add_field(name='Fun', value='\uFEFF', inline=False)
            embed.add_field(name='NSFW', value='\uFEFF', inline=False)
            embed.add_field(name='Voice', value='\uFEFF', inline=False)
            embed.add_field(name='Economy', value='\uFEFF', inline=False)
            embed.add_field(name='Moderation', value='\uFEFF', inline=False)
            embed.add_field(name='Miscellaneous', value='\uFEFF', inline=False)

            embed.set_footer(text='Use $help [category] to see a list of all commands in that category.\nUse $help [command] for command usage and aliases.')
            await ctx.send(embed=embed)

#   Fun Category

    @help.command()
    async def fun(self, ctx):
        embed = discord.Embed(colour=randomhex(), title='Fun')

        embed.add_field(name=f'\uFEFF', value=f'**$cat** - Sends a random cat picture!', inline=False)
        embed.add_field(name=f'\uFEFF', value=f'**$quote** - Sends a quote from a pre-selected list of quotes.', inline=False)
        embed.add_field(name=f'\uFEFF', value=f'**$quote2** - Sends a random quote.', inline=False)
        embed.add_field(name=f'\uFEFF', value=f'**$headpat** - Sends a headpat gif.', inline=False)
        embed.add_field(name=f'\uFEFF', value=f'**$hug** - Sends a hugging gif.', inline=False)
        embed.add_field(name=f'\uFEFF', value=f'**$kiss** - Sends a kissing gif.', inline=False)
        embed.add_field(name=f'\uFEFF', value=f'**$slap** - Sends a slapping gif.', inline=False)
        embed.add_field(name=f'\uFEFF', value=f'**$topic** - Sends a topic of conversation.', inline=False)
        embed.add_field(name=f'\uFEFF', value=f'**$inspire** - Sends an AI generated inspirational quote.', inline=False)
        embed.add_field(name=f'\uFEFF', value=f'**$pokemon** - Sends a random pokemon picture.')
        embed.add_field(name=f'\uFEFF', value=f'**$rps** - Play rock paper scissors with b1nzy.', inline=False)
        embed.add_field(name=f'\uFEFF', value=f'**$coinflip** - Flips a coin, leave the input blank if you\'re not guessing the side.', inline=False)
        embed.add_field(name=f'\uFEFF', value=f'**$8ball** - Ask a yes/no question, and b1nzy will answer.', inline=False)
        embed.add_field(name=f'\uFEFF', value=f'**$uwu** - UwUizes your message.', inline=False)
        embed.add_field(name=f'\uFEFF', value=f'**$xuwu** - UwUizes your message but with a bit more ✨spice✨ to it.', inline=False)
        embed.add_field(name=f'\uFEFF', value=f'**$urban** - Look up your input on urban dictionary, if none is specified get a random word.', inline=False)
        embed.add_field(name=f'\uFEFF', value=f'**$insult** - Insults the specified user, if none is specified, insults you.', inline=False)
        embed.add_field(name=f'\uFEFF', value=f'**$achievement** - Makes your input into a minecraft achievement.', inline=False)
        embed.add_field(name=f'\uFEFF', value=f'**$edit** - Edits whatever you want onto an ugly background in the specified font. For extra ugliness it won\'t be centred.', inline=False)
        embed.add_field(name=f'\uFEFF', value=f'**$meme** - Sends a meme that\'s probably not very funny.', inline=False)

        embed.set_footer(text='Use $help [command] for command usage and aliases.')

        await ctx.send(embed=embed)

#   Fun Commands

    #   $cat
    @help.command(aliases=['cats', 'catpictures', 'catpicture', 'catpics', 'catpic'])
    async def cat(self, ctx):
        embed = discord.Embed(colour=randomhex(), title='**Command:** `cat`')

        embed.add_field(name=f'**Description:** Sends a random cat picture!', value='\uFEFF', inline=False)
        embed.add_field(name=f'**Usage:** `$cat`', value='\uFEFF', inline=False)
        embed.add_field(name=f'**Aliases:**', value='cats\ncatpic\ncatpics\ncatpicture\ncatpictures', inline=False)
        await ctx.send(embed=embed)

    #   $quote
    @help.command()
    async def quote(self, ctx):
        embed = discord.Embed(colour=randomhex(), title='**Command:** `quote`')

        embed.add_field(name=f'**Description:** Sends a quote from a pre-selected list of quotes.', value='\uFEFF',
                        inline=False)
        embed.add_field(name=f'**Usage:** `$quote`', value='\uFEFF', inline=False)
        await ctx.send(embed=embed)

    #   $quote2
    @help.command()
    async def quote2(self, ctx):
        embed = discord.Embed(colour=randomhex(), title='**Command:** `quote2`')

        embed.add_field(name=f'**Description:** Sends a random quote.', value='\uFEFF', inline=False)
        embed.add_field(name=f'**Usage:** `$quote2`', value='\uFEFF', inline=False)
        await ctx.send(embed=embed)

    #   $headpat
    @help.command()
    async def headpat(self, ctx):
        embed = discord.Embed(colour=randomhex(), title='**Command:** `headpat`')

        embed.add_field(name=f'**Description:** Sends a headpat gif.', value='\uFEFF', inline=False)
        embed.add_field(name=f'**Usage:** `$headpat`', value='\uFEFF', inline=False)
        await ctx.send(embed=embed)

    #   $hug
    @help.command()
    async def hug(self, ctx):
        embed = discord.Embed(colour=randomhex(), title='**Command:** `hug`')

        embed.add_field(name=f'**Description:** Sends a hugging gif.', value='\uFEFF', inline=False)
        embed.add_field(name=f'**Usage:** `$hug`', value='\uFEFF', inline=False)
        await ctx.send(embed=embed)

    #   $kiss
    @help.command()
    async def kiss(self, ctx):
        embed = discord.Embed(colour=randomhex(), title='**Command:** `kiss`')

        embed.add_field(name=f'**Command:** $kiss', value='\uFEFF', inline=False)
        embed.add_field(name=f'**Description:** Sends a kissing gif.', value='\uFEFF', inline=False)
        embed.add_field(name=f'**Usage:** `$kiss`', value='\uFEFF', inline=False)
        await ctx.send(embed=embed)

    #   $slap
    @help.command()
    async def slap(self, ctx):
        embed = discord.Embed(colour=randomhex(), title='**Command:** `slap`')

        embed.add_field(name=f'**Description:** Sends a slapping gif.', value='\uFEFF', inline=False)
        embed.add_field(name=f'**Usage:** `$slap`', value='\uFEFF', inline=False)
        await ctx.send(embed=embed)

    #   $topic
    @help.command()
    async def topic(self, ctx):
        embed = discord.Embed(colour=randomhex(), title='**Command:** `topic`')

        embed.add_field(name=f'**Description:** Sends a topic of conversation.', value='\uFEFF', inline=False)
        embed.add_field(name=f'**Usage:** `$topic`', value='\uFEFF', inline=False)
        await ctx.send(embed=embed)

    #   $inspire
    @help.command()
    async def inspire(self, ctx):
        embed = discord.Embed(colour=randomhex(), title='**Command:** `inspire`')

        embed.add_field(name=f'**Description:** Sends an AI generated inspirational quote.', value='\uFEFF',
                        inline=False)
        embed.add_field(name=f'**Usage:** `$inspire`', value='\uFEFF', inline=False)
        embed.add_field(name=f'**Aliases:**', value='inspiration\ninspireme', inline=False)
        await ctx.send(embed=embed)

    #   $pokemon
    @help.command()
    async def pokemon(self, ctx):
        embed = discord.Embed(colour=randomhex(), title='**Command:** `pokemon`')

        embed.add_field(name=f'**Description:** Sends a random pokemon.', value='\uFEFF', inline=False)
        embed.add_field(name=f'**Usage:** `$pokemon`', value='\uFEFF', inline=False)
        await ctx.send(embed=embed)

    #   $rps
    @help.command(aliases=['rockpaperscissors'])
    async def rps(self, ctx):
        embed = discord.Embed(colour=randomhex(), title='**Command:** `rps`')

        embed.add_field(
            name=f'**Description:** Play rock paper scissors with b1nzy.\nYou can use numbers 1-3 or words as your choice.\n1=rock, 2=paper, 3=scissors', value='\uFEFF', inline=False)
        embed.add_field(name=f'**Usage:** `$rps [choice]`', value='\uFEFF', inline=False)
        embed.add_field(name=f'**Aliases:**', value='rockpaperscissors', inline=False)
        await ctx.send(embed=embed)

    #   $coinflip
    @help.command(aliases=['flip', 'coin', '50/50', '5050'])
    async def coinflip(self, ctx):
        embed = discord.Embed(colour=randomhex(), title='**Command:** `coinflip`')

        embed.add_field(name=f'**Description:** Flips a coin, leave the input blank if you\'re not guessing the side.', value='\uFEFF', inline=False)
        embed.add_field(name=f'**Usage:** `$coinflip [side]`', value='\uFEFF', inline=False)
        embed.add_field(name=f'**Aliases:**', value='coin\nflip\n50/50\n5050', inline=False)
        await ctx.send(embed=embed)

    #   $8ball
    @help.command(aliases=['8ball'])
    async def eightball(self, ctx):
        embed = discord.Embed(colour=randomhex(), title='**Command:** `8ball`')

        embed.add_field(name=f'**Description:** Ask a yes/no question, and b1nzy will answer.', value='\uFEFF', inline=False)
        embed.add_field(name=f'**Usage:** `$8ball [question]`', value='\uFEFF', inline=False)
        embed.add_field(name=f'**Aliases:**', value='eightball', inline=False)
        await ctx.send(embed=embed)

    #   $uwu
    @help.command(aliases=['uwuize', 'owo', 'owoize'])
    async def uwu(self, ctx):
        embed = discord.Embed(colour=randomhex(), title='**Command:** `uwu`')

        embed.add_field(name=f'**Description:** UwUizes your message.', value='\uFEFF', inline=False)
        embed.add_field(name=f'**Usage:** `$uwu [input]`', value='\uFEFF', inline=False)
        embed.add_field(name=f'**Aliases:**', value='uwuize\nowo\nowoize', inline=False)
        await ctx.send(embed=embed)

    #   $urban
    @help.command(aliases=['ud', 'urbandictionary', 'urbans', 'urbandict'])
    async def urban(self, ctx):
        embed = discord.Embed(colour=randomhex(), title='**Command:** `urban`')

        embed.add_field(name=f'**Description:** Look up your input on urban dictionary.', value='\uFEFF', inline=False)
        embed.add_field(name=f'**Usage:** `$urban [input]`', value='\uFEFF', inline=False)
        embed.add_field(name=f'**Aliases:**', value='urbandictionary\nud', inline=False)
        await ctx.send(embed=embed)

    #   $insult
    @help.command()
    async def insult(self, ctx):
        embed = discord.Embed(colour=randomhex(), title='**Command:** `insult`')

        embed.add_field(name=f'**Description:** Insults the specified user, if noone is specified, insults you.', value='\uFEFF', inline=False)
        embed.add_field(name=f'**Usage:** `$insult`', value='\uFEFF', inline=False)
        await ctx.send(embed=embed)

    #   $achievement
    @help.command()
    async def achievement(self, ctx):
        embed = discord.Embed(colour=randomhex(), title='**Command:** `achievement`')

        embed.add_field(name=f'**Description:** Makes your input into a minecraft achievement.', value='\uFEFF', inline=False)
        embed.add_field(name=f'**Usage:** `$achievement <achievement>`', value='\uFEFF', inline=False)
        embed.add_field(name=f'**Aliases:**', value='achievment\nmc\nminecraft', inline=False)
        embed.set_footer(text='This command is a WIP so your achievement will probably look ugly /:')
        await ctx.send(embed=embed)

    #   $edit
    @help.command()
    async def edit(self, ctx):
        embed = discord.Embed(colour=randomhex(), title='**Command:** `edit`')

        embed.add_field(name=f'**Description:** Edits whatever you want onto an ugly background in the specified font. For extra ugliness it won\'t be centred.', value='\uFEFF', inline=False)
        embed.add_field(name=f'**Usage:** `$edit <font> <content>`', value='\uFEFF', inline=False)
        embed.set_footer(text='This command is a WIP so your edit will probably look ugly')
        await ctx.send(embed=embed)

    #   $meme
    @help.command()
    async def meme(self, ctx):
        embed = discord.Embed(colour=randomhex(), title='**Command:** `meme`')

        embed.add_field(name=f'**Description:** Sends a meme that\'s probably not very funny.', value='\uFEFF', inline=False)
        embed.add_field(name=f'**Usage:** `$meme`', value='\uFEFF', inline=False)
        await ctx.send(embed=embed)

#   NSFW Category

    #   NSFW
    @help.command()
    async def nsfw(self, ctx):
        embed = discord.Embed(colour=randomhex(), title='NSFW')

        embed.add_field(name=f'\uFEFF', value=f'**$spreading** - Sends a spreading picture.', inline=False)
        embed.add_field(name=f'\uFEFF', value=f'**$gangbang** - Sends a gangbang picture.', inline=False)
        embed.add_field(name=f'\uFEFF', value=f'**$titfuck** - Sends a titfuck picture.', inline=False)
        embed.add_field(name=f'\uFEFF', value=f'**$ahegao** - Sends an ahegao picture.', inline=False)
        embed.add_field(name=f'\uFEFF', value=f'**$hentai** - Sends a hentai picture.', inline=False)
        embed.add_field(name=f'\uFEFF', value=f'**$ubani** - Sends an ubani picture.', inline=False)
        embed.add_field(name=f'\uFEFF', value=f'**$bunny** - Sends a bunny suit picture.', inline=False)
        embed.add_field(name=f'\uFEFF', value=f'**$anal** - Sends an anal picture.', inline=False)
        embed.add_field(name=f'\uFEFF', value=f'**$tits** - Sends a titty picture.', inline=False)
        embed.add_field(name=f'\uFEFF', value=f'**$trap** - Sends a trap/femboy picture.', inline=False)
        embed.add_field(name=f'\uFEFF', value=f'**$neko** - Sends a neko picture.', inline=False)
        embed.add_field(name=f'\uFEFF', value=f'**$ass** - Sends an ass picture.', inline=False)

        embed.set_footer(text='Use $help [command] for command usage and aliases.')

        await ctx.send(embed=embed)

#   NSFW Commands

    #   spreading
    @help.command(aliases=['spread', 'eagle', 'americaneagle', 'spreaded'])
    async def spreading(self, ctx):
        embed = discord.Embed(colour=randomhex(), title='**Command:** `spreading`')

        embed.add_field(name=f'**Description:** Sends a picture of someone spreading.', value='\uFEFF', inline=False)
        embed.add_field(name=f'**Usage:** `$spreading`', value='\uFEFF', inline=False)
        await ctx.send(embed=embed)

    #   gangbang
    @help.command(aliases=['banggang'])
    async def gangbang(self, ctx):
        embed = discord.Embed(colour=randomhex(), title='**Command:** `gangbang`')

        embed.add_field(name=f'**Description:** Sends a gangbang picture.', value='\uFEFF', inline=False)
        embed.add_field(name=f'**Usage:** `$gangbang`', value='\uFEFF', inline=False)
        await ctx.send(embed=embed)

    #   titfuck
    @help.command(aliases=['boobjob', 'tittyfuck', 'titdick', 'dicktit', 'titdicks', 'dicktits'])
    async def titfuck(self, ctx):
        embed = discord.Embed(colour=randomhex(), title='**Command:** `titfuck`')

        embed.add_field(name=f'**Description:** Sends a boobjob picture.', value='\uFEFF', inline=False)
        embed.add_field(name=f'**Usage:** `$titfuck`', value='\uFEFF', inline=False)
        embed.add_field(name=f'**Aliases:**', value='boobjob\ntittyfuck', inline=False)
        await ctx.send(embed=embed)

    #   ahegao
    @help.command(aliases=['aheago', 'ahegaos', 'aheagos'])
    async def ahegao(self, ctx):
        embed = discord.Embed(colour=randomhex(), title='**Command:** `ahegao`')

        embed.add_field(name=f'**Description:** Sends an ahegao picture.', value='\uFEFF', inline=False)
        embed.add_field(name=f'**Usage:** `$ahegao`', value='\uFEFF', inline=False)
        await ctx.send(embed=embed)

    #   hentai
    @help.command(aliases=['hentais'])
    async def hentai(self, ctx):
        embed = discord.Embed(colour=randomhex(), title='**Command:** `hentai`')

        embed.add_field(name=f'**Description:** Sends a hentai picture.', value='\uFEFF', inline=False)
        embed.add_field(name=f'**Usage:** `$hentai`', value='\uFEFF', inline=False)
        await ctx.send(embed=embed)

    #   ubani
    @help.command(aliases=['ubanis'])
    async def ubani(self, ctx):
        embed = discord.Embed(colour=randomhex(), title='**Command:** `ubani`')

        embed.add_field(name=f'**Description:** Sends an ubani picture.', value='\uFEFF', inline=False)
        embed.add_field(name=f'**Usage:** `$ubani`', value='\uFEFF', inline=False)
        await ctx.send(embed=embed)

    #   bunny
    @help.command(aliases=['bunnies', 'bunnysuit', 'bunnygirl', 'bunnygirlsuit', 'bunnysuitgirl'])
    async def bunny(self, ctx):
        embed = discord.Embed(colour=randomhex(), title='**Command:** `bunny`')

        embed.add_field(name=f'**Description:** Sends a bunny suit picture.', value='\uFEFF', inline=False)
        embed.add_field(name=f'**Usage:** `$bunny`', value='\uFEFF', inline=False)
        embed.add_field(name=f'**Aliases:**', value='bunnies\nbunnysuit\nbunnygirl', inline=False)
        await ctx.send(embed=embed)

    #   anal
    @help.command(aliases=['analsex', 'buttfuck', 'buttstuff'])
    async def anal(self, ctx):
        embed = discord.Embed(colour=randomhex(), title='**Command:** `anal`')

        embed.add_field(name=f'**Description:** Sends an anal picture.', value='\uFEFF', inline=False)
        embed.add_field(name=f'**Usage:** `$anal`', value='\uFEFF', inline=False)
        await ctx.send(embed=embed)

    #   tits
    @help.command(aliases=['boobs', 'titties', 'honkers', 'tit', 'boob'])
    async def tits(self, ctx):
        embed = discord.Embed(colour=randomhex(), title='**Command:** `tits`')

        embed.add_field(name=f'**Description:** Sends a titty picture.', value='\uFEFF', inline=False)
        embed.add_field(name=f'**Usage:** `$tits`', value='\uFEFF', inline=False)
        embed.add_field(name=f'**Aliases:**', value='boobs\ntitties', inline=False)
        await ctx.send(embed=embed)

    #   trap
    @help.command(aliases=['traps', 'femboy', 'femboys'])
    async def trap(self, ctx):
        embed = discord.Embed(colour=randomhex(), title='**Command:** `trap`')

        embed.add_field(name=f'**Description:** Sends a trap picture.', value='\uFEFF', inline=False)
        embed.add_field(name=f'**Usage:** `$trap`', value='\uFEFF', inline=False)
        embed.add_field(name=f'**Aliases:**', value='traps\nfemboy\nfemboys', inline=False)
        await ctx.send(embed=embed)

    #   neko
    @help.command(aliases=['nekos'])
    async def neko(self, ctx):
        embed = discord.Embed(colour=randomhex(), title='**Command:** `neko`')

        embed.add_field(name=f'**Description:** Sends a neko picture.', value='\uFEFF', inline=False)
        embed.add_field(name=f'**Usage:** `$neko`', value='\uFEFF', inline=False)
        await ctx.send(embed=embed)

    #   ass
    @help.command(aliases=['booty', 'asscheeks', 'bootycheeks', 'dumptruck', 'badonkadonk'])
    async def ass(self, ctx):
        embed = discord.Embed(colour=randomhex(), title='**Command:** `ass`')

        embed.add_field(name=f'**Description:** Sends a booty picture.', value='\uFEFF', inline=False)
        embed.add_field(name=f'**Usage:** `$ass`', value='\uFEFF', inline=False)
        embed.add_field(name=f'**Aliases:**', value='booty', inline=False)
        await ctx.send(embed=embed)

#   Miscellaneous Category

    @help.command(aliases=['misc', 'miscilleanous', 'misclanous', 'miscelanous', 'miscellanous', 'miscellanious', 'miscelaneous'])
    async def miscellaneous(self, ctx):
        embed = discord.Embed(colour=randomhex(), title='Miscellaneous')

        embed.add_field(name=f'\uFEFF', value='**$suggest** - Suggest new features and maybe they\'ll get added. <:smiling:795774009136513084>', inline=False)
        embed.add_field(name=f'\uFEFF', value='**$joined** - Shows when a member joined the server.', inline=False)
        embed.add_field(name=f'\uFEFF', value='**$toprole** - Shows a member\'s highest role.', inline=False)
        embed.add_field(name=f'\uFEFF', value='**$perms** - Shows the specified member\'s permissions.', inline=False)
        embed.add_field(name=f'\uFEFF', value='**$rand** - Chooses a random number between the min and max that you specify.', inline=False)
        embed.add_field(name=f'\uFEFF', value='**$translate** - Translates the inputted text to english.', inline=False)
        embed.add_field(name=f'\uFEFF', value='**$math** - Does math. Can only do simple operations (+, -, /, and *).', inline=False)
        embed.add_field(name=f'\uFEFF', value='**$ping** - Sends b1nzy\'s ping.', inline=False)
        embed.add_field(name=f'\uFEFF', value='**$invite** - Sends b1nzy\'s invite link.', inline=False)
        embed.add_field(name=f'\uFEFF', value='**$credits** - Who helped me make b1nzyBot.', inline=False)
        embed.add_field(name=f'\uFEFF', value='**$github** - b1nzyBot\'s source code.', inline=False)
        embed.add_field(name=f'\uFEFF', value='**$snipe** - Shows the last deleted message in the current channel.', inline=False)
        embed.add_field(name=f'\uFEFF', value='**$editsnipe** - Shows the last edited message in the current channel.', inline=False)
        embed.add_field(name=f'\uFEFF', value='**$suicide** - Sends a list of suicide hotlines.', inline=False)

        embed.set_footer(text='Use $help [command] for command usage and aliases.')

        await ctx.send(embed=embed)

#   Miscellaneous Commands

    #   $suggest
    @help.command()
    async def suggest(self, ctx):
        embed = discord.Embed(colour=randomhex(), title='**Command:** `suggest`')

        embed.add_field(name=f'**Description:** Suggest new features and maybe they\'ll get added. <:smiling:795774009136513084>', value='\uFEFF', inline=False)
        embed.add_field(name=f'**Usage:** `$suggest [suggestion]`', value='\uFEFF', inline=False)
        await ctx.send(embed=embed)

    #   $joined
    @help.command()
    async def joined(self, ctx):
        embed = discord.Embed(colour=randomhex(), title='**Command:** `joined`')

        embed.add_field(name=f'**Description:** Shows when a member joined the server.', value='\uFEFF', inline=False)
        embed.add_field(name=f'**Usage:** `$joined [member]`', value='\uFEFF', inline=False)
        await ctx.send(embed=embed)

    #   $toprole
    @help.command(aliases=['top_role', 'show_toprole'])
    async def toprole(self, ctx):
        embed = discord.Embed(colour=randomhex(), title='**Command:** `toprole`')

        embed.add_field(name=f'**Description:** Shows a member\'s highest role.', value='\uFEFF', inline=False)
        embed.add_field(name=f'**Usage:** `$toprole [member]`', value='\uFEFF', inline=False)
        await ctx.send(embed=embed)

    #   $perms
    @help.command(aliases=['perms_for', 'permissions', 'check_permissions'])
    async def perms(self, ctx):
        embed = discord.Embed(colour=randomhex(), title='**Command:** `perms`')

        embed.add_field(name=f'**Description:** Shows the specified member\'s permissions.', value='\uFEFF', inline=False)
        embed.add_field(name=f'**Usage:** `$perms [member]`', value='\uFEFF', inline=False)
        await ctx.send(embed=embed)

    #   $random
    @help.command(aliases=['rand', 'randint'])
    async def random(self, ctx):
        embed = discord.Embed(colour=randomhex(), title='**Command:** `rand`')

        embed.add_field(name=f'**Description:** Chooses a random number between the min and max that you specify.', value='\uFEFF', inline=False)
        embed.add_field(name=f'**Usage:** `$rand [minimum] [maximum]`', value='\uFEFF', inline=False)
        embed.add_field(name=f'**Aliases:**', value='random\nrandint', inline=False)
        await ctx.send(embed=embed)

    #   $translate
    @help.command()
    async def translate(self, ctx):
        embed = discord.Embed(colour=randomhex(), title='**Command:** `translate`')

        embed.add_field(name=f'**Description:** Translates the inputted text to english.', value='\uFEFF', inline=False)
        embed.add_field(name=f'**Usage:** `$translate [input]`', value='\uFEFF', inline=False)
        await ctx.send(embed=embed)

    #   $math
    @help.command()
    async def math(self, ctx):
        embed = discord.Embed(colour=randomhex(), title='**Command:** `math`')

        embed.add_field(name=f'**Description:** Does math. Can only do simple operations (+, -, /, and *).', value='\uFEFF', inline=False)
        embed.add_field(name=f'**Usage:** `$math [number] [operation] [number]`', value='\uFEFF', inline=False)
        await ctx.send(embed=embed)

    #   $ping
    @help.command()
    async def ping(self, ctx):
        embed = discord.Embed(colour=randomhex(), title='**Command:** `ping`')

        embed.add_field(name=f'**Description:** Sends b1nzy\'s ping.', value='\uFEFF', inline=False)
        embed.add_field(name=f'**Usage:** `$ping`', value='\uFEFF', inline=False)
        await ctx.send(embed=embed)

    #   $invite
    @help.command()
    async def invite(self, ctx):
        embed = discord.Embed(colour=randomhex(), title='**Command:** `invite`')

        embed.add_field(name=f'**Description:** Sends b1nzy\'s invite link.', value='\uFEFF', inline=False)
        embed.add_field(name=f'**Usage:** `$invite`', value='\uFEFF', inline=False)
        await ctx.send(embed=embed)

    #   $credits
    @help.command(aliases=['credit'])
    async def credits(self, ctx):
        embed = discord.Embed(colour=randomhex(), title='**Command:** `credits`')

        embed.add_field(name=f'**Description:** Who helped me make b1nzyBot.', value='\uFEFF', inline=False)
        embed.add_field(name=f'**Usage:** `$credits`', value='\uFEFF', inline=False)
        embed.add_field(name=f'**Aliases:**', value='credit', inline=False)
        await ctx.send(embed=embed)

    #   github
    @help.command(aliases=['code', 'opensource', 'sourcecode', 'source'])
    async def github(self, ctx):
        embed = discord.Embed(colour=randomhex(), title='**Command:** `github`')

        embed.add_field(name=f'**Description:** Sends the link to b1nzyBot\'s github repo.', value='\uFEFF', inline=False)
        embed.add_field(name=f'**Usage:** `$github`', value='\uFEFF', inline=False)
        embed.add_field(name=f'**Aliases:**', value='opensource\nsourcecode\nsource\ncode', inline=False)
        await ctx.send(embed=embed)

    #   $snipe
    @help.command(aliases=['deleted'])
    async def snipe(self, ctx):
        embed = discord.Embed(colour=randomhex(), title='**Command:** `snipe`')

        embed.add_field(name=f'**Description:** Shows the last deleted message in the current channel.', value='\uFEFF', inline=False)
        embed.add_field(name=f'**Usage:** `$snipe`', value='\uFEFF', inline=False)
        embed.add_field(name='**Aliases:**', value='deleted', inline=False)
        embed.set_footer(text=f'If embed is blank the deleted message was either a file or another embed.')
        await ctx.send(embed=embed)

    #   $editsnipe
    @help.command(aliases=['edited'])
    async def editsnipe(self, ctx):
        embed = discord.Embed(colour=randomhex(), title='**Command:** `editsnipe`')

        embed.add_field(name=f'**Description:** Shows the last edited message in the current channel.', value='\uFEFF', inline=False)
        embed.add_field(name=f'**Usage:** `$editsnipe`', value='\uFEFF', inline=False)
        embed.add_field(name='**Aliases:**', value='edited', inline=False)
        embed.set_footer(text=f'If embed is blank the edited message was another embed.')
        await ctx.send(embed=embed)

    #   $suicide
    @help.command()
    async def suicide(self, ctx):
        embed = discord.Embed(colour=randomhex(), title='**Command:** `suicide`')

        embed.add_field(name=f'**Description:** Sends a list of suicide hotlines.', value='\uFEFF', inline=False)
        embed.add_field(name=f'**Usage:** `$suicide`', value='\uFEFF', inline=False)
        embed.add_field(name=f'**Aliases:**', value='suicidal\nselfharm\nhelpme', inline=False)
        await ctx.send(embed=embed)

#   Voice Category

    @help.command()
    async def voice(self, ctx):
        embed = discord.Embed(colour=randomhex(), title='Voice')

        embed.add_field(name=f'\uFEFF', value='**$join** - Joins the voice channel the user is currently in.', inline=False)
        embed.add_field(name=f'\uFEFF', value='**$leave** - Disconnects b1nzy from the voice channel they\'re currently in.', inline=False)

        embed.set_footer(text='Use $help [command] for command usage and aliases.\n\nDISCLAIMER: This feature is currently a WIP and may not work.')

        await ctx.send(embed=embed)

#   Voice Commands

    #   $join
    @help.command(aliases=['connect'])
    async def join(self, ctx):
        embed = discord.Embed(colour=randomhex(), title='**Command:** `join`')

        embed.add_field(name=f'**Description:** Joins the voice channel the user is currently in.', value='\uFEFF', inline=False)
        embed.add_field(name=f'**Usage:** `$join`', value='\uFEFF', inline=False)
        embed.set_footer(text='DISCLAIMER: This feature is currently a WIP and may not work.')
        await ctx.send(embed=embed)

    #   $disconnect
    @help.command(aliases=['dc', 'disconnect', 'fuckoff'])
    async def leave(self, ctx):
        embed = discord.Embed(colour=randomhex(), title='**Command:** `leave`')

        embed.add_field(name=f'**Description:** Disconnects b1nzy from the voice channel they\'re currently in.', value='\uFEFF', inline=False)
        embed.add_field(name=f'**Usage:** `$leave`', value='\uFEFF', inline=False)
        embed.set_footer(text='DISCLAIMER: This feature is currently a WIP and may not work.')
        await ctx.send(embed=embed)

#   Economy Category

    @help.command()
    async def economy(self, ctx):
        embed = discord.Embed(colour=randomhex(), title='Economy')

        embed.add_field(name=f'\uFEFF', value='**$work** - Work to get money.', inline=False)
        embed.add_field(name=f'\uFEFF', value='**$bal** - Displays your balance.', inline=False)
        embed.add_field(name=f'\uFEFF', value='**$pay** - Transfer money to other users.', inline=False)

        embed.set_footer(text='Use $help [command] for command usage and aliases.\n\nDISCLAIMER: The currency feature is currently a WIP and data loss is common. Don\'t put too much time into it.')

        await ctx.send(embed=embed)

#   Economy Commands

    #   $work
    @help.command()
    async def work(self, ctx):
        embed = discord.Embed(colour=randomhex(), title='**Command:** `work`')

        embed.add_field(name=f'**Description:** Work to get money.', value='\uFEFF', inline=False)
        embed.add_field(name=f'**Usage:** `$work`', value='\uFEFF', inline=False)
        embed.set_footer(text='DISCLAIMER: The currency feature is currently a WIP and data loss is common. Don\'t put too much time into it.')
        await ctx.send(embed=embed)

    #   $balance
    @help.command(aliases=['balance'])
    async def bal(self, ctx):
        embed = discord.Embed(colour=randomhex(), title='**Command:** `bal`')

        embed.add_field(name=f'**Description:** Displays your balance.', value='\uFEFF', inline=False)
        embed.add_field(name=f'**Usage:** `$bal`', value='\uFEFF', inline=False)
        embed.add_field(name=f'**Aliases:**', value='balance', inline=False)
        embed.set_footer(text='DISCLAIMER: The currency feature is currently a WIP and data loss is common. Don\'t put too much time into it.')
        await ctx.send(embed=embed)

    #   $pay
    @help.command(aliases=['transfer', 'give'])
    async def pay(self, ctx):
        embed = discord.Embed(colour=randomhex(), title='**Command:** `pay`')

        embed.add_field(name=f'**Description:** Transfer money to other users.', value='\uFEFF', inline=False)
        embed.add_field(name=f'**Usage:** `$pay [member] [amount]`', value='\uFEFF', inline=False)
        embed.add_field(name=f'**Aliases:**', value='transfer\ngive', inline=False)
        embed.set_footer(text='DISCLAIMER: The currency feature is currently a WIP and data loss is common. Don\'t put too much time into it.')
        await ctx.send(embed=embed)

#   Moderation Category

    @help.command()
    async def moderation(self, ctx):
        embed = discord.Embed(colour=randomhex(), title='Moderation')

        embed.add_field(name=f'\uFEFF', value='**$kick** - Kicks the specified member.', inline=False)
        embed.add_field(name=f'\uFEFF', value='**$ban** - Bans the specified member.', inline=False)
        embed.add_field(name=f'\uFEFF', value='**$unban** - Unbans the specified member.', inline=False)
        embed.add_field(name=f'\uFEFF', value='**$clear** - Clears the specified number of messages, if left blank 10 messages will be cleared.', inline=False)

        embed.set_footer(text='Use $help [command] for command usage and aliases.')

        await ctx.send(embed=embed)

#   Moderation Commands

    #   $kick
    @help.command()
    async def kick(self, ctx):
        embed = discord.Embed(colour=randomhex(), title='**Command:** `kick`')

        embed.add_field(name=f'**Description:** Kicks the specified member.', value='\uFEFF', inline=False)
        embed.add_field(name=f'**Usage:** `$kick [member]`', value='\uFEFF', inline=False)
        await ctx.send(embed=embed)

    #   $ban
    @help.command()
    async def ban(self, ctx):
        embed = discord.Embed(colour=randomhex(), title='**Command:** `ban`')

        embed.add_field(name=f'**Description:** Bans the specified member.', value='\uFEFF', inline=False)
        embed.add_field(name=f'**Usage:** `$ban [member]`', value='\uFEFF', inline=False)
        await ctx.send(embed=embed)

    #   $unban
    @help.command()
    async def unban(self, ctx):
        embed = discord.Embed(colour=randomhex(), title='**Command:** `unban`')

        embed.add_field(name=f'**Description:** Unbans the specified member.', value='\uFEFF', inline=False)
        embed.add_field(name=f'**Usage:** `$unban [member]`', value='\uFEFF', inline=False)
        await ctx.send(embed=embed)

    #   $clear
    @help.command(aliases=['purge'])
    async def clear(self, ctx):
        embed = discord.Embed(colour=randomhex(), title='**Command:** `clear`')

        embed.add_field(name=f'**Description:** Clears the specified number of messages, if left blank 10 messages will be cleared.', value='\uFEFF', inline=False)
        embed.add_field(name=f'**Usage:** `$clear [amount]`', value='\uFEFF', inline=False)
        embed.add_field(name=f'**Aliases:**', value='purge', inline=False)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Help(bot))
