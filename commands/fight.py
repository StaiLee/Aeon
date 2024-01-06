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

ongoing_combats = {}  # Variable globale pour suivre les combats en cours

@Aeonya.command()
async def fightimport(ctx):
    # Vérifier s'il y a déjà un combat en cours pour cet utilisateur
    if ctx.author.id in ongoing_combats:
        await ctx.send("You are already in a battle!")
        return

    # Récupérer les stats du joueur depuis la base de données
    user_id = ctx.author.id
    async with aiosqlite.connect('aeon.db') as db:
        cursor = await db.execute("SELECT * FROM class WHERE user_id = ?", (user_id,))
        user_class = await cursor.fetchone()
        if user_class:
            class_name = user_class[1]  # Supposons que le nom de la classe soit à l'index 1
            # Obtenir les statistiques de la classe depuis la table class_info
            cursor = await db.execute("SELECT * FROM class_info WHERE class_name = ?", (class_name,))
            class_stats = await cursor.fetchone()
            if class_stats:
                # Définir les statistiques du gobelin
                gobelin_hp = 10  # HP du gobelin
                gobelin_attack = 10  # Attaque du gobelin

                # Stocker les données du combat en cours
                ongoing_combats[ctx.author.id] = {
                    'monster_hp': gobelin_hp,
                    'monster_name': 'goblin'
                }

                # Message de début de combat
                await ctx.send(f"A wild goblin appears! It has {gobelin_hp} HP. What will you do? (Type '*attack' or '*run')")
            else:
                await ctx.send("Your class stats are missing. Please choose a class using the 'wannabe...' command.")
        else:
            await ctx.send("You haven't chosen a class yet. Please choose a class using the 'wannabe...' command.")

@Aeonya.command()
async def attackimport(ctx):
    # Vérifier s'il y a un combat en cours pour cet utilisateur
    if ctx.author.id in ongoing_combats:
        # Vérifier si les données de combat existent pour cet utilisateur
        if ongoing_combats[ctx.author.id]:
            monster_hp = ongoing_combats[ctx.author.id]['monster_hp']
            monster_name = ongoing_combats[ctx.author.id]['monster_name']
            # Réduire les HP du monstre lors de l'attaque du joueur
            monster_hp -= 20
            if monster_hp <= 0:
                # Si le monstre est vaincu
                await ctx.send(f"You defeated the {monster_name}!")
                # Supprimer l'entrée du combat en cours
                del ongoing_combats[ctx.author.id]
            else:
                # Mettre à jour les HP du monstre et envoyer un message
                ongoing_combats[ctx.author.id]['monster_hp'] = monster_hp
                await ctx.send(f"You dealt 20 damage! {monster_name}'s HP: {monster_hp}")
        else:
            await ctx.send("No ongoing battle.")
    else:
        await ctx.send("No ongoing battle.")

@Aeonya.command()
async def runimport(ctx):
    # Vérifier s'il y a un combat en cours pour cet utilisateur
    if ctx.author.id in ongoing_combats:
        monster_name = ongoing_combats[ctx.author.id]['monster_name']
        # Supprimer l'entrée du combat en cours
        del ongoing_combats[ctx.author.id]
        await ctx.send(f"You run from the {monster_name}!")
    else:
        await ctx.send("No ongoing battle.")