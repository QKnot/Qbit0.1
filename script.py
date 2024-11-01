import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord! 🤖')

@bot.command(name='help')
async def help(ctx):
    commands_list = """
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
    """
    await ctx.send(commands_list)

@bot.group(name='cp', invoke_without_command=True)
async def cp(ctx):
    """Provides options for CP resources."""
    await ctx.send("""
    **CP Options:**
    `/cp books` - Recommend CP books
    `/cp platform` - Recommend CP judge platforms
    `/cp blog` - Recommend some Bangla blogs
    `/cp banglaBlog` - Recommend some Bangla blogs
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

bot.run('YOUR_BOT_TOKEN')
