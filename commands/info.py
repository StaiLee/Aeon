import discord , asyncio, os, dotenv, aiosqlite
from discord.ext import commands

from commands.queries import *
from commands.classinfo import *
from commands.log import *

intents = discord.Intents.default()
intents.message_content = True

Aeonya = commands.Bot(command_prefix="*", intents=discord.Intents.all())


@Aeonya.command()
async def playimport(ctx):
    user_mention = ctx.author.mention
    embed_dive = discord.Embed(
        title=f"Welcome to Aeon Online, {ctx.author.name} !",
        description="Aeon is a Discord-based MMORPG where players choose character classes, customize gear, collect rare items, trade, and engage in epic monster battles. Join quests, form guilds, duel other players, and immerse yourself in an ever-expanding fantasy world. Discover the truth behind the world of AEON.",
        color=0x0312e3
    )

    embed_dive.add_field(name="To create your character", value="*start", inline=False)
    embed_dive.add_field(name="For the tutorial", value="*tuto", inline=False)
    embed_dive.set_image(url="https://i.pinimg.com/originals/0c/fc/8d/0cfc8d83add7f676e7068bde63bbd4de.gif")
    embed_dive.set_footer(text="Enjoy ! @stailee")

    await ctx.send(embed=embed_dive)

   



@Aeonya.command()
async def tutoimport(ctx):
    embed_tuto = discord.Embed(
        title="Welcome to the Tutorial",
        description="first of all, you need to registrer with (*start) \n then you can choose your class with (*wikiclass) \n ", 
        color = 0xe4f706
    )
    
    embed_tuto.set_image(url="https://i.pinimg.com/originals/bd/7c/0c/bd7c0cca1872e49c42b90beee03b4e24.gif")

    await ctx.send(embed=embed_tuto)

    


@Aeonya.command()
async def wikiclassimport(ctx):
    embed_wikiclass = discord.Embed(
        title="This are all the classes available (more will be add)",
        description="*rogue \n *mage \n *warrior \n *archer \n *samurai",
        color = 0x0238
    )

    await ctx.send(embed=embed_wikiclass)

@Aeonya.command()
async def wikicommandsimport(ctx):
    commands_list = [
        "-all_commands",
        "-archer",
        "-attack",
        "-classinfo",
        "-clear_history",
        "-fight",
        "-history",
        "-mage",
        "-myStats",
        "-play",
        "-record_command",
        "-reset_conversation",
        "-rogue",
        "-samurai",
        "-show_history",
        "-speak_about",
        "-start",
        "-tuto",
        "-wannabearcher",
        "-wannabemage",
        "-wannaberogue",
        "-wannabesamurai",
        "-wannabewarrior",
        "-warrior",
        "-wikiclass",
        "-wikicommands"
    ]

    commands_list.sort()

    column_size = 5
    commands_columns = [commands_list[i:i + column_size] for i in range(0, len(commands_list), column_size)]

    embed_wikicommands = discord.Embed(
        title="These are all the available commands",
        description="\n".join(["\u200b" + "\n".join(commands) for commands in commands_columns]),
        color=0xff8000
    )

    await ctx.send(embed=embed_wikicommands)


    