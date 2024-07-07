import discord 
from redbot.core.utils.views import SetApiView
from redbot.core.utils.chat_formatting import box
import sys
import pyjokes
import random
from redbot.cogs.downloader.converters import InstalledCog
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
    def __init__(self, bot):
        self.bot = bot
    async def cog_unload(self) -> None:
         with contextlib.suppress(Exception):
             self.bot.get_command("info")
             self.bot.get_command("ping")
             self.bot.get_command("invite")
             self.bot.remove_command("invite")
             self.bot.remove_command("info")
             self.bot.remove_command("ping")
    # Some part of the update command was take from Vrt's pull command!
    @commands.command() #
    @commands.is_owner()
    async def update(self, ctx: commands.Context, *cogs: InstalledCog):
        """Updates all the installed cog's!"""
        guild = ctx.guild
        prefix = await self.bot.get_valid_prefixes(guild=guild)
        rprefix = random.choice(prefix)
        cog_update = self.bot.get_command("cog update")
        if cog_update is None:
            return await ctx.send(f"The downloader cog is not loaded, load zaa downloader cog by using `{rprefix}load downloader`!")
        if await ctx.invoke(cog_update, True, *cogs):
            await ctx.send("Doneso <a:done:1257746596968267819>")
    @commands.command()
    async def info(self, ctx):
        """Shows information about Cop<:cop:1243924879045034075>."""
        guilds = len(self.bot.guilds)
        ping = round(self.bot.latency * 1000)
        dpy_version = "{}".format(discord.__version__)
        python_version = "{}.{}.{}".format(*sys.version_info[:3])
        red_version = "{}".format(__version__)
        title = "Cop <:cop:1243924879045034075>"
        embed = discord.Embed(title=title, description="Hi, I am the most mysterious Cop(<:cop:1243924879045034075>) in the world, and I like mangoes 🥭. I am always on-duty and ready to help whenever someone wants me. Now that you know about me, it's time to tell you about my friend named [Red](https://github.com/Cog-Creators/Red-DiscordBot/tree/V3/develop/redbot). \nRed is an open source discord bot created by [Twnetysix26](https://github.com/Twentysix26) and [improved by many](https://github.com/Cog-Creators/Red-DiscordBot/graphs/contributors).")
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/1225026736379396149/1434bdad4028cb752cc0ea270a3c284c.png")
        embed.add_field( inline=False, name = ' ',  value = 'I (<:cop:1243924879045034075>) am a instance of Red-DiscordBot, if you want a bot like me(Cause i am so good and cool 😎),then you too can host your own instance by following the [Red installation docs](https://docs.discord.red/en/stable/install_guides/index.html) .\n')
        embed.add_field(inline=False, name = ' ', value = 'Use `m!credits` and `m!findcog` to view the other sources used in Cop.')
        embed.add_field( inline=False, name = ' ', value = "You may be wondering that how can I invite Cop, currently it's not possible to invite Cop, as He(The Most Dumbest Cop in the world) is a private bot, but if you still want to invite Cop, then you have to contact AffirmativeGuy.\nAffirmativeGuy:- What gem did you find in Cop, that you want to invite him? I mean he is the dumbest Cop, and he always sleeps 💤.\nProbably you should host your own Red instance instead of inviting Cop.")
        embed.add_field(inline=False, name = '', value=(f"**Server Slots:** ```{guilds}/100```"))
        embed.add_field( inline=False, name = "", value = (f"**<:suspython:1252942734738591776> Python Version: {python_version} \n<:dpy:1252942959855276143> discord.py: {dpy_version} \n<:cop:1244503516039348234> Red version: {red_version} \n<a:ping:1257736017968889959> Ping : {ping}ms\n**"))
        await ctx.send(embed=embed)
    @commands.command()
    async def credits(self, ctx):
        """Shows the credits of Cop."""
        embed = discord.Embed(title = 'The Honorable CreditBoard', description = " ")
        embed.add_field(inline=False, name = 'Red-DiscordBot', value = "Cop is a instance of Red, Created by [Twentysix26](https://github.com/Twentysix26) and [improved by many awesome people.](https://github.com/Cog-Creators/Red-DiscordBot/graphs/contributors)")
        embed.add_field(inline=False, name = 'Emojis', value = "Most of the emojis used in this bot is taken from NQN, so the credits goes to their respective owners.")  
        embed.add_field(inline=False, name = 'Cogs and their creators(Thanks to those awesome people for their work :P! <:thanks:1254778925582778389>)', value = '**[aaa3a-cogs](https://github.com/AAA3A-AAA3A/AAA3A-cogs): aaa3a\n[ad-cog](https://github.com/aikaterna/gobcog.git): aikaterna\n[adrian](https://github.com/designbyadrian/CogsByAdrian.git): thinkadrian \n[blizz-cogs](https://git.purplepanda.cc/blizz/blizz-cogs): blizzthewolf\n[crab-cogs](https://github.com/orchidalloy/crab-cogs): hollowstrawberry\n[flare-cogs](https://github.com/flaree/Flare-Cogs): flare (flare#0001)\n[fluffycogs](https://github.com/zephyrkul/FluffyCogs): Zephyrkul (Zephyrkul#1089)\n[jojocogs](https://github.com/Just-Jojo/JojoCogs): Jojo#7791\n[jumperplugins](https://github.com/Redjumpman/Jumper-Plugins): Redjumpman (Redjumpman#1337)\n[laggrons-dumb-cogs](https://github.com/retke/Laggrons-Dumb-Cogs): El Laggron\n[lui-cogs-v3](https://github.com/Injabie3/lui-cogs-v3): Injabie3#1660, sedruk, KaguneAstra#6000, TheDarkBot#1677, quachtridat・たつ#8232\n[maxcogs](https://github.com/ltzmax/maxcogs): MAX\n**')
        embed.add_field(inline=False, name = ' ', value = '**[affirmative-cogs](https://github.com/AffirmativeGuy/affirmative-cogs): affirmativeguy\n[npc-cogs](https://github.com/npc203/npc-cogs): epic guy#0715\n[pcxcogs](https://github.com/PhasecoreX/PCXCogs): PhasecoreX (PhasecoreX#0635)\n[seina-cogs](https://github.com/japandotorg/Seina-Cogs/): inthedark.org\n[sravan](https://github.com/sravan1946/sravan-cogs): sravan\n[toxic-cogs](https://github.com/NeuroAssassin/Toxic-Cogs): Neuro Assassin\n[Trusty-cogs](https://github.com/TrustyJAID/Trusty-cogs/): TrustyJAID\n[vrt-cogs](https://github.com/vertyco/vrt-cogs): Vertyco\n[yamicogs](https://github.com/yamikaitou/YamiCogs): YamiKaitou#8975\n**')
        await ctx.send(embed=embed)
    @commands.command()
    async def ping(self, ctx):
        """Shows C<:cop:1243924879045034075>p's ping"""
        ping = round(self.bot.latency * 1000)
        await ctx.send(f" You're being detained at a speed of **{ping}ms** <a:nstar:1257723866046922784> .")
    @commands.command(name="mang", aliases=["mangs", "mangoes", "balance", "bal"])
    async def mang(self, ctx, user: discord.Member = commands.Author):
        """Get info about your balance"""
        bal = await bank.get_balance(user)
        currency = await bank.get_currency_name(ctx.guild)
        msg = f"You have {bal} {currency} in your Bank account."
        await ctx.send(msg)
    @commands.command()
    async def invite(self, ctx):
        """Invite Cop to your server"""
        embed = discord.Embed(title = "Want to invite Cop?", description = (f"We've got you covered."))
        embed.add_field(inline = False, name='', value = "You may know that Cop is a private bot, not accessible to large number of servers, so we made a requirement for it.\nYou need to have at least 2000 members in your server(Excluding bots) and the server should abide by Discord's Tos.")
        embed.add_field(inline = False, name='', value = "Now that you know what do you need for inviting Cop, here's the forum link you need to fill out,\n https://affirmativeguy.github.io/invite.html")
        embed.set_image(url = 'https://media.discordapp.net/attachments/1251495443557519382/1256631212299124827/COPS_INVITE.png?ex=66817884&is=66802704&hm=33fd08ba819d0c6424bb0c2f44d536ac73eeedb9b0a6ebd923ac26967297e0e6&=&format=webp&quality=lossless&width=1025&height=342')
        await ctx.send(embed=embed)
    @commands.command()
    async def website(self, ctx):
        """Want to view my rip-off website?"""
        msg = "Here's my rip-off(<:rip:1257744824065458258>) website - https://affirmativeguy.github.io/index.html"
        await ctx.send(msg)
    @commands.command(name = "joke", aliases=["jokes", "Jokes", "random joke", "random jokes", "dev_joke"])
    async def joke(self, ctx):
        """Get some random dev based jokes."""
        joke_list = pyjokes.get_jokes()       
        random_joke = random.choice(joke_list) # Just noticed that i could just use pyjokes.get_joke instead of jokes to get a single joke lol 🤣💀
        msg = random_joke
        await ctx.send("{}".format(msg))