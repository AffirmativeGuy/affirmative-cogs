from redbot.core.bot import Red
from .cop import cop
import json
from pathlib import Path



old_info = None
old_ping = None
old_invite = None

# Thanks to yami for helping me in understanding this part

async def setup(bot: Red) -> None: 
    global old_invite
    global old_info
    global old_ping
    global old_bank_balance
    global old_uptime
    old_uptime = bot.get_command("uptime")
    old_info = bot.get_command("info")
    old_ping = bot.get_command("ping")
    old_invite = bot.get_command("invite")
    old_bank_balance = bot.get_command("bank balance")
    if old_bank_balance:
        bot.remove_command(old_bank_balance.name)
    if old_info:
        bot.remove_command(old_info.name)
    if old_ping:
        bot.remove_command(old_ping.name)
    if old_invite:
        bot.remove_command(old_invite.name)
    if old_uptime:
        bot.remove_command(old_uptime.name)
    
    cog = cop(bot)
    await bot.add_cog(cog)

# Thanks to yami for making me understand this code
def teardown(bot: Red) -> None:
    global old_invite
    global old_info
    global old_uptime
    global old_ping
    global old_bank_balance
    if old_info:
        bot.remove_command("info")
        bot.add_command(old_info)
    if old_bank_balance:
        bot.remove_command("bank balance")
        bot.add_command(old_bank_balance)
    if old_ping:
        bot.remove_command("ping")
        bot.add_command(old_ping)
    if old_invite:
        bot.remove_command("invite")
        bot.add_command(old_invite)
    if old_uptime:
        bot.remove_command("uptime")
        bot.add_command(old_uptime)