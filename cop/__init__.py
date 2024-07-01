from redbot.core.bot import Red
from .cop import cop
from .cop import setup
import json
from pathlib import Path



old_info = None
old_ping = None

async def setup(bot: Red) -> None:
    global old_info
    global old_ping
    old_info = bot.get_command("info")
    old_ping = bot.get_command("ping")
    if old_info:
        bot.remove_command(old_info.name)
    if old_ping:
        bot.remove_command(old_ping.name)
    
    cog = cop(bot)
    await bot.add_cog(cog)

def teardown(bot: Red) -> None:
    global old_info
    global old_ping
    if old_info:
        bot.remove_command("info")
        bot.add_command(old_info)
    if old_ping:
        bot.remove_command("ping")
        bot.add_command(old_ping)