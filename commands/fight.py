import discord , asyncio, os, dotenv, aiosqlite
from discord.ext import commands

from commands.classinfo import *
from commands.info import *
from commands.queries import *
from commands.wannabe import *
from commands.log import *

intents = discord.Intents.default()
intents.message_content = True

Aeonya = commands.Bot(command_prefix="*", intents=discord.Intents.all())

ongoing_combats = {}  # see if combat is ongoing for a user

@Aeonya.command()
async def fightimport(ctx):
    # check if there is an ongoing combat for this user
    if ctx.author.id in ongoing_combats:
        await ctx.send("You are already in a battle!")
        return

    # get stats of the user's class
    user_id = ctx.author.id
    async with aiosqlite.connect('aeon.db') as db:
        cursor = await db.execute("SELECT * FROM class WHERE user_id = ?", (user_id,))
        user_class = await cursor.fetchone()
        if user_class:
            class_name = user_class[1]  
            # get stats of the user's class 
            cursor = await db.execute("SELECT * FROM class_info WHERE class_name = ?", (class_name,))
            class_stats = await cursor.fetchone()
            if class_stats:
                # goblin stats
                gobelin_hp = 10  # gobelin HP
                gobelin_attack = 10  # attack of the gobelin

                # stock ongoing combat data for this user
                ongoing_combats[ctx.author.id] = {
                    'monster_hp': gobelin_hp,
                    'monster_name': 'goblin'
                }

                # fight message
                await ctx.send(f"A wild goblin appears! It has {gobelin_hp} HP. What will you do? (Type '*attack' or '*run')")
            else:
                await ctx.send("Your class stats are missing. Please choose a class using the 'wannabe...' command.")
        else:
            await ctx.send("You haven't chosen a class yet. Please choose a class using the 'wannabe...' command.")

@Aeonya.command()
async def attackimport(ctx):
    # check if there is an ongoing combat for this user
    if ctx.author.id in ongoing_combats:
        # check if fight data is present for this user
        if ongoing_combats[ctx.author.id]:
            monster_hp = ongoing_combats[ctx.author.id]['monster_hp']
            monster_name = ongoing_combats[ctx.author.id]['monster_name']
            # reduce monster HP by 20
            monster_hp -= 20
            if monster_hp <= 0:
                # if monster HP is 0 or less, send a message and delete the ongoing combat entry
                await ctx.send(f"You defeated the {monster_name}!")
                # delete the ongoing combat entry
                del ongoing_combats[ctx.author.id]
            else:
                # update monster HP in the ongoing combat entry
                ongoing_combats[ctx.author.id]['monster_hp'] = monster_hp
                await ctx.send(f"You dealt 20 damage! {monster_name}'s HP: {monster_hp}")
        else:
            await ctx.send("No ongoing battle.")
    else:
        await ctx.send("No ongoing battle.")

@Aeonya.command()
async def runimport(ctx):
    # check if there is an ongoing combat for this user
    if ctx.author.id in ongoing_combats:
        monster_name = ongoing_combats[ctx.author.id]['monster_name']
        # delete the ongoing combat entry
        del ongoing_combats[ctx.author.id]
        await ctx.send(f"You run from the {monster_name}!")
    else:
        await ctx.send("No ongoing battle.")