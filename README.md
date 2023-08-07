##########################################################################################
##########################################################################################
**EXAMPLE.py**

import discord
from discord.ext import commands
from owologger import processor

intents = discord.Intents.all()

bot = commands.Bot(command_prefix="?",intents=intents)
    
@bot.event
async def on_raw_message_edit(payload):
    # this is the deafult structure
    # {"sender_id": sender_id, "amount": amount, "receiver_id": receiver_id,"channel_id":message_channel_id,"guild_id":message_guild_id}
    result = processor.process(payload)

    sender_id = result["sender_id"]
    receiver_id = result["receiver_id"]
    amount = result["amount"]
    channel_id = result["channel_id"]
    guild_id = result["guild_id"]


bot.run("MTEzNTEyMDI4NzU0MTc1NTk1NA.GjaCVs.-6RyTz2pZ3WXUznO-TNhstbvE9NFOu0jhfo0Uc")

##########################################################################################
##########################################################################################
**JSON STRUCTURE**

{"sender_id": sender_id, "amount": amount, "receiver_id": receiver_id,"channel_id":message_channel_id,"guild_id":message_guild_id}