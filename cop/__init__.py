

from .cop import cop


async def setup(bot):
    bot.get_command("info")
    bot.remove_command("info")
    bot.get_command("ping")
    bot.remove_command("ping")
await bot.add_cog(cop(bot))
  
