import discord
from discord.ext import comands
import random
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.bot(command_prefix= '$', intents=Intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba {bot.user}! Ben bir botum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

bot.run("MTE4NzgzODM3MTE3NTg2MjI5NQ.GFeNju.J3wl1mZCGYtQ_ziYfiT99LioQZQb_Yyajheg0s")