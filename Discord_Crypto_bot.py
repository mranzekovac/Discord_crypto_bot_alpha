# import all libraries we need
import bs4
import urllib.request
import time
import discord
from discord.colour import Color
from discord.ext import commands
import asyncio
from discord.ext import commands, tasks
import datetime

# price list
prices_list = []
# coins webpages
url1 = 'https://digitalcoinprice.com/coins/polymath-network'
url2 = 'https://digitalcoinprice.com/coins/bitcoin'
url3 = 'https://digitalcoinprice.com/coins/ethereum'
# other variables
i = 0
I = 1

price_D = 0
price_D2 = 0
price_D3 = 0

status1 = 0
status2 = 0
status3 = 0

msg = ""
msg2 = ""
msg3 = ""


def main():
    global price_D, price_D2, price_D3, status1, status2, status3, msg, msg2, msg3
    # POLY coin part

    sauce = urllib.request.urlopen(url1).read()
    soup = bs4.BeautifulSoup(sauce, "html.parser")

    prices = soup.find(id="quote_price").get_text()
    prices = float(prices.replace("$", ""))

    if price_D > prices:
        print("POLY ", prices, " Falls")
        status1 = 0
    elif price_D == prices:
        print("POLY ", prices, "The price is the same")
        status1 = 1
    elif price_D < prices:
        print("POLY ", prices, "It's growing")
        status1 = 2

    price_D = prices
    # BTC coin part

    sauce2 = urllib.request.urlopen(url2).read()
    soup2 = bs4.BeautifulSoup(sauce2, "html.parser")

    prices2 = soup2.find(id="quote_price").get_text()
    prices2 = float(prices2.replace("$", "").replace(",", ""))

    if price_D2 > prices2:
        print("BTC ", prices2, " Falls")
        status2 = 0
    elif price_D2 == prices2:
        print("BTC ", prices2, "The price is the same")
        status2 = 1
    elif price_D2 < prices2:
        print("BTC ", prices2, "It's growing")
        status2 = 2

    price_D2 = prices2
    # ETH coin part

    sauce3 = urllib.request.urlopen(url3).read()
    soup3 = bs4.BeautifulSoup(sauce3, "html.parser")

    prices3 = soup3.find(id="quote_price").get_text()
    prices3 = float(prices3.replace("$", "").replace(",", ""))

    if price_D3 > prices3:
        print("ETH ", prices3, " Falls")
        status3 = 0
    elif price_D3 == prices3:
        print("ETH ", prices3, "The price is the same")
        status3 = 1
    elif price_D3 < prices3:
        print("ETH ", prices3, "It's growing")
        status3 = 2

    price_D3 = prices3
    # status section
    if status1 == 0:
        msg = prices, " Falls"
    elif status1 == 1:
        msg = prices, "The price is the same"
    else:
        msg = prices, "It's growing"

    if status2 == 0:
        msg2 = prices2, " Falls"
    elif status2 == 1:
        msg2 = prices2, "The price is the same"
    else:
        msg2 = prices2, "It's growing"

    if status3 == 0:
        msg3 = prices3, " Falls"
    elif status3 == 1:
        msg3 = prices3, "The price is the same"
    else:
        msg3 = prices3, "It's growing"

    return msg, msg2, msg3


# bot call command
client = commands.Bot(command_prefix="!")


# add event
# when bot is ready
@client.event
async def on_ready():
    print("Bot is ready")


# clear command
@client.command()
async def clear(ctx, amount=500000):
    await ctx.channel.purge(limit=amount)


# command for coins stat
@tasks.loop(minutes=15.00)
async def background_loop():
    await client.wait_until_ready()
    while i < 1:
        main()
        x = datetime.datetime.now()
        y = x.strftime("%c")
        channel = client.get_channel(802134961775443998)
        embed = discord.Embed(title="Crypto prices",
                              description="The bot will automatically start every 15 minutes and give coins prices!",
                              color=0x2e2969)
        embed.add_field(name="POLY", value=msg, inline=True)
        embed.add_field(name="BTC", value=msg2, inline=True)
        embed.add_field(name="ETH", value=msg3, inline=True)
        Clockmessages = y
        await channel.send(Clockmessages)
        await channel.send(embed=embed)
        await asyncio.sleep(900)


background_loop.start()

# run bot
client.run("YOUR BOT KEY")
