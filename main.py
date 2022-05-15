
# IMPORT DISCORD.PY. ALLOWS ACCESS TO DISCORD'S API.
import discord
import random
import os

# GETS THE CLIENT OBJECT FROM DISCORD.PY. CLIENT IS SYNONYMOUS WITH BOT.
from discord import message


intents = discord.Intents.all()
bot = discord.Client(intents=intents)

# EVENT LISTENER FOR WHEN THE BOT HAS SWITCHED FROM OFFLINE TO ONLINE.
@bot.event
async def on_ready():
	# CREATES A COUNTER TO KEEP TRACK OF HOW MANY GUILDS / SERVERS THE BOT IS CONNECTED TO.
	guild_count = 0

	# LOOPS THROUGH ALL THE GUILD / SERVERS THAT THE BOT IS ASSOCIATED WITH.
	for guild in bot.guilds:
		# PRINT THE SERVER'S ID AND NAME.
		print(f"- {guild.id} (name: {guild.name})")

		# INCREMENTS THE GUILD COUNTER.
		guild_count = guild_count + 1

	# PRINTS HOW MANY GUILDS / SERVERS THE BOT IS IN.
	print("SampleDiscordBot is in " + str(guild_count) + " guilds.")

# EVENT LISTENER FOR WHEN A NEW MESSAGE IS SENT TO A CHANNEL.
@bot.event
async def on_message(message):
	# CHECKS IF THE MESSAGE THAT WAS SENT IS EQUAL TO "HELLO".
	if message.author == bot.user:
		return
	if "morbing" in message.content.lower():
		await message.channel.send(file=discord.File("./images/" + random.choice(os.listdir('./images'))))
	if "morbius" in message.content.lower():
		# SENDS BACK A MESSAGE TO THE CHANNEL.
		await message.channel.send("""Morbius is a 2022 American superhero film based on the Marvel Comics character Morbius, the Living Vampire, produced by Columbia Pictures in association with Marvel. Distributed by Sony Pictures Releasing, it is the third film in Sony's Spider-Man Universe (SSU). Directed by Daniel Espinosa and written by Matt Sazama and Burk Sharpless, it stars Jared Leto as Dr. Michael Morbius, alongside Matt Smith, Adria Arjona, Jared Harris, Al Madrigal, and Tyrese Gibson. In the film, Morbius and his surrogate brother Milo become living vampires after curing themselves of a rare blood disease.

There were several attempts to bring Morbius to the big screen since 1998, including joining the Blade franchise and having a solo film produced by Artisan Entertainment, neither of which ever came to fruition. After announcing plans for a new shared universe of films inspired by Spider-Man characters beginning with Venom (2018), Sony began developing a film based on Morbius. Sazama and Sharpless had written a script by November 2017, and Leto and Espinosa officially joined in June 2018. Work on the film began at the end of the year with further casting, ahead of production starting in London in February 2019. Filming was confirmed to have been completed by June 2019, with reshoots happening in Los Angeles the following February.

Morbius premiered at the Plaza Carso in Mexico City on March 10, 2022, and was theatrically released in the United States on April 1, 2022, after being delayed several times from an initial July 2020 date primarily due to the COVID-19 pandemic. The film received negative reviews from critics who criticized its writing, visual effects, and especially its mid-credits scenes, although Smith's performance was better received.[6][7][8] It has grossed over $162 million against a $75–83 million budget, making it the tenth highest-grossing film of 2022.""")

@bot.event
async def on_typing(channel, member, when ):
	await channel.send(f"EVERYONE PAY ATTENTION! {member.display_name} is typing a message")

# EXECUTES THE BOT WITH THE SPECIFIED TOKEN. TOKEN HAS BEEN REMOVED AND USED JUST AS AN EXAMPLE.
bot.run("OTc1MDYwMjI1OTEwNTM4MzIw.GVhdZI.1qrE_xKb7Fco2qjX7_LAYWm3FNHznykfiX9nz0")