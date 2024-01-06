import discord , asyncio, os, dotenv, aiosqlite
from discord.ext import commands

from commands.classinfo import *
from commands.info import *
from commands.queries import *
from commands.wannabe import *
from commands.log import *
from commands.conv import *
from commands.logconv import *
from commands.fight import *

intents = discord.Intents.default()
intents.message_content = True

Aeonya = commands.Bot(command_prefix="*", intents=discord.Intents.all())

@Aeonya.event
async def on_ready():
    Aeonya.db = await aiosqlite.connect('aeon.db')
    c = await Aeonya.db.cursor()
    await create_monster_table()
    await create_class_info_table()
    await fill_class_info_table()
    await create_goblin()
    print(f'We have logged in as {Aeonya.user}')


@Aeonya.command()
async def start(ctx):
    user_id = ctx.author.id
    c = await Aeonya.db.cursor()

    await c.execute("SELECT * FROM user WHERE user_id = ?", (user_id,))
    existing_user = await c.fetchone()

    if existing_user:
        await ctx.send(f"{ctx.author.name}, you are already registered. Choose a class now. (*wikiclass)")
    else:
        await c.execute("INSERT INTO user (user_id) VALUES (?)", (user_id,))
        await Aeonya.db.commit()

        await ctx.send("Welcome to the world of Aeon! Your adventure begins now. Choose a class to start your journey:\n")
        embed_choose_class = discord.Embed(
            title=f"{ctx.author.name}, choose your class!\n",
            description="\n You can choose from the following classes:\n"
                        ":crossed_swords: Samurai\n"
                        ":bow_and_arrow: Archer\n"
                        ":dagger: Rogue\n"
                        ":shield: Warrior\n"
                        ":sparkles: Mage\n\n"
                        "wannabe + class name to choose your class\n",
            color=0xea1858
        )
        embed_choose_class.set_image(url="https://i.pinimg.com/originals/3b/17/51/3b17511d6566fe9402b9567abd31ecb8.gif")

        await ctx.send(embed=embed_choose_class)

    await c.close()  



# import de toutes les commandes logs
@Aeonya.command()
async def history(ctx):
    await historyimport(ctx)
    command_history.add_command(ctx.message.content, ctx.author.id)

@Aeonya.command()
async def all_commands(ctx):
    await all_commandsimport(ctx)
    command_history.add_command(ctx.message.content, ctx.author.id)

@Aeonya.command()
async def clear_history(ctx):
    await clear_historyimport(ctx)
    command_history.add_command(ctx.message.content, ctx.author.id)

# import de toutes les commandes conv
@Aeonya.command()
async def help_conversation(ctx):
    await help_conversationimport(ctx)
    command_history.add_command(ctx.message.content, ctx.author.id)

@Aeonya.command()
async def answer(ctx, response):
    await answerimport(ctx, response)
    command_history.add_command(ctx.message.content, ctx.author.id)

@Aeonya.command()
async def reset_conversation(ctx):
    await reset_conversationimport(ctx)
    command_history.add_command(ctx.message.content, ctx.author.id)

@Aeonya.command()
async def speak_about(ctx):
    await speak_aboutimport(ctx)
    command_history.add_command(ctx.message.content, ctx.author.id)

# import de toutes les commandes logconv
    
@Aeonya.command()
async def record_command(ctx, *, command):
    await record_commandimport(ctx, command)
    command_history.add_command(ctx.message.content, ctx.author.id)

@Aeonya.command()
async def show_history(ctx):
    await show_historyimport(ctx)
    command_history.add_command(ctx.message.content, ctx.author.id)


# import des toutes les classes
@Aeonya.command()
async def warrior(ctx):
    await warriorimport(ctx)
    command_history.add_command(ctx.message.content, ctx.author.id)

@Aeonya.command()
async def mage(ctx):
    await mageimport(ctx)
    command_history.add_command(ctx.message.content, ctx.author.id)

@Aeonya.command()
async def samurai(ctx):
    await samuraiimport(ctx)
    command_history.add_command(ctx.message.content, ctx.author.id)

@Aeonya.command()
async def archer(ctx):
    await archerimport(ctx)
    command_history.add_command(ctx.message.content, ctx.author.id)

@Aeonya.command()
async def rogue(ctx):
    await rogueimport(ctx)
    command_history.add_command(ctx.message.content, ctx.author.id)

# import de touts les wannabe
@Aeonya.command()
async def wannabewarrior(ctx):
    await wannabeWarriorimport(ctx)
    command_history.add_command(ctx.message.content, ctx.author.id)

@Aeonya.command()
async def wannabemage(ctx):
    await wannabeMageimport(ctx)
    command_history.add_command(ctx.message.content, ctx.author.id)

@Aeonya.command()
async def wannabesamurai(ctx):
    await wannabeSamuraiimport(ctx)
    command_history.add_command(ctx.message.content, ctx.author.id)

@Aeonya.command()
async def wannabearcher(ctx):
    await wannabeArcherimport(ctx)
    command_history.add_command(ctx.message.content, ctx.author.id)

@Aeonya.command()
async def wannaberogue(ctx):
    await wannabeRogueimport(ctx)
    command_history.add_command(ctx.message.content, ctx.author.id)

# import de toutes les infos
@Aeonya.command()
async def tuto(ctx):
    await tutoimport(ctx)
    command_history.add_command(ctx.message.content, ctx.author.id)

@Aeonya.command()
async def wikiclass(ctx):
    await wikiclassimport(ctx)
    command_history.add_command(ctx.message.content, ctx.author.id)

@Aeonya.command()
async def play(ctx):
    await playimport(ctx)
    command_history.add_command(ctx.message.content, ctx.author.id)

# import des commandes stats
@Aeonya.command()
async def myStats(ctx):
    await myStatsimport(ctx)
    command_history.add_command(ctx.message.content, ctx.author.id)


# import des commandes fight
@Aeonya.command()
async def fight(ctx):
    await fightimport(ctx)
    command_history.add_command(ctx.message.content, ctx.author.id)

@Aeonya.command()
async def attack(ctx):
    await attackimport(ctx)
    command_history.add_command(ctx.message.content, ctx.author.id)

@Aeonya.command()
async def run(ctx):
    await runimport(ctx)
    command_history.add_command(ctx.message.content, ctx.author.id)



if __name__ == '__main__':
    async def main():
        await Aeonya.start('TOKEN')

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
