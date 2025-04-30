import discord
import random, string
from discord.ext import commands
import os
import requests
from flask import Flask
import random
import string
from TTOKEN import TOKEN
from bot_logic import gb, ef ,vd, api, pl, gp, fc


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.command()
async def hello(ctx):
    await ctx.send(f'### Hello! im {bot.user}!')

@bot.command()
async def info(ctx):
    await ctx.send(f'### i am a bot that can tell you about global warming, my main commands are, sending videos about it, telling you what is it, tell you about the effects, and tell you almost every cities tempreture! , you can learn more by using !help command! ')

@bot.command()
async def global_warming_def(ctx):
    await ctx.send(f'## {gb()}')

@bot.command()
async def warming_effects(ctx):
    await ctx.send(f'## {ef()}')


@bot.command()
async def weather(ctx, *cities): 
    await ctx.send(f'{api(cities)}')


@bot.command()
async def videos(ctx):
    await ctx.send(vd())

@bot.command()
async def facts(ctx):
    await ctx.send(f'{pl()}')

@bot.command()
async def coin_flip(ctx):
    await ctx.send(f'coin flip:{fc()}')
    


@bot.command()
async def generate(ctx, length: int = 8):
    await ctx.send(f"Generated password: {gp(length)}")


bot.run(TOKEN)