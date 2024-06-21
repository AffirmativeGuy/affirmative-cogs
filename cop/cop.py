import discord 
from redbot.core.utils.views import SetApiView
from redbot.core.utils.chat_formatting import box
import sys
from redbot.core.bot import Red
from redbot.core import (
    __version__,
    version_info as red_version_info,
    commands,
    bank,
    errors,
    i18n,
    bank,
    modlog,
) 


class cop(commands.Cog):
    """Some tools which gives info about Cop <:cop:1243924879045034075>."""
    def __init__(self, bot: Red, old_info:
    commands.Command):
       self.bot = bot
       self.old_info = old_info

    async def cog_unload(self) -> None:
       if self.old_info:
         with contextlib.suppress(Exception):
             self.bot.remove_command("info")
             self.bot.add_command(self.old_info)
    @commands.command()
    async def info(self, ctx):
        """Shows information about Cop<:cop:1243924879045034075>."""
      # The code to remove a core(in this case info) was copied from blizzard's simple ping. Thanks to his code.
        ping = round(self.bot.latency * 1000)
        python_url = "https://www.python.org/"
        dpy_repo = "https://github.com/Rapptz/discord.py"
        red_pypi = "https://pypi.org/project/Red-DiscordBot"
        dpy_version = "{}".format(discord.__version__)
        python_version = "{}.{}.{}".format(*sys.version_info[:3])
        red_version = "{}".format(__version__)
        title = "Cop <:cop:1243924879045034075>"
        embed = discord.Embed(title=title, description="Hi, I am the most mysterious Cop(<:cop:1243924879045034075>) in the world, and I like mangoes 🥭. I am always on-duty and ready to help whenever someone wants me. Now that you know about me, it's time to tell you about my friend named [Red](https://github.com/Cog-Creators/Red-DiscordBot/tree/V3/develop/redbot). \nRed is an open source discord bot created by [Twnetysix26](https://github.com/Twentysix26) and [improved by many](https://github.com/Cog-Creators/Red-DiscordBot/graphs/contributors).")
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/1225026736379396149/1434bdad4028cb752cc0ea270a3c284c.png")
        embed.add_field( inline=False, name = ' ',  value = 'I (<:cop:1243924879045034075>) am a instance of Red-DiscordBot, if you want a bot like me(Cause i am so good and cool 😎),then you too can host your own instance by following the [Red installation docs](https://docs.discord.red/en/stable/install_guides/index.html) .\n')
        embed.add_field(inline=False, name = ' ', value = 'Use `m!credits` and `m!findcog` to view the other sources used in Cop.')
        embed.add_field( inline=False, name = ' ', value = "You may be wondering that how can I invite Cop, currently it's not possible to invite Cop, as He(The Most Dumbest Cop in the world) is a private bot, but if you still want to invite Cop, then you have to contact AffirmativeGuy.\nAffirmativeGuy:- What gem did you find in Cop, that you want to invite him? I mean he is the dumbest Cop, and he always sleeps 💤.\nProbably you should host your own Red instance instead of inviting Cop.")
        embed.add_field( inline=False, name = "", value = (f"**<:suspython:1252942734738591776> Python Version: {python_version} \n<:dpy:1252942959855276143> discord.py: {dpy_version} \n<:cop:1244503516039348234> Red version: {red_version} \n🏓 Ping : {ping}ms\n**"))
        await ctx.send(embed=embed)
    @commands.command()
    async def credits(self, ctx):
        """Shows the credits of Cop."""
        title = "Credits"
        embed = discord.Embed(title = 'The Honorable CreditBoard', description = " ")
        embed.add_field(inline=False, name = 'Red-DiscordBot', value = "Cop is a instance of Red, Created by [Twnetysix26](https://github.com/Twentysix26) and [improved by many awesome people.](https://github.com/Cog-Creators/Red-DiscordBot/graphs/contributors)")
        embed.add_field(inline=False, name = 'Emojis', value = "Most of the emojis used in this bot is taken from NQN, so the credits goes to their respective owners.")  
        embed.add_field(inline=False, name = 'Cogs and their creators(Thanks to thoose awesome people for their work :P)', value = "Work In Progress 🤠")
        await ctx.send(embed=embed)
    # Since, i was having some issue in removing core commands, i made this bping instead of ping :)
    @commands.command()
    async def bping(self, ctx):
        """Shows Cop's ping"""
        ping = round(self.bot.latency * 1000)
        await ctx.send(f" You're being detained at a speed of **{ping}ms**!")
    @commands.command()
    async def mang(self, ctx, user: discord.Member = commands.Author):
        """Get info about your balance"""
        bal = await bank.get_balance(user)
        currency = await bank.get_currency_name(ctx.guild)
        embed = discord.Embed(title = "Yourrr Balance Isssss", description = (f"** {bal} {currency}**"))
        await ctx.send(embed=embed)



    @commands.command()
    async def lboard(self, ctx):
        msg = bank.get_leaderboard
      # msg = bank.get_leaderboard
        await ctx.send(msg)
         
        
        
