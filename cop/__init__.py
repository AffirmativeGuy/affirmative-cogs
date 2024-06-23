from redbot.core.bot import Red
from .cop import cop


'''async def setup(bot):
    bot.get_command("info")
    bot.remove_command("info")
    bot.get_command("ping")
    bot.remove_command("ping")
    await bot.add_cog(cop(bot))'''
async def cog_unload(self) -> None:
    global old_ping
    if old_ping:
          with contextlib.suppress(Exception):
               self.bot.remove_command("ping")
               self.bot.add_command(old_ping)
               self.bot.remove_command("info")
async def setup(bot: Red) -> None:
    global old_ping
    old_ping = bot.get_command("ping")
    if old_ping:
        bot.remove_command(old_ping.name)
        cog = cop(bot)
    await bot.add_cog(cop(bot))
  
