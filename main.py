credits="""
shit gen bot
github:
active rn
"""







#NAME ACCOUNT FILES LOWERCASED!
print(credits)
import discord,json,os,random
from discord.ext import commands

with open("config.json") as file: #loading the config 
    info = json.load(file)
    token = info["token"]
    delete = info["autodelete"]
    prefix = info["prefix"]

bot = commands.Bot(command_prefix=prefix)

   @bot.event
     async def on_ready():
    print("Bot Running!")
@bot.command() #Stock command
async def stock(ctx):
    stockmenu = discord.Embed(title="Acc Stock",description="") 
    for filename in os.listdir("Accounts"):
        with open("Accounts\\"+filename) as f: 
            ammount = len(f.read().splitlines()) 
            name = (filename[0].upper() + filename[1:].lower()).replace(".txt","") 
            stockmenu.description += f"*{name}* - {ammount}\n" 
    await ctx.send(embed=stockmenu) 



@bot.command() #gen command
async def gen(ctx,name=None):
    if name == None:
        await ctx.send("Type a name of account you want!!") 
    else:
        name = name.lower()+".txt" 
        if name not in os.listdir("Accounts"): 
            await ctx.send(f"Account Does Not Exist. `{prefix}stock`")
        else:
            with open("Accounts\\"+name) as file:
                lines = file.read().splitlines() 
            if len(lines) == 0: 
                await ctx.send("Account out of stock!") 
            else:
                with open("Accounts\\"+name) as file:
                    account = random.choice(lines)
                try: 
                    await ctx.author.send(f"`{str(account)}`\n\nMessage Will Be Deleted in {str(delete)} secounds!",delete_after=delete)
                except: 
                    await ctx.send("Error! Turn On DMS")
                else: 
                    await ctx.send("Message sent on dms")
                    with open("Accounts\\"+name,"w") as file:
                        file.write("") 
                    with open("Accounts\\"+name,"a") as file:
                        for line in lines: 
                            if line != account: 
                                file.write(line+"\n") 
bot.run(token)