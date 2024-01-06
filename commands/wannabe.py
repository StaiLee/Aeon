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


async def get_class_stats(class_name):
    async with aiosqlite.connect('aeon.db') as db:
        cursor = await db.execute('''
            SELECT * FROM class_info WHERE class_name = ?
        ''', (class_name,))
        stats = await cursor.fetchone()
        return stats  # Retourne les statistiques de la classe choisie



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

@Aeonya.command()
async def myStatsimport(ctx):
    user_id = ctx.author.id

    async with aiosqlite.connect('aeon.db') as db:
        cursor = await db.execute("SELECT chosen_class FROM class WHERE user_id = ?", (user_id,))
        existing_class = await cursor.fetchone()

        if existing_class:
            chosen_class = existing_class[0]

            class_stats = await db.execute_fetchall(
                "SELECT * FROM class_info WHERE class_name = ?", (chosen_class,)
            )

            if class_stats:
                class_stats = class_stats[0]  # Il ne devrait y avoir qu'une seule ligne

                embed_stats = discord.Embed(
                    title=f"{ctx.author.name}'s Stats as {chosen_class.capitalize()}",
                    color=0x9a939c
                )

                embed_stats.add_field(name="Class", value=chosen_class.capitalize(), inline=False)
                embed_stats.add_field(
                    name="Base Stats",
                    value=f"HP: {class_stats[1]}\nSTAM: {class_stats[2]}\nDEX: {class_stats[3]}\nSTR: {class_stats[4]}\nINT: {class_stats[5]}",
                    inline=False
                )

                await ctx.send(embed=embed_stats)
            else:
                await ctx.send("No stats found for your class.")
        else:
            await ctx.send("You haven't chosen a class yet.")
    

