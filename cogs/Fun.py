import datetime
import json
import os
import random

import aiohttp
import discord
import feedparser
import requests
import urbandictionary
import urllib3
from PIL import Image, ImageDraw, ImageFont
from discord.ext import commands
from dotenv import load_dotenv
from termcolor import cprint

load_dotenv()

YOUR_USER_ID = int(os.getenv('YOUR_USER_ID'))


intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)
currenttime = datetime.datetime.now()
guild = discord.guild


#   Random hex code generator
def randomhex(x):
    #   Define the possible characters in a hex code.
    hexvalues = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    #   Define the base of the hex code.
    hexbase = '0x'

    #   Make the hex code.
    hex = hexbase + random.choice(hexvalues)
    hex = hex + random.choice(hexvalues)
    hex = hex + random.choice(hexvalues)
    hex = hex + random.choice(hexvalues)
    hex = hex + random.choice(hexvalues)
    hex = hex + random.choice(hexvalues)

    #   Convert it into an actual hex code.
    hex = int(hex, 16)
    return hex


def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


class Fun(commands.Cog):

    # useless but nice commands.
    def __init__(self, bot):
        self.bot = bot

    # says when cog is online
    @commands.Cog.listener()
    async def on_ready(self):
        print('Fun cog is online.\n')
        cprint('------------logs------------', 'blue')

    #   sends cat pictures from random.cat
    @commands.command(aliases=['cat', 'cats', 'catpictures', 'catpics', 'catpicture'])
    async def catpic(self, ctx):
        """INFINITE CAT PICTURES!!!!!!!!!!!!!!!!"""
        async with aiohttp.ClientSession() as session:
            async with session.get('https://some-random-api.ml/facts/cat') as g:
                jscat = await g.json()
                async with session.get('http://aws.random.cat/meow') as r:
                    if r.status == 200:
                        js = await r.json()
                        embed = discord.Embed(colour=randomhex(hex))

                        embed.set_image(url=f'{js["file"]}')
                        embed.set_footer(text=f'{jscat["fact"]}')
                        await ctx.send(embed=embed)

    #   sends a quote pulled from quotable API
    @commands.command()
    async def quote2(self, ctx):
        """Fetches a random quote via quotable."""
        async with aiohttp.ClientSession() as session:
            async with session.get('https://api.quotable.io/random') as q:
                # import json
                js = await q.json()
                await ctx.send(f"{js['content']}")

    # The reason I have this pre-set list of quotes is because I like these quotes much better than the random ones.
    @commands.command()
    async def quote(self, ctx):
        """Fetches a random quote from an internal list of quotes pulled from Phantom Forces."""
        #   pre-set list of quotes.
        quotes = ["War does not determine who is right - only who is left.", "When you do crazy things, expect crazy results", "I dream of a better tomorrow, where chickens can cross the road and not be quested about their motives", "No I didn't trip, the floor looked like it needed a hug", "Better late than never, but never late is better", "I was standing in the park wondering why frisbees got bigger as they get closer. Then it hit me.", "When tempted to fight fire with fire, remember that the fire department generally uses water.", "Some cause happiness wherever they go; others whenever they go.", "Never underestimate the power of stupid people in large groups", "A successful man is one who makes more money than his wife can spend. A successful woman is one who can find such a man.", "Behind every great man is a woman rolling her eyes.", "Perfection is not attainable, but if we chase perfection we can catch excellence.", "An idea isn't responsible for the people who believe in it.", "I would like to die on Mars. Just not on impact.", "If women ran the world we wouldn't have wars, just intense negotiations every 28 days.\n- Robin Williams", "Between two evils, I always pick the one I never tried before.", "If two wrongs don't make a right, try three.", "Man cannot live by bread alone; he must have peanut butter.", "A pessimist is a person who has had to listen to too many optimists.", "All men are equal before fish.", "I've never been married, but I tell people I'm divorced so they won't think something is wrong with me.", "O Lord, help me to be pure, but not yet.", "Any kid will run any errand for you, if you ask at bedtime.", "We owe to the Middle Ages the two worst inventions of humanity - romantic love and gunpowder.", "Guilt: the gift that keeps on giving.", "The point of war is not to die for your country, but to make the noob on the other side die for his", "Always borrow money from a pessimist. He won't expect it back.", "Friendship is like peeing on yourself: everyone can see it, but only you get the warm feeling that it brings.", "Dogs have masters. Cats have staff.", "Knowledge is knowing a tomato is a fruit; wisdom is not putting it in a fruit salad.", "Why do people say 'no offense' right before they're about to offend you?", "By all means, marry. If you get a good wife, you'll become happy; if you get a bad one, you'll become a philosopher.", "I asked God for a bike, but I know God doesn't work that way. So I stole a bike and asked for forgiveness.", "The best way to lie is to tell the truth . . . carefully edited truth.", "Do not argue with an idiot. He will drag you down to his level and beat you with experience.", "The only mystery in life is why the kamikaze pilots wore helmets.", "Going to church doesn't make you a Christian any more than standing in a garage makes you a car.", "A bargain is something you don't need at a price you can't resist.", "If you steal from one author, it's plagiarism; if you steal from many, it's research.", "If you think nobody cares if you're alive, try missing a couple of car payments.", "How is it one careless match can start a forest fire, but it takes a whole box to start a campfire?", "God gave us our relatives; thank God we can choose our friends.", "Children: You spend the first 2 years of their life teaching them to walk and talk. Then you spend the next 16 telling them to sit down and shut-up.", "Nothing sucks more than that moment during an argument when you realize you're wrong.", "By the time a man realizes that his father was right, he has a son who thinks he's wrong.", "We've all heard that a million monkeys banging on a million typewriters will eventually reproduce the entire works of Shakespeare. Now, thanks to the Internet, we know this is not true.", "Women who seek to be equal with men lack ambition.", "When you go into court you are putting your fate into the hands of twelve people who weren't smart enough to get out of jury duty.", "Those people who think they know everything are a great annoyance to those of us who do.", "By working faithfully eight hours a day you may eventually get to be boss and work twelve hours a day.", "When tempted to fight fire with fire, remember that the Fire Department usually uses water.", "America is a country where half the money is spent buying food, and the other half is spent trying to lose weight.", "A bank is a place that will lend you money, if you can prove that you don't need it.", "The best time to give advice to your children is while they're still young enough to believe you know what you're talking about.", "Tell a man there are 300 billion stars in the universe and he'll believe you. Tell him a bench has wet paint on it and he'll have to touch it to be sure.", "The human brain is a wonderful thing. It starts working the moment you are born, and never stops until you stand up to speak in public.", "At every party, there are two kinds of people'those who want to go home and those who don't. The trouble is, they are usually married to each other.", "You love flowers, but you cut them. You love animals, but you eat them. You tell me you love me, so now I'm scared!", "I don't need a hair stylist, my pillow gives me a new hairstyle every morning.", "Don't worry if plan A fails, there are 25 more letters in the alphabet.", "Studying means 10% reading and 90% complaining to your friends that you have to study.", "If you want your wife to listen to you, then talk to another woman; she will be all ears.", "You never realize how boring your life is until someone asks what you like to do for fun.", "In the morning you beg to sleep more, in the afternoon you are dying to sleep, and at night you refuse to sleep.", "When I said that I cleaned my room, I just meant I made a path from the doorway to my bed.", "Life isn't measured by the number of breaths you take, but by the number of moments that take your breath away.", "The great pleasure in life is doing what people say you cannot do.", "If we were on a sinking ship, and there was only one life vest... I would miss you so much.", "All my life I thought air was free, until I bought a bag of chips.", "Long time ago I used to have a life, until someone told me to create a Facebook account.", "Never take life seriously. Nobody gets out alive anyway."]
        await ctx.send(f'{random.choice(quotes)}')

    @commands.command(aliases=['flip', 'coin', '50/50', '5050'])
    async def coinflip(self, ctx, side='none'):
        """Coinflip 🤑🤑
        Use heads or tails to play against b1nzy.
        Input "none," or "flip" to flip and only return the side."""
        #   Define the bot's flip.
        #   1 = heads
        #   2 = tails
        botflip = random.randint(1, 2)
        #   Below is an absolute mess of if statements.
        #   If the side input is either heads or tails, then proceed with coinflip.
        if side in ['heads', 'tails', 'Heads', 'Tails']:
            #   If the user chose heads the do:
            if side in ['heads', 'Heads']:
                #    Check if b1nzy flipped heads. If b1nzy flipped heads, the user wins.
                if botflip == 1:
                    await ctx.send(f'Congrats! You won!')
                #   If b1nzy flipped tails, the user loses.
                else:
                    await ctx.send(f'Awww! You lost!')
            #   If the user's side choice is tails, then proceed with coinflip.
            elif side in ['tails', 'Tails']:
                #   If b1nzy flipped tails then the user wins.
                if botflip == 2:
                    await ctx.send(f'Congrats! You won!')
                #   If b1nzy flipped heads, then the user loses.
                else:
                    await ctx.send(f'Awww! You lost!')
        #   Allows user to flip without b1nzy, essentially just returning heads or tails without a pre-defined win/loss in the bot.
        elif side in ['none', 'flip', 'N/A', 'nill', 'null', 'nada']:
            #   I got lazy and didn't wanna make a random.choice and a list so we have this handler which does the same thing.
            #   The handler checks for heads and tails through the numbers, which we defined above.
            if botflip == 1:
                await ctx.send(f'It was heads!')
            elif botflip == 2:
                await ctx.send(f'It was tails!')
        #   Error handling.
        else:
            #   If the user provides improper input then return this.
            await ctx.send('Error: Side must be either heads or tails.')

    # 8 ball command.
    @commands.command(name='8ball')
    async def eightball(self, ctx, *, question):
        """ask a yes or no question and the 8ball will give you an answer."""
        #   list of answers.
        responses = ['As I see it, yes.', 'Ask again later.', 'Don’t count on it.', 'It is certain.', 'It is decidedly so.', 'Most likely.', 'My reply is no.', 'My sources say no.', 'Outlook not so good.', 'Outlook good.', 'Signs point to yes.', 'Very doubtful.', 'Without a doubt.', 'Yes.', 'Yes – definitely.', 'You may rely on it.']

        embed = discord.Embed(colour=randomhex(hex))

        embed.set_author(name='b1nzy', icon_url='https://cdn.discordapp.com/attachments/794323054317928478/794385737235562506/image.png')

        embed.add_field(name='Question:', value=f'{question}', inline=True)
        embed.add_field(name='Answer:', value=f'{random.choice(responses)}', inline=True)

        await ctx.send(embed=embed)

    @commands.command()
    async def topic(self, ctx):
        """Sends a conversation topic."""
        topics = ['Do you have any secret family recipes?', 'What three words best describe you?', 'Have you ever quit a job?', 'Where did you go last weekend? / What did you do last weekend?', 'If you could change anything about me, what would it be?', 'If you could have any superpower, what would it be?', 'What would be your perfect weekend?', 'Who is your oldest friend? Where did you meet them?', 'Do you have any fun family traditions?', 'What’s your favorite way to waste time?', 'Have you ever been in a fight with anyone in your family?', 'Do you have any siblings?', 'Have you ever had any pets?', 'What do you do to get rid of stress?', 'When was the last time you worked incredibly hard?', 'What is something you are obsessed with?', 'Do you enjoy your job?', 'What’s the most trouble you’ve ever been in with your mom or dad?', 'What/who/which type of person annoys you the most', 'Do you get along with the people you work for/with?', 'What’s your favorite family story?', 'What’s the most useful thing you own?', 'What three words best describe you?']
        await ctx.send(f'{random.choice(topics)}')

    #   Sends headpat gif
    @commands.command(aliases=['pat'])
    async def headpat(self, ctx, *, user=None):
        """*pats head*"""
        if user is None:
            async with aiohttp.ClientSession() as session:
                async with session.get('https://some-random-api.ml/animu/pat') as g:
                    js = await g.json()
                    embed = discord.Embed(colour=randomhex(hex), description='*Gives you a headpatt.*')
                    embed.set_image(url=f'{js["link"]}')

                    await ctx.send(embed=embed)
        else:
            message = ctx.message
            async with aiohttp.ClientSession() as session:
                async with session.get('https://some-random-api.ml/animu/pat') as g:
                    js = await g.json()
                    embed = discord.Embed(colour=randomhex(hex), description=f'*<@{message.author.id}> gives <@{message.mentions[0].id}> a headpat.*')
                    embed.set_image(url=f'{js["link"]}')

                    await ctx.send(embed=embed)

    #   Sends hugging gif
    @commands.command()
    async def hug(self, ctx, *, user=None):
        """*hugs*"""
        if user is None:
            async with aiohttp.ClientSession() as session:
                async with session.get('https://some-random-api.ml/animu/hug') as g:
                    js = await g.json()
                    embed = discord.Embed(colour=randomhex(hex), description='*Hugs you.*')
                    embed.set_image(url=f'{js["link"]}')

                    await ctx.send(embed=embed)
        else:
            message = ctx.message
            async with aiohttp.ClientSession() as session:
                async with session.get('https://some-random-api.ml/animu/hug') as g:
                    js = await g.json()
                    embed = discord.Embed(colour=randomhex(hex), description=f'*<@{message.author.id}> hugs <@{message.mentions[0].id}>.*')
                    embed.set_image(url=f'{js["link"]}')

                    await ctx.send(embed=embed)

    #   Sends kissing gif
    @commands.command()
    async def kiss(self, ctx):
        """*kisses*"""
        await ctx.send("https://tenor.com/view/love-you-lots-kiss-peachcat-gif-13985240")

    #   Sends slapping gif
    @commands.command()
    async def slap(self, ctx):
        """*slaps*"""
        await ctx.send("https://tenor.com/view/slap-face-gif-11457043")

    #   Picks a random number inbetween the values that the user specifies.
    @commands.command(aliases=['random', 'randint'])
    async def rand(self, ctx, min_num, max_num):
        """Picks a random number inbetween the specified values."""
        await ctx.send(str(random.randint(int(min_num), int(max_num))))

    #   Play rock paper scissors with b1nzy :)
    # 1 = rock, 2 = paper, 3 = scissors
    @commands.command(aliases=['rockpaperscissors'])
    async def rps(self, ctx, playeranswer):
        """Play Rock Paper Scissors with b1nzy!
        You can play using words or numbers.
        1 = rock
        2 = paper
        3 = scissors
        """
        #   choose b1nzy's answer.
        botanswer = random.randint(1, 3)
        #   if b1nzy answers with rock
        if botanswer == 1:
            if playeranswer == "rock" or '1':
                await ctx.send("It's a tie! We both chose rock!")
            elif playeranswer == "paper" or '2':
                await ctx.send("Oh no! I chose rock and you chose paper! You win!")
            elif playeranswer == "scissors" or '3':
                await ctx.send("I chose rock, and you chose scissors! You lose!")
        #   if b1nzy answers with paper
        elif botanswer == 2:
            if playeranswer == "rock" or '1':
                await ctx.send("I chose paper and you chose rock! You lose!")
            elif playeranswer == "paper" or '2':
                await ctx.send("It's a tie! We both chose paper!")
            elif playeranswer == "scissors" or '3':
                await ctx.send("Oh no! I chose paper and you chose scissors! You win!")
        #   if b1nzy answers with scissors
        elif botanswer == 3:
            if playeranswer == "rock" or '1':
                await ctx.send("I chose scissors and you chose rock! You win!")
            elif playeranswer == "paper" or '2':
                await ctx.send(" I chose scissors and you chose paper! You lose!")
            elif playeranswer == "scissors" or '3':
                await ctx.send("It's a tie! We both chose scissors!")

    #   Normal UwUize a message. This command replaces certain letters.
    @commands.command(aliases=['uwuize', 'owo', 'owoize'])
    async def uwu(self, ctx, *, arg1):
        """Normal UwUize"""
        arg1 = arg1.replace("l", "w")
        arg1 = arg1.replace("r", "w")
        await ctx.send(arg1 + " UwU")

    #   Extreme UwUize a message. This command does the same stuff as the normal UwUize but also replaces whole words with special versions.
    @commands.command(aliases=['xuwuize', 'xowo', 'xowoize'])
    async def xuwu(self, ctx, *, arg1):
        """Extreme UwUize."""
        arg1 = arg1.replace("l", "w")
        arg1 = arg1.replace("r", "w")
        arg1 = arg1.replace("this", "dis")
        arg1 = arg1.replace("that", "dat")
        arg1 = arg1.replace("the", "de")
        arg1 = arg1.replace("you", "yuw")
        arg1 = arg1.replace("thought", "fought")
        arg1 = arg1.replace("them", "dem")
        arg1 = arg1.replace("with", "wif")
        arg1 = arg1.replace("their", "deiw")
        arg1 = arg1.replace("they're", "dey'we")
        arg1 = arg1.replace("theyre", "dey'we")
        arg1 = arg1.replace("these", "dese")
        await ctx.send(arg1 + " UwU")

    #   AI generated inspirational quotes
    @commands.command(aliases=['inspiration', 'inspireme'])
    async def inspire(self, ctx):
        """Sends an AI generated inspirational quite."""
        url = 'http://inspirobot.me/api?generate=true'
        params = {'generate': 'true'}
        response = requests.get(url, params, timeout=10)
        image = response.text

        embed = discord.Embed(colour=randomhex(hex))

        embed.set_image(url=image)

        embed.set_footer(text="This is an AI generated quote.")

        await ctx.send(embed=embed)

    #   Searches your query on urban dictionary.
    #   Does not return the results from UD, just sends a link that the user can click.
    @commands.is_nsfw()
    @commands.command(aliases=['urbans', 'urbandictionary', 'urban'])
    async def ud(self, ctx, *, query='random'):
        """Searches urban dictionary for your input."""
        if query == 'random':
            ran = urbandictionary.random()
            limit = 1
            for r in ran:
                while limit != 0:
                    definition = r.definition
                    example = r.example

                    #   Remove all square brackets as they only have an effect on the urban dictionary website
                    definition = definition.replace('[', '')
                    definition = definition.replace(']', '')
                    example = example.replace('[', '')
                    example = example.replace(']', '')

                    #   Make an embed because all things are better in an embed
                    embed = discord.Embed(colour=randomhex(hex), title=r.word)

                    embed.add_field(name='Definition:', value=definition, inline=False)
                    embed.add_field(name='Example:', value=example, inline=False)

                    #   Send the embed.
                    await ctx.send(embed=embed)
                    limit -= 1
        else:
            #   replace spaces with %20's to function as a proper link
            query.replace(' ', '%20')
            await ctx.send(f'https://urbandictionary.com/define.php?term={query}')

    #   Sends a random pokemon :)
    @commands.command()
    async def pokemon(self, ctx):
        """Sends a random pokemon!"""
        first = random.randint(1, 152)
        second = random.randint(1, 152)
        #   Adding numbers to the link to get a truly random pokemon each time.
        image = ("https://images.alexonsager.net/pokemon/fused/" + str(first) + "/" + str(first) + "." + str(
            second) + ".png")

        embed = discord.Embed(colour=randomhex(hex))
        embed.set_image(url=image)
        embed.set_footer(text="I choose you!")

        await ctx.send(embed=embed)

    #   Sends news from the specified source
    @commands.command()
    async def news(self, ctx, source='list'):
        """Send news from a source of your choice.
        Use list to show all sources."""

        if source == "bbc":
            d = feedparser.parse("http://feeds.bbci.co.uk/news/rss.xml?edition=us#")
            a = d['entries'][0]['link']
            b = d['entries'][0]['title']
            c = b + ": " + a
            await ctx.send(c)

        if source == "cnn":
            d = feedparser.parse("http://rss.cnn.com/rss/cnn_topstories.rss")
            a = d['entries'][0]['link']
            b = d['entries'][0]['title']
            c = b + ": " + a
            await ctx.send(c)

        if source == "scmp":
            d = feedparser.parse("https://www.scmp.com/rss/91/feed")
            a = d['entries'][0]['link']
            b = d['entries'][0]['title']
            c = b + ": " + a
            await ctx.send(c)

        if source == "cbc":
            d = feedparser.parse("https://www.cbc.ca/cmlink/rss-topstories")
            a = d['entries'][0]['link']
            b = d['entries'][0]['title']
            c = b + ": " + a
            await ctx.send(c)

        if source == "propublica":
            d = feedparser.parse("http://feeds.propublica.org/propublica/main")
            a = d['entries'][0]['link']
            b = d['entries'][0]['title']
            c = b + ": " + a
            await ctx.send(c)

        if source == "list":
            await ctx.send("here's a list of the available sources: \nbbc\ncnn\nscmp\ncbc\npropublica\nreuters")

        # general error handling.
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'<@{ctx.author.id}>, You do not have the required permissions to do that.')
        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f'<@{ctx.author.id}>, this command is on cooldown for you!')

    # Why this is in the fun cog, no idea, but it works.
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        #   Put your user id here to be notified when the bot joins a guild.
        user = self.bot.get_user(YOUR_USER_ID)
        await user.send(f'I just joined **{guild.name}** (id: **{guild.id}**)!')

    # Sends very creative insults, either insults you or insults whoever you specify.
    @commands.command()
    async def insult(self, ctx, *, member=None):
        if not member:
            member = ctx.author.display_name
        http = urllib3.PoolManager()
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        test = http.request('GET', 'https://insult.mattbas.org/api/insult')
        await ctx.send(f"{member}, " + str(test.data, "utf-8"))

    # More shitty image manipulation, this one however is just kinda meant to not be great. I would make it good if the text looked centred when it's at the middle of the file but it doesn't and I don't know where to put it to properly centre it sooo.
    @commands.command()
    async def edit(self, ctx, font=None, *, content=':)'):
        img = Image.open("Background.png")
        draw = ImageDraw.Draw(img)
        if font not in ['courier', 'impact', 'minecraft', 'rust', 'monobold', 'modernsans']:
            await ctx.send('Please select a valid font.\nFont list:```\ncourier\nimpact\nminecraft\nrust\nmonobold\nmodernsans\n```')
        elif font == 'rust':
            font = ImageFont.truetype("Fonts/Rust.ttf", 300)
            draw.text((1300, 1100), content, (206, 66, 43), font=font)
            img.save('UpdatedImage.png')
            await ctx.send(file=discord.File('UpdatedImage.png'))
            os.remove('UpdatedImage.png')
        elif font == 'courier':
            font = ImageFont.truetype("Fonts/courier.ttf", 300)
            draw.text((1300, 1100), content, (206, 66, 43), font=font)
            img.save('UpdatedImage.png')
            await ctx.send(file=discord.File('UpdatedImage.png'))
            os.remove('UpdatedImage.png')
        elif font == 'impact':
            font = ImageFont.truetype("Fonts/impact.ttf", 300)
            draw.text((1300, 1100), content, (206, 66, 43), font=font)
            img.save('UpdatedImage.png')
            await ctx.send(file=discord.File('UpdatedImage.png'))
            os.remove('UpdatedImage.png')
        elif font in ['minecraft', 'mc']:
            font = ImageFont.truetype("Fonts/Minecraftia.ttf", 300)
            draw.text((1300, 1100), content, (206, 66, 43), font=font)
            img.save('UpdatedImage.png')
            await ctx.send(file=discord.File('UpdatedImage.png'))
            os.remove('UpdatedImage.png')
        elif font == 'monobold':
            font = ImageFont.truetype("Fonts/FreeMonoBold.ttf", 300)
            draw.text((1300, 1100), content, (206, 66, 43), font=font)
            img.save('UpdatedImage.png')
            await ctx.send(file=discord.File('UpdatedImage.png'))
            os.remove('UpdatedImage.png')
        elif font == 'modernsans':
            font = ImageFont.truetype("Fonts/Modern_Sans_light.otf", 300)
            draw.text((1300, 1100), content, (206, 66, 43), font=font)
            img.save('UpdatedImage.png')
            await ctx.send(file=discord.File('UpdatedImage.png'))
            os.remove('UpdatedImage.png')

    #   Shitty image manipulation that works but it just ends up looking bad
    @commands.command(aliases=['achievment', 'mc', 'minecraft'])
    async def achievement(self, ctx, *, content):
        img = Image.open('McAchievement.png')
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype('Fonts/Minecraftia.ttf', 12)
        draw.text((59, 30), content, (255, 255, 255), font=font)
        img.save('mcget.png')
        await ctx.send(file=discord.File('mcget.png'))
        os.remove('mcget.png')

    #   Send a shitty meme, seems to end up just repeating the same meme over and over
    @commands.command()
    async def meme(self, ctx):
        response = requests.get('https://some-random-api.ml/meme')
        meme = response.json()['image']
        caption = response.json()['caption']
        embed = discord.Embed(colour=randomhex(hex))
        embed.set_image(url=meme)
        embed.set_footer(text=caption)
        await ctx.send(embed=embed)

    #   WIP
    @commands.command(aliases=['mcname'])
    async def namemc(self, ctx, *, username):
        parameters = {
            'username': username
        }
        response = requests.get('https://some-random-api.ml/mc', params=parameters)
        jprint(response.json()['name_history'])
        history = response.json()['name_history']
        namehistory = []
        for d in history:
            name = d['name']


def setup(bot):
    bot.add_cog(Fun(bot))
