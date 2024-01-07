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

# node logic

class CommandNode:
    def __init__(self, command, user_id):
        self.command = command
        self.user_id = user_id
        self.previous = None
        self.next = None

class CommandHistory:
    def __init__(self):
        self.head = None
        self.tail = None
        self.user_commands = {}

    def add_command(self, command, user_id):
        new_node = CommandNode(command, user_id)

        if user_id not in self.user_commands:
            self.user_commands[user_id] = new_node
        else:
            current_node = self.user_commands[user_id]
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node
            new_node.previous = current_node

    def get_last_command(self, user_id):
        if user_id in self.user_commands:
            return self.user_commands[user_id].command
        return None

    def get_all_commands(self, user_id):
        if user_id in self.user_commands:
            commands = []
            current_node = self.user_commands[user_id]
            while current_node:
                commands.append(current_node.command)
                current_node = current_node.next
            return commands
        return None

    def clear_history(self, user_id):
        if user_id in self.user_commands:
            del self.user_commands[user_id]


command_history = CommandHistory()

# log commands
@Aeonya.command()
async def historyimport(ctx):
    last_command = command_history.get_last_command(ctx.author.id)
    if last_command:
        await ctx.send(f"Last command by {ctx.author.name}: {last_command}")
    else:
        await ctx.send("No command history for this user")
    

@Aeonya.command()
async def all_commandsimport(ctx):
    all_user_commands = command_history.get_all_commands(ctx.author.id)
    if all_user_commands:
        await ctx.send(f"All commands by {ctx.author.name}: {', '.join(all_user_commands)}")
    else:
        await ctx.send("No command history for this user")
    

@Aeonya.command()
async def clear_historyimport(ctx):
    command_history.clear_history(ctx.author.id)
    await ctx.send(f"Command history cleared for {ctx.author.name}")
    
