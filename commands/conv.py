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
class Node:
    def __init__(self, question, left=None, right=None):
        self.question = question
        self.left = left
        self.right = right

class ConversationTree:
    def __init__(self):
        self.root = Node("Do you need technical support?")
        self.current_node = self.root

    def add_branch(self, question, left_answer, right_answer):
        new_node = Node(question)
        new_node.left = Node(left_answer)
        new_node.right = Node(right_answer)
        return new_node

    def reset(self):
        self.current_node = self.root

# conv tree
conversation = ConversationTree()
node_1 = conversation.add_branch("Do you need help with programming?", "Python", "Java")
node_2 = conversation.add_branch("Do you need help with hardware?", "PC", "Mobile")

conversation.root.left = node_1
conversation.root.right = node_2

# conv commands
@Aeonya.command()
async def help_conversationimport(ctx):
    conversation.reset()
    await ctx.send("Welcome to the conversation! Answer with 'yes' or 'no'")

@Aeonya.command()
async def answerimport(ctx, response):
    response = response.lower()
    if response == 'yes' and conversation.current_node.left:
        conversation.current_node = conversation.current_node.left
        await ctx.send(conversation.current_node.question)
    elif response == 'no' and conversation.current_node.right:
        conversation.current_node = conversation.current_node.right
        await ctx.send(conversation.current_node.question)
    else:
        await ctx.send("Invalid response or end of conversation")

@Aeonya.command()
async def reset_conversationimport(ctx):
    conversation.reset()
    await ctx.send("Conversation reset")

@Aeonya.command()
async def speak_aboutimport(ctx, topic):
    topic = topic.lower()
    current_node = conversation.current_node
    if current_node.left and current_node.left.question.lower() == topic:
        await ctx.send(f"Yes, I speak about {topic}")
    elif current_node.right and current_node.right.question.lower() == topic:
        await ctx.send(f"Yes, I speak about {topic}")
    else:
        await ctx.send(f"No, I don't speak about {topic}")
