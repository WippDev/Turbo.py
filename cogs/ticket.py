import json
import random
import asyncio
import discord
from discord import utils
from discord.ext import commands
from discord.ext.commands import BucketType
from discord.utils import get

from modules import open_account, save_bank, users

THEME1 = 0xD41C34


class TiketFreelance(commands.Cog):
    """Error Handling"""
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, reaction: discord.RawReactionActionEvent):
        if reaction.channel_id == 823150318341586984:
            if reaction.emoji.id == 802998890101080115: # yes
                guild = self.bot.get_guild(630919368192163850)
                user = reaction.member
                categ = utils.get(guild.categories, name = "Freelance tickets")
                if not categ:
                    overwrites = {
                        guild.default_role : discord.PermissionOverwrite(read_messages = True),
                        guild.me : discord.PermissionOverwrite(read_messages = True)
                    }
                    categ = await guild.create_category(name = "Freelance tickets", overwrites = overwrites)

                channel = utils.get(categ.channels, topic = str(user.id))
                if not channel:
                    channel = await categ.create_text_channel(name = f"TT-{user.name}#{user.discriminator}", topic = str(user.id))
                    await channel.send(f"New ticket created by {user.mention}")
                
                #824963914109812736
              
                #firs part reaction roles 
                em = discord.Embed(color = THEME1)
                em.add_field(name = "Chose a option !" , value = "Please do not contact us for fun that will result in a ban !\n1️⃣ - to request a freelancer\n2️⃣ - to contact staff team\n3️⃣ - to cancel the ticket")
                em.set_footer(text = "To report any bug please dm $wip#9999 , made by turbo team")
                em.set_thumbnail(url = "https://cdn.discordapp.com/avatars/799519785666347049/2acbd61602936456b43a9585174d48db.webp?size=1024")
                msg1 = await channel.send(embed = em)
                await msg1.add_reaction('1️⃣')
                await msg1.add_reaction('2️⃣')
                await msg1.add_reaction('3️⃣')
                

                def check(reaction, user):
                    
                    return user == user and str(reaction.emoji) in ["1️⃣", "2️⃣", "3️⃣", "4️⃣"] and not user.bot
                while True:
                    try:
                        reaction, user = await self.bot.wait_for("reaction_add", timeout=60, check=check)
                        if str(reaction.emoji) == "2️⃣":
                            role_id = 824963914109812736
                            role = get(guild.roles, id=role_id)
                            await channel.send(f"Staff contact {role.mention}")
                        
                        if str(reaction.emoji) == "3️⃣":
                            
                            await channel.send("Deleting the channel in 10 seconds!")
                            await asyncio.sleep(10)
                            await channel.delete()

                            

                        if str(reaction.emoji) == "1️⃣":
                        



                            embed = discord.Embed(title="Request In process",
                            description="You need to answer a few questions. For all you will have `300`s each !",
                                    color=THEME1)
                            embed.set_footer(text = "NOTE : If you do not respect our rules and create one just for fun you will be banned!")
                            
            
                            await channel.send(embed=embed)
                            questions=["<:infinite:825074114704048158> What category would you like to contact ?",
                                    "<:infinite:825074114704048158> Add a title for this commission ?",
                                    "<:infinite:825074114704048158> What is your budget for the commission ?",
                                    "<:infinite:825074114704048158> More details about the project ? max  `250 characters`",
                                    "<:infinite:825074114704048158> Skills needed ? ",
                                    "<:infinite:825074114704048158> You are all set to close the ticket just do !commit {proof upload a ss on a website and send the link} {amoumt of money} ex. 100 no `$`\nAnswer with `ok` to continue"]
                            
                            answers = []
                            #Check Author
                            def check(user):
                                return user == user and user.channel == channel
                            
                            for i, question in enumerate(questions):
                                embed = discord.Embed(title=f"Question {i}",
                                            description=question,
                                            color = 0xccd0ff )
                                await channel.send(embed=embed)
                                try:
                                    message = await self.bot.wait_for('message', timeout=300, check=check)
                                except TimeoutError:
                                    await channel.send("You didn't answer the questions in Time")
                                    return
                                answers.append(message.content)
                            #Check if Channel Id is valid
                            
                            category = answers[0]
                            title1 = answers[1]
                            budget = answers[2]
                            details = answers[3]
                            status = answers[4]
                            pos = users[str(user.id)]["commisions"]

                            #check if role is valid 
                            req_ch = self.bot.get_channel(822911502435614781)
                            em = discord.Embed(color = THEME1 , title = title1)
                            em.add_field(name = f"Request by {user}" , value = f"Client positive rating: `{pos}`" , inline= False)
                            em.add_field(name = f"Request on {category}" , value = f"**Budget is :** {budget}\nSkills needed : {status}\nDetails : ```{details}```", inline= False)
                            
                            msg = await req_ch.send(embed = em)
                            await msg.add_reaction("🏆")

                    except asyncio.TimeoutError:
                        break
                        
                        

                        
                    
                    #Check if Giveaway Cancelled
                    self.cancelled = False

                    


   
                        
                          

            
        
        

def setup(bot):
    bot.add_cog(TiketFreelance(bot))
    print("Tiket cog is enabled now")