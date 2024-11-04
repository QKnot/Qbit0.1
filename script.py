import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord! 🤖')

@bot.command(name='helpBot')
async def helpBot(ctx):
    commands_list = """
    ```
    Available Commands:
    /help - List all the commands
    /about - About the bot 
    /cp - Gives multiple options to select:
        a) books => Recommend CP books 
        b) platform => Recommend CP judges
        c) blog => Recommend some Bangla blogs
        d) banglaBlog => Recommend some Bangla blogs
    
    /algorithm - Gives multiple options:
        a) books => Recommend algorithmic books
        b) platform => Recommend some algorithm problem-solving platforms 
        c) blog => Recommend algorithm blogs 
        d) videos => Recommend algorithm videos

    /language - Gives multiple options:
        a) cpp => Recommend C++ reference website
            1) books => Recommend the best C++ books 
            2) roadmap => Creating a roadmap for it
    /llm - Gives multiple options:
        a) ChatGPT 3.5
        b) ChatGPT 4.0
        c) Blackbox 
        d) Llama 3.1 
        e) Sonnet 3.5 
        f) Gemini 
        
    /goatProgrammer:
        a) John Carmack 
        b) Linus Torvalds
    /birthDay - 30 Oct 2024 
    /creator - Rahul Kumar Ghosh 
    /coverpage - Generates a cover page
    ```
    """
    await ctx.send(commands_list)
    
    # /cp - Gives multiple options to select:
    #     a) books => Recommend CP books 
    #     b) platform => Recommend CP judges
    #     c) blog => Recommend some Bangla blogs
    #     d) banglaBlog => Recommend some Bangla blogs

@bot.group(name='cp', invoke_without_command=True)
async def cp(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send("""
        **CP Options:**
        Use any of these subcommands:
        `/cp books` - Recommend CP books
        `/cp platform` - Recommend CP judge platforms
        `/cp blog` - Recommend some Bangla blogs
        `/cp banglaBlog` - Recommend additional Bangla blogs
        """)

@cp.command(name='books')
async def cp_books(ctx):
    """Recommends CP books."""
    books = """
    Here are some recommended CP books:
    - "Competitive Programming" by Steven Halim and Felix Halim
    - "Introduction to Algorithms" by Thomas H. Cormen
    - "Programming Challenges" by Steven S. Skiena and Miguel A. Revilla
    """
    await ctx.send(books)

@cp.command(name='platform')
async def cp_platform(ctx):
    """Recommends CP platforms."""
    platforms = """
    Here are some popular CP platforms:
    - Codeforces: https://codeforces.com/
    - AtCoder: https://atcoder.jp/
    - LeetCode: https://leetcode.com/
    - HackerRank: https://www.hackerrank.com/
    """
    await ctx.send(platforms)

@cp.command(name='blog')
async def cp_blog(ctx):
    """Recommends CP blogs in Bangla."""
    blog = """
    Here are some Bangla CP blogs:
    - CP Bangla: https://cpbangla.com/
    - Tamim Shahriar's Blog: https://tamimshahriar.com/
    - Shafin Mahmud's Blog: https://shafin.dev/
    """
    await ctx.send(blog)

@cp.command(name='banglaBlog')
async def cp_bangla_blog(ctx):
    """Recommends additional Bangla CP blogs."""
    bangla_blog = """
    Additional Bangla CP blogs:
    - TopCoder Bangla: https://topcoderbangla.com/
    - Dhaka University Programming Society (DUPS) Blog: https://dups.cse.du.ac.bd/
    """
    await ctx.send(bangla_blog)

    # /algorithm - Gives multiple options:
    #     a) books => Recommend algorithmic books
    #     b) platform => Recommend some algorithm problem-solving platforms 
    #     c) blog => Recommend algorithm blogs 
    #     d) videos => Recommend algorithm videos

@bot.group(name='algorithm', invoke_without_command=True)
async def algorithm(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send("""
            **Algorithm Options:**
            Use any of these subcommands:
            `/algorithm books` - Recommend algorithmic books
            `/algorithm platform` - Recommend some algorithm problem-solving platforms
            `/algorithm blog` - Recommend algorithm blogs
            `/algorithm videos` - Recommend algorithm videos
        """)

#algorithm Videos 
@algorithm.command(name='videos')
async def algorithmVideos(ctx):
    algovideos = """
        [`Mit Algorithm`](https://youtube.com/playlist?list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&si=REvpiW-IkBW4Zu-X)
    """
    await ctx.send(algovideos)
bot.run('')
