import os
from twitchio.ext import commands

'''
    File name: main.py
    Author: Nathan Wong
    Description: Adds "peko." to the end of anyone who writes a message in specified Twitch channel. It is a reference to the popular virtual Youtuber named Usada Pekora.
    Date Created: February 20th, 2021
    Date Last Modified: September 3rd, 2021
    Python Version: Python 3.8
'''

channel = input("Input channel name: ") # get channel name
channel = "#" + channel

bot = commands.Bot(
    # set up the bot
    irc_token=os.getenv("TOKEN"),
    client_id=os.getenv("ID"),
    prefix="!",
    nick="pekopwnbot",
    initial_channels=[channel]
)

@bot.event
async def event_ready():
    'Called once when the bot goes online.'
    print(f"PekoBot is online!")
    ws = bot._ws  # this is only needed to send messages within event_ready
    await ws.send_privmsg(channel, f"Pekobot activated.")

@bot.event
async def event_message(ctx):
    'Runs every time a message is sent in chat.'

    # make sure the bot ignores itself and the streamer
    if ctx.author.name.lower() == "pekopwnbot".lower():
        return

    await bot.handle_commands(ctx)

    message = ctx.content + " peko." # adds peko. to the end of a message

    await ctx.channel.send(message)

if __name__ == "__main__":
    bot.run()

