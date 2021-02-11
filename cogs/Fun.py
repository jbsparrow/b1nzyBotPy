import random
import datetime
from discord.ext import commands
import aiohttp
import discord
import requests
import feedparser
intents = discord.Intents.default()
intents.members = True


client = discord.Client(intents=intents)
currenttime = datetime.datetime.now()
guild = discord.guild


class Fun(commands.Cog):

    # useless but nice commands.
    def __init__(self, bot):
        self.bot = bot

    # says when cog is online
    @commands.Cog.listener()
    async def on_ready(self):
        print('Fun cog is online.\n')

    #   sends cat pictures from random.cat
    @commands.command(aliases=['cat', 'cats', 'catpictures', 'catpics', 'catpicture'])
    async def catpic(self, ctx):
        """INFINITE CAT PICTURES!!!!!!!!!!!!!!!!"""
        async with aiohttp.ClientSession() as session:
            async with session.get('http://aws.random.cat/meow') as r:
                if r.status == 200:
                    js = await r.json()
                    await ctx.send(js['file'])

    #   sends a quote pulled from quotable API
    @commands.command()
    async def quote2(self, ctx):
        """Fetches a random quote via quotable."""
        async with aiohttp.ClientSession() as session:
            async with session.get('https://api.quotable.io/random') as q:
                js = await q.json()
                await ctx.send(f'''"{js['content']}"\n- {js['author']}''')

    # the reason I have this pre-set list of quotes is because I like these quotes much better than the random ones.
    @commands.command()
    async def quote(self, ctx):
        """Fetches a random quote from an internal list of quotes pulled from Phantom Forces."""
        #   pre-set list of quotes.
        quotes = ["War does not determine who is right - only who is left.", "When you do crazy things, expect crazy results", "I dream of a better tomorrow, where chickens can cross the road and not be quested about their motives", "No I didn't trip, the floor looked like it needed a hug", "Better late than never, but never late is better", "I was standing in the park wondering why frisbees got bigger as they get closer. Then it hit me.", "When tempted to fight fire with fire, remember that the fire department generally uses water.", "Some cause happiness wherever they go; others whenever they go.", "Never underestimate the power of stupid people in large groups", "A successful man is one who makes more money than his wife can spend. A successful woman is one who can find such a man.", "Behind every great man is a woman rolling her eyes.", "Perfection is not attainable, but if we chase perfection we can catch excellence.", "An idea isn't responsible for the people who believe in it.", "I would like to die on Mars. Just not on impact.", "If women ran the world we wouldn't have wars, just intense negotiations every 28 days.\n- Robin Williams", "Between two evils, I always pick the one I never tried before.", "If two wrongs don't make a right, try three.", "Man cannot live by bread alone; he must have peanut butter.", "A pessimist is a person who has had to listen to too many optimists.", "All men are equal before fish.", "I've never been married, but I tell people I'm divorced so they won't think something is wrong with me.", "O Lord, help me to be pure, but not yet.", "Any kid will run any errand for you, if you ask at bedtime.", "We owe to the Middle Ages the two worst inventions of humanity - romantic love and gunpowder.", "Guilt: the gift that keeps on giving.", "The point of war is not to die for your country, but to make the noob on the other side die for his", "Always borrow money from a pessimist. He won't expect it back.", "Friendship is like peeing on yourself: everyone can see it, but only you get the warm feeling that it brings.", "Dogs have masters. Cats have staff.", "Knowledge is knowing a tomato is a fruit; wisdom is not putting it in a fruit salad.", "Why do people say 'no offense' right before they're about to offend you?", "By all means, marry. If you get a good wife, you'll become happy; if you get a bad one, you'll become a philosopher.", "I asked God for a bike, but I know God doesn't work that way. So I stole a bike and asked for forgiveness.", "The best way to lie is to tell the truth . . . carefully edited truth.", "Do not argue with an idiot. He will drag you down to his level and beat you with experience.", "The only mystery in life is why the kamikaze pilots wore helmets.", "Going to church doesn't make you a Christian any more than standing in a garage makes you a car.", "A bargain is something you don't need at a price you can't resist.", "If you steal from one author, it's plagiarism; if you steal from many, it's research.", "If you think nobody cares if you're alive, try missing a couple of car payments.", "How is it one careless match can start a forest fire, but it takes a whole box to start a campfire?", "God gave us our relatives; thank God we can choose our friends.", "Children: You spend the first 2 years of their life teaching them to walk and talk. Then you spend the next 16 telling them to sit down and shut-up.", "Nothing sucks more than that moment during an argument when you realize you're wrong.", "By the time a man realizes that his father was right, he has a son who thinks he's wrong.", "We've all heard that a million monkeys banging on a million typewriters will eventually reproduce the entire works of Shakespeare. Now, thanks to the Internet, we know this is not true.", "Women who seek to be equal with men lack ambition.", "When you go into court you are putting your fate into the hands of twelve people who weren't smart enough to get out of jury duty.", "Those people who think they know everything are a great annoyance to those of us who do.", "By working faithfully eight hours a day you may eventually get to be boss and work twelve hours a day.", "When tempted to fight fire with fire, remember that the Fire Department usually uses water.", "America is a country where half the money is spent buying food, and the other half is spent trying to lose weight.", "A bank is a place that will lend you money, if you can prove that you don't need it.", "The best time to give advice to your children is while they're still young enough to believe you know what you're talking about.", "Tell a man there are 300 billion stars in the universe and he'll believe you. Tell him a bench has wet paint on it and he'll have to touch it to be sure.", "The human brain is a wonderful thing. It starts working the moment you are born, and never stops until you stand up to speak in public.", "At every party, there are two kinds of people'those who want to go home and those who don't. The trouble is, they are usually married to each other.", "You love flowers, but you cut them. You love animals, but you eat them. You tell me you love me, so now I'm scared!", "I don't need a hair stylist, my pillow gives me a new hairstyle every morning.", "Don't worry if plan A fails, there are 25 more letters in the alphabet.", "Studying means 10% reading and 90% complaining to your friends that you have to study.", "If you want your wife to listen to you, then talk to another woman; she will be all ears.", "You never realize how boring your life is until someone asks what you like to do for fun.", "In the morning you beg to sleep more, in the afternoon you are dying to sleep, and at night you refuse to sleep.", "When I said that I cleaned my room, I just meant I made a path from the doorway to my bed.", "Life isn't measured by the number of breaths you take, but by the number of moments that take your breath away.", "The great pleasure in life is doing what people say you cannot do.", "If we were on a sinking ship, and there was only one life vest... I would miss you so much.", "All my life I thought air was free, until I bought a bag of chips.", "Long time ago I used to have a life, until someone told me to create a Facebook account.", "Never take life seriously. Nobody gets out alive anyway."]
        await ctx.send(f'{random.choice(quotes)}')

    # 8 ball command.
    @commands.command(name='8ball')
    async def eightball(self, ctx, *, question):
        """ask a yes or no question and the 8ball will give you an answer."""
        #   list of answers.
        responses = ['As I see it, yes.', 'Ask again later.', 'Don’t count on it.', 'It is certain.', 'It is decidedly so.', 'Most likely.', 'My reply is no.', 'My sources say no.', 'Outlook not so good.', 'Outlook good.', 'Signs point to yes.', 'Very doubtful.', 'Without a doubt.', 'Yes.', 'Yes – definitely.', 'You may rely on it.']
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')
        return

    #   Sends one of b1nzy's works.
    @commands.command()
    async def blob(self, ctx):
        """blob"""
        await ctx.send('https://ablobwob.work/')

    #   Sends headpat gif
    @commands.command()
    async def headpat(self, ctx):
        """*pats head*"""
        await ctx.send("https://tenor.com/view/chihya-puchimas-patshead-anime-chibi-gif-5518317")

    #   Sends hugging gif
    @commands.command()
    async def hug(self, ctx):
        """*hugs*"""
        await ctx.send("https://tenor.com/view/hug-peachcat-cat-cute-gif-13985247")

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
    @commands.command()
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
            if playeranswer == "rock" or 1:
                await ctx.send("It's a tie! We both chose rock!")
            if playeranswer == "paper" or 2:
                await ctx.send("Oh no! I chose rock and you chose paper! You win!")
            if playeranswer == "scissors" or 3:
                await ctx.send("I chose rock, and you chose scissors! You lose!")
        #   if b1nzy answers with paper
        if botanswer == 2:
            if playeranswer == "rock" or 1:
                await ctx.send("I chose paper and you chose rock! You lose!")
            if playeranswer == "paper" or 2:
                await ctx.send("It's a tie! We both chose paper!")
            if playeranswer == "scissors" or 3:
                await ctx.send("Oh no! I chose paper and you chose scissors! You win!")
        #   if b1nzy answers with scissors
        if botanswer == 3:
            if playeranswer == "rock" or 1:
                await ctx.send("I chose scissors and you chose rock! You win!")
            if playeranswer == "paper" or 2:
                await ctx.send(" I chose scissors and you chose paper! You lose!")
            if playeranswer == "scissors" or 3:
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
        await ctx.send(image)

    #   Searches your query on urban dictionary.
    #   Does not return the results from UD, just sends a link that the user can click.
    @commands.command(aliases=['urban', 'urbandictionary'])
    async def ud(self, ctx, *, query):
        """Searches urban dictionary for your input."""
        #   Replaces spaces with %20's so that it can be included in the search term.
        query = query.replace(" ", "%20")
        await ctx.send("https://urbandictionary.com/define.php?term=" + query)

    #   Sends a random pokemon :)
    @commands.command()
    async def pokemon(self, ctx):
        """Sends a random pokemon!"""
        first = random.randint(1, 152)
        second = random.randint(1, 152)
        #   Adding numbers to the link to get a truly random pokemon each time.
        await ctx.send("https://images.alexonsager.net/pokemon/fused/" + str(first) + "/" + str(first) + "." + str(
            second) + ".png")

    #   Sends news from the specified source
    @commands.command()
    async def news(self, ctx, source):
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
        if source == "reuters":
            d = feedparser.parse("http://feeds.reuters.com/reuters/topNews")
            a = d['entries'][0]['link']
            b = d['entries'][0]['title']
            c = b + ": " + a
            await ctx.send(c)

        if source == "cbs":
            d = feedparser.parse("https://www.cbsnews.com/latest/rss/main/")
            a = d['entries'][0]['link']
            b = d['entries'][0]['title']
            c = b + ": " + a
            await ctx.send(c)
        if source == "list":
            await ctx.send("bbc, cnn, scmp, cbc, propublica, reuters, cbs")

    #   b1nzy :)
    @commands.command(aliases=['space'])
    async def b1nzy(self, ctx):
        """origin story 👀"""
        await ctx.send('https://takeb1nzyto.space')

    #   sends a picture of b1nzy
    @commands.command(hidden=True)
    async def b1nzypic(self, ctx):
        """sends a beautiful picture of the lord b1nzy himself."""
        await ctx.send(file=discord.File('cogs/lord b1nzy.png'))

        # general error handling.
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.UserInputError):
            await ctx.send(f'Incorrect arguments passed, please try again.')
            if isinstance(error, commands.CommandNotFound):
                await ctx.send(f'That command does not exist.')
            if isinstance(error, commands.MissingPermissions):
                await ctx.send(f'<@{ctx.author.id}>, You do not have the required permissions to do that.')


def setup(bot):
    bot.add_cog(Fun(bot))
