from redbot.core.bot import Red
from .cop import cop
from .cop import setup
import json
from pathlib import Path



old_info = None

async def setup(bot: Red) -> None:
    global old_info
    old_info = bot.get_command("info")
    if old_info:
        bot.remove_command(old_info.name)
    
    cog = cop(bot)
    await bot.add_cog(cog)

def teardown(bot: Red) -> None:
    global old_info
    if old_info:
        bot.remove_command("info")
        bot.add_command(old_info)