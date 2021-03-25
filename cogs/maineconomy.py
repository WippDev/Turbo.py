import json
import random
import asyncio
import discord
from discord.ext import commands
from discord.ext.commands import BucketType

from modules import open_account, save_bank, users

THEME1 = 0xD41C34


class EconomyProflie(commands.Cog):
    """Error Handling"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["b2c4"])
    async def profile(self, ctx, member: discord.Member = None):
        if not member:
            member = ctx.message.author

        await open_account(ctx.author)
        await open_account(member)

        user = member

        bio = users[str(member.id)]["about"]
        timez = users[str(member.id)]["timezone"]
        bank_amt = users[str(user.id)]["bank"]
        com = users[str(user.id)]["commisions"]
        neg = users[str(user.id)]["negative"]
        portofolio = users[str(user.id)]["portofolio"]
        pfp = user.avatar_url
        em = discord.Embed(
            title=f"Information about {member.name}",
            color=THEME1,
            description="For more information [click](https://www.youtube.com/watch?v=pbWFaDutdxA) here ",
        )
        em.add_field(name="About :", value=f"{bio}", inline=False)
        em.add_field(name="Portfolio :", value=f"{portofolio}", inline=False)
        em.add_field(name="Timezone: ", value=f"{timez}")
        em.add_field(name="Earnings:", value=f"{bank_amt}$  ")
        em.add_field(name="Rating:", value=f"positive:{com} | Negative: {neg}")
        em.set_footer(text="2021 Turbo Copyright®")
        em.set_thumbnail(url=str(pfp))
        await ctx.send(embed=em)

    @commands.command(name="commit")
    # @commands.cooldown(1, 2, BucketType.user)
    async def commit(self, ctx, proof, amount):
        member = ctx.author
        await open_account(ctx.author)

        user = ctx.author

        com = users[str(user.id)]["commisions"]
        if com < 1:
            em = discord.Embed(color=THEME1)
            em.add_field(
                name="Commision execution !",
                value=f"Congratulations ! {member.mention} made his first Commision , Now you have {com} \nplease wait for confirmation before aprovement !",
            )

        else:
            em = discord.Embed(color=THEME1)
            em.add_field(
                name="Commision execution !",
                value=f"Congratulations ! {member.mention} now you have  {com + 1}  Commissions done ! \nplease wait for confirmation before aprovement !",
            )

            await ctx.send(embed=em)

        channel = self.bot.get_channel(822219897958301756)
        em = discord.Embed(color=THEME1)
        em.add_field(
            name=f"Commision made by {member.id}",
            value=f"Value = {amount}\nProof = [proof screenshot]({proof})\nconfirmed = False",
        )

        msg = await channel.send(embed=em)
        await msg.add_reaction("❌")
        await msg.add_reaction("<:yes:760727679023710218>")
        if ctx.channel.category.name == "Freelance tickets":
            await ctx.send("Deleting the channel in 7200(2h) seconds!")
            await asyncio.sleep(7200)
            await ctx.channel.delete()
			
	
			
			

        

        
        # function to add to JSON

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, reaction: discord.RawReactionActionEvent):
        channel = self.bot.get_channel(822219897958301756)
        if reaction.channel_id != 822219897958301756:
            return
        if str(reaction.emoji) == "\u274c":
            mode = "Rejected"
        elif reaction.emoji.id == 760727679023710218:
            mode = "Accepted"
        else:
            print("Reaction mismatch")
            return
        msg = await self.bot.get_channel(reaction.channel_id).fetch_message(reaction.message_id)
        if msg.author !=  msg.guild.me:
            print("Author mismatch")
            return
        if self.bot.get_user(reaction.user_id).bot:
            return
        em = msg.embeds[0]
        if len(em.fields) > 1:
            return
        em.add_field(name=mode, value=f"{mode} by <@!{reaction.user_id}>")
        await msg.edit(embed=em)
        # commission_by = (int(em.name.split()[-1]))

    @commands.command()
    async def rr(self, ctx):
        self.bot.reload_extension("cogs.maineconomy")
    
    @commands.command()
    async def raw(self, ctx: commands.Context):
        msg = ctx.message.reference.cached_message or await ctx.channel.fetch_message(ctx.message.reference.message_id)
        print(msg.embeds[0].to_dict())

    @commands.command()
    async def rate(self, ctx, member: discord.Member, *, typee=None):
        await open_account(member)
        if typee.lower() not in ("positive", "negative"):
            return ctx.send("bruhh")
        else:

            if typee == "positive":
                earnings = 1
                em = discord.Embed(color=THEME1)
                em.add_field(
                    name=f"You rated :{typee} {member.name}",
                    value="Thank you for your review !",
                )
                await ctx.send(embed=em)

                users[str(member.id)]["commisions"] += earnings

                await save_bank()

            elif typee == "negative":
                earnings = 1
                em = discord.Embed(color=THEME1)
                em.add_field(
                    name=f"You rated :{typee} {member.name}",
                    value="Thank you for your review !",
                )
                await ctx.send(embed=em)

                users[str(member.id)]["negative"] += earnings

                await save_bank()

            else:
                await ctx.send("something is broke")

    @commands.command()
    async def bio_set(self, ctx, *, bio: str):
        member = ctx.author
        await open_account(member)

        users[str(member.id)]["about"] = bio
        await ctx.send(f"Bio sat us ```{bio}```")
        await save_bank()

    @commands.command()
    async def timezone_set(self, ctx, *, bio: str):
        member = ctx.author
        await open_account(member)

        users[str(member.id)]["timezone"] = bio
        await ctx.send(f"Timezone set to ```{bio}```")
        await save_bank()

    @commands.command()
    async def portofolio_set(self, ctx, *, bio: str):
        member = ctx.author
        await open_account(member)

        users[str(member.id)]["portofolio"] = bio
        await ctx.send(f"portofolio set to ```{bio}```")
        await save_bank()

    @commands.command()
    async def bio(self, ctx, member: discord.Member = None):
        if not member:
            member = ctx.message.author

        await open_account(ctx.author)
        await open_account(member)

        user = member

        portofolio = users[str(user.id)]["about"]

        em = discord.Embed(color=THEME1)
        em.add_field(name=f"{member.name}'s profile", value=f"```{portofolio}```")
        await ctx.send(embed=em)
    
    @commands.command()
    async def boom(self, ctx):
        await ctx.send("<a:boom:822793131740889099>")



    @commands.command()
    @commands.has_permissions(manage_messages =True)
    async def bio_ban(self, ctx, member: discord.Member = None):
        if not member:
            member = ctx.message.author
        bio = "banned"
        await open_account(ctx.author)
        await open_account(member)

        user = member
        await open_account(member)

        users[str(member.id)]["about"] = bio
        await save_bank()
        portofolio = users[str(user.id)]["about"]

        em = discord.Embed(color=THEME1)
        em.add_field(name=f"{member.name}'s profile bio has been banned", value=f"new bio :```{portofolio}```")
        await ctx.send(embed=em)
    

    @commands.command()
    @commands.has_permissions(manage_messages =True)
    # @has_role("admin")
    async def request(self, ctx):
        #Ask Questions
        embed = discord.Embed(title="Request In process",
                      description="You need to answer a few questions.",
                      color=THEME1)
        await ctx.send(embed=embed)
        questions=["What category of freelancers are you interested in ? ",
                   "What is you budget for this commission ? ",
                   "More details about the project ? ",
				   "status of the project ?"]
        answers = []
        #Check Author
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel
        
        for i, question in enumerate(questions):
            embed = discord.Embed(title=f"Question {i}",
                          description=question )
            await ctx.send(embed=embed)
            try:
                message = await self.bot.wait_for('message', timeout=25, check=check)
            except TimeoutError:
                await ctx.send("You didn't answer the questions in Time")
                return
            answers.append(message.content)
        #Check if Channel Id is valid
        
        channel = self.bot.get_channel(822911502435614781)
        category = answers[0]
        budget = answers[1]
        details = answers[2]
        status = answers[3]
        pos = users[str(ctx.author.id)]["commisions"]

		#check if role is valid 
        em = discord.Embed(color = THEME1)
        em.add_field(name = f"Request by {ctx.author}" , value = f"Client positive rating: `{pos}`")
        em.add_field(name = f"Request on {category}" , value = f"**Budget is :** {budget}\nDetails : {details}\nStatus : {status}")
        
        msg = await channel.send(embed = em)
    
        

        
        await msg.add_reaction("🏆")
        #Check if Giveaway Cancelled
        self.cancelled = False
       
        
        
      

def setup(bot):
    bot.add_cog(EconomyProflie(bot))
    print("EconomyProflie cog is enabled now")