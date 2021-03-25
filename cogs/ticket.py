import json
import random
import asyncio
import discord
from discord import utils
from discord.ext import commands
from discord.ext.commands import BucketType

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
                        guild.default_role : discord.PermissionOverwrite(read_messages = False),
                        guild.me : discord.PermissionOverwrite(read_messages = True)
                    }
                    categ = await guild.create_category(name = "Freelance tickets", overwrites = overwrites)

                channel = utils.get(categ.channels, topic = str(user.id))
                if not channel:
                    channel = await categ.create_text_channel(name = f"{user.name}#{user.discriminator}", topic = str(user.id))
                    await channel.send(f"New ticket created by {user.mention}")
                
              
              
                #firs part reaction roles 
                em = discord.Embed(color = THEME1)
                em.add_field(name = "Chose a category" , value = "each category will contact the category freelancers.If there is any priblem please report it to $wip#9999")
                em.set_footer(text = "created by Turbo Team")
                em.set_thumbnail(url = "https://cdn.discordapp.com/attachments/651211380556431400/824705665662189608/istockphoto-913475058-612x612.jpg")
                msg1 = await channel.send(embed = em)
                await msg1.add_reaction('1️⃣')

                def check(reaction, user):
                    
                    return user == user and str(reaction.emoji) == '1️⃣' and not user.bot

                try:
                    reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
                except asyncio.TimeoutError:
                    await channel.send('👎')
                else:
                    await channel.send('👍')





                embed = discord.Embed(title="Request In process",
                      description="You need to answer a few questions.",
                            color=THEME1)
                
  
                await channel.send(embed=embed)
                questions=["What category of freelancers are you interested in ? ex : Developer ",
                        "What is you budget for this commission ? `ex: 100$` ",
                        "More details about the project ? max 50 ch.",
                        "skills needed  ? ex : Adobe Illustrator or Java {modulename}",
                        "You are all set to close the ticket just do !commit {proof upload a ss on a website and send the link} {amoumt of money} ex. 100 no `$`\nAnswer with `ok` to continue"]
                answers = []
                #Check Author
                def check(user):
                    return user == user and user.channel == channel
                
                for i, question in enumerate(questions):
                    embed = discord.Embed(title=f"Question {i}",
                                description=question )
                    await channel.send(embed=embed)
                    try:
                        message = await self.bot.wait_for('message', timeout=25, check=check)
                    except TimeoutError:
                        await channel.send("You didn't answer the questions in Time")
                        return
                    answers.append(message.content)
                #Check if Channel Id is valid
                
                category = answers[0]
                budget = answers[1]
                details = answers[2]
                status = answers[3]
                pos = users[str(user.id)]["commisions"]

                #check if role is valid 
                req_ch = self.bot.get_channel(822911502435614781)
                em = discord.Embed(color = THEME1)
                em.add_field(name = f"Request by {user}" , value = f"Client positive rating: `{pos}`")
                em.add_field(name = f"Request on {category}" , value = f"**Budget is :** {budget}\nDetails : ```{details}```\nSkills needed : {status}")
                
                msg = await req_ch.send(embed = em)
            
                

                
                await msg.add_reaction("🏆")
                #Check if Giveaway Cancelled
                self.cancelled = False
    


   
                        
                          

            
        
        

def setup(bot):
    bot.add_cog(TiketFreelance(bot))
    print("Tiket cog is enabled now")