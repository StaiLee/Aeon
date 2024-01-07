import discord , asyncio, os, dotenv, aiosqlite
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

Aeonya = commands.Bot(command_prefix="*", intents=discord.Intents.all())

#create info table
async def create_class_info_table():
    async with aiosqlite.connect('aeon.db') as db:
        cursor = await db.cursor()
        await cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS class_info (
                class_name TEXT PRIMARY KEY,
                base_hp INTEGER,
                base_stamina INTEGER,
                base_dexterity INTEGER,
                base_strength INTEGER,
                base_intelligence INTEGER
            )
            '''
        )
        await db.commit()

# fill the table

async def fill_class_info_table():
    class_stats = [
        ("rogue", 70, 6, 15, 5, 4),
        ("mage", 50, 5, 7, 3, 15),
        ("warrior", 110, 10, 5, 13, 2),
        ("archer", 65, 5, 12, 5, 7),
        ("samurai", 85, 6, 10, 10, 4)
    ]

    try:
        async with aiosqlite.connect('aeon.db') as db:
            for stats in class_stats:
                await db.execute('''
                    INSERT INTO class_info (class_name, base_hp, base_stamina, base_dexterity, base_strength, base_intelligence)
                    VALUES (?, ?, ?, ?, ?, ?)
                ''', stats)
            await db.commit()
    except Exception as e:
        print(f"An error occurred: {e}")

# create monster table
async def create_monster_table():
    async with aiosqlite.connect('aeon.db') as db:
        cursor = await db.execute(
            '''
            CREATE TABLE IF NOT EXISTS monster (
                monster_id INTEGER PRIMARY KEY AUTOINCREMENT,
                monster_name TEXT,
                attack INTEGER,
                health INTEGER
            )
            '''
        )
        await db.commit()

#create goblin
async def create_goblin():
    try:
        async with aiosqlite.connect('aeon.db') as db:
            await db.execute('''
                INSERT INTO monster (monster_name, attack, health)
                VALUES (?, ?, ?)
            ''', ('Goblin', 10, 10))
            await db.commit()
    except Exception as e:
        print(f"An error occurred: {e}")