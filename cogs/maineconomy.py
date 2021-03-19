import discord
from discord.ext import commands
from modules import open_account , get_bank_data
import random 
import json 
from discord.ext.commands import BucketType
THEME1 = 0xd41c34



class EconomyProflie(commands.Cog):
    '''Error Handling'''
    def __init__(self, bot):
        self.bot = bot


    
    @commands.command(aliases=["b2c4"])
    async def profile(self, ctx ,  member: discord.Member = None):
        if not member:  
            member = ctx.message.author


        await open_account(ctx.author)
        await open_account(member)

        user = member

        users = await get_bank_data()
        bio = users[str(member.id)]["about"] 
        timez = users[str(member.id)]["timezone"] 
        bank_amt = users[str(user.id)]["bank"]
        com = users[str(user.id)]["commisions"] 
        neg =  users[str(user.id)]["negative"] 
        portofolio = users[str(user.id)]["portofolio"] 
        pfp = user.avatar_url
        em = discord.Embed(title = f"Information about {member.name}" , color = THEME1 , description = "For more information [click](https://www.youtube.com/watch?v=pbWFaDutdxA) here " )
        em.add_field(name = "About :" , value = f"{bio}", inline = False)
        em.add_field(name = "Portfolio :" , value = f"{portofolio}" , inline = False)
        em.add_field(name = "Timezone: " , value =f"{timez}")
        em.add_field(name = "Earnings:" , value =f"{bank_amt}$  " )
        em.add_field(name = "Rating:" , value =f"positive:{com} | Negative: {neg}" )
        em.set_footer(text = "2021 Turbo Copyright®")
        em.set_thumbnail(url=(pfp))
        await ctx.send(embed = em)
    

    @commands.command(name = "simulate")
    #@commands.cooldown(1, 2, BucketType.user)
    async def simulate(self , ctx , proof , amount ):
        member = ctx.author
        await open_account(ctx.author)
        users = await get_bank_data()


       


        user = ctx.author



        com = users[str(user.id)]["commisions"] 
        earnings = 1
        
        if com < 1:
            em = discord.Embed(color = THEME1)
            em.add_field(name = "Commision execution !" , value = f"Congratulations ! {member.mention} made his first Commision , Now you have {com} \nplease wait for confirmation before aprovement !")
        
        else:
            em = discord.Embed(color = THEME1)
            em.add_field(name = "Commision execution !" , value = f"Congratulations ! {member.mention} now you have  {com + 1}  Commissions done ! \nplease wait for confirmation before aprovement !")
        
            await ctx.send(embed = em)
        
        channel = self.bot.get_channel(822219897958301756)
        em = discord.Embed(color = THEME1)
        em.add_field(name = f"Commision made by {member.id}" , value = f"Value = {amount}\nProof = [proof screenshot]({proof})\nconfirmed = False")

        msg = await channel.send(embed = em)
        await msg.add_reaction("❌")
        await msg.add_reaction("<:yes:760727679023710218>")


       
        users[str(user.id)]["commisions"] += earnings
        # function to add to JSON 
    

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, reaction: discord.RawReactionActionEvent):
        channel = self.bot.get_channel(822219897958301756)
        if reaction.channel_id == 822219897958301756:
            if reaction.emoji.id == 760727679023710218:
                await channel.send("wow gg")



    @commands.command()
    async def rate(self , ctx ,  member:discord.Member , * , typee = None ):
        await open_account(member)
        if typee.lower() not in ("positive", "negative"): return ctx.send("bruhh")
        else:
        

            if typee == "positive":
                users = await get_bank_data()
                earnings = 1
                em = discord.Embed(color = THEME1)
                em.add_field(name = f"You rated :{typee} {member.name}" , value = "Thank you for your review !")
                await ctx.send(embed = em)

                users[str(member.id)]["commisions"] += earnings

                with open("bank.json" , "w") as f:
                    json.dump(users,f)
            
            elif typee == "negative":
                users = await get_bank_data()
                earnings = 1
                em = discord.Embed(color = THEME1)
                em.add_field(name = f"You rated :{typee} {member.name}" , value = "Thank you for your review !")
                await ctx.send(embed = em)

                users[str(member.id)]["negative"] += earnings

                with open("bank.json" , "w") as f:
                    json.dump(users,f)

                
            else :
                await ctx.send("something is broke")


    @commands.command()
    async def bio_set(self , ctx ,*, bio:str):
        member = ctx.author
        users = await get_bank_data()
        await open_account(member)


        users[str(member.id)]["about"] = bio
        await ctx.send(f"Bio sat us ```{bio}```")
        with open("bank.json" , "w") as f:
            json.dump(users,f)
    


    @commands.command()
    async def timezone_set(self , ctx ,*, bio:str):
        member = ctx.author
        users = await get_bank_data()
        await open_account(member)


        users[str(member.id)]["timezone"] = bio
        await ctx.send(f"Timezone set to ```{bio}```")
        with open("bank.json" , "w") as f:
            json.dump(users,f)
    

    @commands.command()
    async def portofolio_set(self , ctx ,*, bio:str):
        member = ctx.author
        users = await get_bank_data()
        await open_account(member)


        users[str(member.id)]["portofolio"] = bio
        await ctx.send(f"portofolio set to ```{bio}```")
        with open("bank.json" , "w") as f:
            json.dump(users,f)
    


    @commands.command()
    async def bio(self , ctx , member:discord.Member = None):
        if not member:  
            member = ctx.message.author


        await open_account(ctx.author)
        await open_account(member)

        user = member

        users = await get_bank_data()
        portofolio = users[str(user.id)]["about"] 
        
        
        em = discord.Embed(color = THEME1)
        em.add_field(name = f"{member.name}'s profile" , value = f"```{portofolio}```")
        await ctx.send(embed = em )
        
        





    
            
            
         
       
        

        





        
    
    
            
    
    



def setup(bot):
    bot.add_cog(EconomyProflie(bot))
    print("EconomyProflie cog is enabled now")