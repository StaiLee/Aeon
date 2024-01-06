import discord , asyncio, os, dotenv, aiosqlite
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

Aeonya = commands.Bot(command_prefix="*", intents=discord.Intents.all())

@Aeonya.command()
async def mageimport(ctx):
    embed_mage = discord.Embed(
        title="Mage",
        description="Mages are scholars of the arcane, wielding the elements of fire, wind, ice, and more to cast a wide array of spells. They are known for their deep understanding of the mystical arts, and their wisdom is unmatched. Mages are erudite individuals, drawing from ancient tomes and scrolls to expand their knowledge. With their command over the elements, they bring both destruction and protection to the battlefield",
        color=0xBD650C
    )

    embed_mage.add_field(name="Base Stats", value=f"HP : 50\n STAM : 5\n  DEX : 7\n  FOR : 3\n INT : 15\n")
    embed_mage.add_field(name="Weapons", value="Staff\n Wand\n Book\n Grimoire")
    embed_mage.add_field(name="Armor", value="Cloth")
    embed_mage.set_image(url="https://i.pinimg.com/originals/e3/de/97/e3de97726d52202a715325fecd0ac829.gif")

    await ctx.send(embed=embed_mage)


@Aeonya.command()
async def samuraiimport(ctx):
    embed_samourai = discord.Embed(
        title="Samurai",
        description="The Samurai class is a master of the blade, wielding their katana with precision and grace. They are known for their strict code of honor and discipline, making them formidable warriors on the battlefield. Samurais excel in one-on-one combat, where their exceptional swordsmanship and lightning-fast strikes can turn the tide of any duel. With a deep connection to the way of the warrior, they draw strength from their unwavering resolve and are often revered for their loyalty and bravery.",
        color=0x2c0b18
    )
    embed_samourai.add_field(name="Base Stats", value="HP : 85\n STAM : 6\n DEX : 10\n FOR : 10\n  INT : 4\n")
    embed_samourai.add_field(name="Weapons", value="Katana\n Sword\n 2 hands Swords\n Bow\n Axe")
    embed_samourai.add_field(name="Armor", value="Cloth\n Leather\n Mail\n")
    embed_samourai.set_image(url="https://i.pinimg.com/originals/42/a1/72/42a172a7d0ce3ffb1746f0e61bd21d1b.gif")

    await ctx.send(embed=embed_samourai)


@Aeonya.command()
async def warriorimport(ctx):
    embed_warrior = discord.Embed(
        title="Warrior",
        description="Warriors are masters of the battlefield, wielding their mighty weapons with precision and strength. They excel in the art of close combat, using swords, axes, and shields to crush their foes. Renowned for their unwavering bravery and unyielding determination, warriors charge into battle fearlessly. They are the vanguard, the protectors of their comrades, and the embodiment of strength and valor. With their unmatched physical prowess, warriors bring both formidable offense and steadfast defense to the battlefield.",
        color=0x9a939c
    )

    embed_warrior.add_field(name="Base Stats", value="HP : 110\n STAM : 10\n DEX : 5\n FOR : 13\n  INT : 2\n")
    embed_warrior.set_image(url="https://i.pinimg.com/originals/62/ca/32/62ca321f6634ca858cf7ae81cfcb71a3.gif")
    embed_warrior.add_field(name="Weapons", value="Shield\n Sword\n 2 hands Swords\n Bow\n Axe")
    embed_warrior.add_field(name="Armor", value="Cloth\n Leather\n Mail\n Plate")

    await ctx.send(embed=embed_warrior)


@Aeonya.command()
async def rogueimport(ctx):
    embed_rogue = discord.Embed(
        title="Rogue",
        description="Rogues are masters of stealth and subterfuge, using their agility and cunning to navigate the shadows. They excel in the art of precision strikes and covert operations, using daggers, poisons, and guile to outmaneuver their adversaries. Renowned for their elusive nature and their ability to slip in and out of the shadows undetected, rogues are the ultimate opportunists. They are the spies, the thieves, and the silent assassins, thriving in the world of intrigue and deceit. With their unparalleled finesse and cunning tactics, rogues bring both surprise attacks and sneaky tactics to the battlefield.",
        color=0xff264d
    )
  
    embed_rogue.add_field(name="Base Stats", value="HP : 70\n STAM : 6\n DEX : 15\n FOR : 5\n  INT : 4\n")
    embed_rogue.add_field(name="Weapons", value="Dagger\n Sword\n Bow\n")
    embed_rogue.set_image(url="https://i.pinimg.com/originals/70/2c/8a/702c8a8159c7ffcf73554437fb04b7bb.gif")
    embed_rogue.add_field(name="Armor", value="Cloth\n Leather\n")

    await ctx.send(embed=embed_rogue)


@Aeonya.command()
async def archerimport(ctx):
    embed_archer = discord.Embed(
        title="Archer",
        description="Archers are skilled marksmen, mastering the art of ranged combat and precision shots. They excel in wielding bows, crossbows, and other ranged weapons, delivering devastating attacks from a distance. Renowned for their keen eyesight and steady hands, archers are the guardians of the open field. They are the hunters, the scouts, and the protectors of the realm, striking down their foes before they draw near. With their unmatched accuracy and superior range, archers bring both long-range firepower and reconnaissance to the battlefield.",
        color = 0x00ca15
    )
    embed_archer.add_field(name="Base Stats", value="HP : 65\n STAM : 5\n DEX : 12\n FOR : 5\n  INT : 7\n")
    embed_archer.add_field(name="Weapons", value="Dagger\n CrossBow\n Bow\n")
    embed_archer.set_image(url="https://i.pinimg.com/originals/c4/44/53/c44453a5e59401eb0956b4ffdacfa44c.gif")
    embed_archer.add_field(name="Armor", value="Cloth\n Leather\n")

    await ctx.send(embed=embed_archer)