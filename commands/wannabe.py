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



@Aeonya.command()
async def wannabeMageimport(ctx):
    user_id = ctx.author.id
    Aeonya.db = await aiosqlite.connect('aeon.db')
    c = await Aeonya.db.cursor()
    async with Aeonya.db.execute("SELECT * FROM user WHERE user_id = ?", (user_id,)) as cursor:
        existing_user = await cursor.fetchone()

    async with Aeonya.db.execute("SELECT * FROM class WHERE user_id = ?", (user_id,)) as cursor:
        existing_class = await cursor.fetchone()

    if not existing_user:
        await ctx.send("You need to register with the `start` command before choosing a class.")
    elif existing_class:
        await ctx.send("You already have a class assigned.")
    else:
        async with Aeonya.db.execute("INSERT INTO class (user_id, chosen_class) VALUES (?, 'mage')", (user_id,)) as cursor:
            await Aeonya.db.commit()
            await ctx.send(f"{ctx.author.name}, you have chosen the Mage class. Your adventure as a mage begins!")



@Aeonya.command()
async def wannabeSamuraiimport(ctx):
    user_id = ctx.author.id
    Aeonya.db = await aiosqlite.connect('aeon.db')
    c = await Aeonya.db.cursor()
    async with Aeonya.db.execute("SELECT * FROM user WHERE user_id = ?", (user_id,)) as cursor:
        existing_user = await cursor.fetchone()

    async with Aeonya.db.execute("SELECT * FROM class WHERE user_id = ?", (user_id,)) as cursor:
        existing_class = await cursor.fetchone()

    if not existing_user:
        await ctx.send("You need to register with the `start` command before choosing a class.")
    elif existing_class:
        await ctx.send("You already have a class assigned.")
    else:
        async with Aeonya.db.execute("INSERT INTO class (user_id, chosen_class) VALUES (?, 'samurai')", (user_id,)) as cursor:
            await Aeonya.db.commit()
            await ctx.send(f"{ctx.author.name}, you have chosen the Samurai class. Your adventure as a samurai begins!")
    


@Aeonya.command()
async def wannabeWarriorimport(ctx):
    user_id = ctx.author.id
    Aeonya.db = await aiosqlite.connect('aeon.db')
    c = await Aeonya.db.cursor()
    async with Aeonya.db.execute("SELECT * FROM user WHERE user_id = ?", (user_id,)) as cursor:
        existing_user = await cursor.fetchone()

    async with Aeonya.db.execute("SELECT * FROM class WHERE user_id = ?", (user_id,)) as cursor:
        existing_class = await cursor.fetchone()

    if not existing_user:
        await ctx.send("You need to register with the `start` command before choosing a class.")
    elif existing_class:
        await ctx.send("You already have a class assigned.")
    else:
        async with Aeonya.db.execute("INSERT INTO class (user_id, chosen_class) VALUES (?, 'warrior')", (user_id,)) as cursor:
            await Aeonya.db.commit()
            await ctx.send(f"{ctx.author.name}, you have chosen the Warrior class. Your adventure as a warrior begins!")
    

@Aeonya.command()
async def wannabeRogueimport(ctx):
    user_id = ctx.author.id
    Aeonya.db = await aiosqlite.connect('aeon.db')
    c = await Aeonya.db.cursor()
    async with Aeonya.db.execute("SELECT * FROM user WHERE user_id = ?", (user_id,)) as cursor:
        existing_user = await cursor.fetchone()

    async with Aeonya.db.execute("SELECT * FROM class WHERE user_id = ?", (user_id,)) as cursor:
        existing_class = await cursor.fetchone()

    if not existing_user:
        await ctx.send("You need to register with the `start` command before choosing a class.")
    elif existing_class:
        await ctx.send("You already have a class assigned.")
    else:
        async with Aeonya.db.execute("INSERT INTO class (user_id, chosen_class) VALUES (?, 'rogue')", (user_id,)) as cursor:
            await Aeonya.db.commit()
            await ctx.send(f"{ctx.author.name}, you have chosen the Rogue class. Your adventure as a rogue begins!")
    

@Aeonya.command()
async def wannabeArcherimport(ctx):
    user_id = ctx.author.id
    Aeonya.db = await aiosqlite.connect('aeon.db')
    c = await Aeonya.db.cursor()
    async with Aeonya.db.execute("SELECT * FROM user WHERE user_id = ?", (user_id,)) as cursor:
        existing_user = await cursor.fetchone()

    async with Aeonya.db.execute("SELECT * FROM class WHERE user_id = ?", (user_id,)) as cursor:
        existing_class = await cursor.fetchone()

    if not existing_user:
        await ctx.send("You need to register with the `start` command before choosing a class.")
    elif existing_class:
        await ctx.send("You already have a class assigned.")
    else:
        async with Aeonya.db.execute("INSERT INTO class (user_id, chosen_class) VALUES (?, 'archer')", (user_id,)) as cursor:
            await Aeonya.db.commit()
            await ctx.send(f"{ctx.author.name}, you have chosen the Archer class. Your adventure as an archer begins!")
    

