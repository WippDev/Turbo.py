import discord
from discord.ext import commands
import sqlite3 
import os
import requests
from discord.ext.commands import BucketType
#from webserver import keep_alive
from asyncio import sleep
import random
import asyncio

#start===================================

THEME1 = 0xd41c34


prefix = "!"
client = commands.Bot(command_prefix=prefix,intents=discord.Intents.all(),case_insensitive=True)



import discord
from discord.ext import tasks



client.remove_command("help")


@client.command()
async def help(ctx):
    em = discord.Embed(color = THEME1)
    em.add_field(name = "!profile" , value = "```shows your profile```" , inline = False)
    em.add_field(name = "!orders" , value = "```orders history```" , inline = False)
    em.add_field(name = "!rate" , value = "```!rate user positive/negative```" , inline = False)
    em.add_field(name = "!bio_set" , value = "```example !bio Hello , I am a 21 years old designer ```" , inline = False)
    em.add_field(name = "!timezone_set" , value = "```example : timezone_set GTM+1```" , inline = False)
    em.add_field(name = "!portofolio_set" , value = "```example : portofolio_set link to portofolio```" , inline = False)
    await ctx.send(embed = em)




async def status():
	while True:
		await client.wait_until_ready()
		await client.change_presence(
		    activity=discord.Activity(type=discord.ActivityType.watching,
		                              name=f'Official Turbo Bot'))
		await sleep(40)
		await client.change_presence(activity=discord.Activity(
		    type=discord.ActivityType.watching, name=f'I keep the data track'))
		await sleep(15)
		await client.change_presence(
		    activity=discord.Activity(type=discord.ActivityType.watching,
		                              name=f"{len(client.users)} users"))
		await sleep(15)


@client.event
async def on_ready():
	print("I AM READY!")
	client.loop.create_task(status())





cogsx = ["suggest"]

cogsy = ["suggest"]

disabled_cogs = []


for filename in os.listdir('./cogs'):
	if filename.endswith('.py'):
		try:
			client.load_extension(f'cogs.{filename[:-3]}')
		except Exception as e:
			raise e

@client.command()
async def cogs(ctx):
	embed = discord.Embed(title='Current Cogs are :({})'.format(len(cogsx)),
	                      colour=THEME1)
	for x in cogsy:
		embed.add_field(name=x, value="no help at the moment", inline=False)
		await ctx.send(embed=embed)


#enable a cog
@client.command()
@commands.cooldown(1, 10, BucketType.user)
async def enable(ctx, extention=None):
	if ctx.author.id == 586531356272754709:
		if extention == None:
			await ctx.send('> Mention a Cog to add !')
			return
		x = extention.lower()
		if x not in cogsx:
			await ctx.send(
			    'Please use a valid cog. They are listed in the command `cogs`.'
			)
			return
		try:  #what could go wrong hereeeeeeeee
			client.load_extension('cogs.{}'.format(extention))
			await ctx.send('Sucessfully enabled the **`{}`** cog!'.format(x))
		except Exception as e:
			print(e)
			await ctx.send('This cog has already been enabled.')
	else:
		await ctx.send("this command is only owner")


@client.command()
@commands.cooldown(1, 10, BucketType.user)
async def disable(ctx, extention):
	if ctx.author.id == 586531356272754709:
		x = extention.lower()
		if x not in cogsx:
			await ctx.send('> Plase enter a cog that exists')
			return
		try:
			client.unload_extension('cogs.{}'.format(extention))
			await ctx.send('Sucessfully disabled the **`{}`** cog!'.format(x))
		except Exception as e:
			print(e)
			await ctx.send('This cog has already been disabled.')
	else:
		await ctx.send("this command is only owner")










#keep_alive()  # Starts a webserver to be pinged.
token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)

