
# Thanks to blizz-cogs, cause the core command remove part was copied from his simpleping cog.
from .cop import cop


async def setup(bot):
    old_info_command = bot.get_command("info")
    if old_info_command:
        bot.remove_command("info")
    await bot.add_cog(cop(bot, old_info_command))
    bot.get_command("ping")
    bot.get_command("inviteset")
    bot.remove_command("ping")
    bot.remove_command("inviteset")
