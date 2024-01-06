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

class CommandNode:
    def __init__(self, command):
        self.command = command
        self.next = None

class CommandHistory:
    def __init__(self):
        self.head = None

    def add_command(self, command):
        new_node = CommandNode(command)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def get_commands(self):
        commands = []
        current = self.head
        while current:
            commands.append(current.command)
            current = current.next
        return commands

# Hashtable pour stocker l'historique des commandes des utilisateurs
user_commands = {}

# Commande pour ajouter une commande à l'historique de l'utilisateur
@Aeonya.command()
async def record_commandimport(ctx, *, command):
    user_id = ctx.author.id
    if user_id not in user_commands:
        user_commands[user_id] = CommandHistory()
    user_commands[user_id].add_command(command)
    await ctx.send(f"Command '{command}' recorded for user {ctx.author.name}")

# Commande pour afficher l'historique des commandes de l'utilisateur
@Aeonya.command()
async def show_historyimport(ctx):
    user_id = ctx.author.id
    if user_id in user_commands:
        commands = user_commands[user_id].get_commands()
        await ctx.send(f"Command history for {ctx.author.name}: {commands}")
    else:
        await ctx.send("No command history found for this user")
