import asyncio
import discord
from discord.ext import commands
import json
import random
import sys
import os
import traceback

bot = commands.Bot(command_prefix="$", case_insensitive=True)

with open("./config.json", "r") as configjsonFile:
    configData = json.load(configjsonFile)
    TOKEN = configData["DISCORD_TOKEN"]


@bot.event
async def on_ready():
    print("I am ready")


@bot.command()
async def hi(ctx):
    await ctx.send("Hello!")

@bot.command()
async def jaiv(ctx):
    await ctx.send("<#910214856089669642>")



@bot.command()
async  def ping(ctx):
    await ctx.send(f"Ping is {round(bot.latency * 1000)}ms")


@bot.command()
@commands.has_permissions(manage_messages=True)
async def say(ctx):
    embed=discord.Embed(
        title="title",
        description="msg",
        color=discord.Color.red()
    )
    embed.set_author(name= ctx.author.name, icon_url= ctx.author.avatar_url)
    embed.add_field(name="fiels 1 ", value="field value", inline=True)
    embed.add_field(name="fiels 2 ", value="field value", inline=True)
    embed.add_field(name="fiels 3 ", value="field value", inline=False)
    embed.set_footer(text="this is footer")
    embed.set_image(url= ctx.guild.icon_url)
    embed.set_thumbnail(url = ctx.author.avatar_url)
       
    await  ctx.send(embed=embed)


@bot.command()
@commands.has_permissions(manage_messages=True)
async def embed(ctx, *,title):
    v=discord.Embed(
        title=title,
        color=discord.Color.red()
    )
    await ctx.channel.purge(limit=1)
    await  ctx.send(embed=v)


@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member , * , reason):
    await member.kick(reason=reason)
    await ctx.send(f" {member.name} was successfully kicked for {reason}")

@kick.error
async def kick_error(ctx , error):
    if isinstance(error, commands.MissingRequiredArgument):
        await  ctx.send("please mention a member to kick.")

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member , * , reason):
    await member.ban(reason=reason)
    await ctx.send(f" {member.name} was successfully banned for {reason}")

@ban.error
async def ban_error(ctx , error):
    if isinstance(error, commands.MissingRequiredArgument):
        await  ctx.send("please mention a member to ban.")



@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount:int):
    await ctx.channel.purge(limit=amount+1)



@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("There was an error.Pls specify a number to Delete!")


@bot.command()
async def timer(ctx, seconds):
    try:
        secondint = int(seconds)
        if secondint <= 0:
            await  ctx.send("I can't go negative!LoL!")
            raise BaseException

        message = await ctx.send(F"Timer: {seconds}")

        while True:
            secondint -= 1
            if secondint == 0:
                await message.edit(content= "Ended!")
                break

            await message.edit(content=f"Timer: {secondint}")
            await asyncio.sleep(1)
        await  ctx.send(f"{ctx.author.mention}, Your Timer has ended!")
    except ValueError:
        await ctx.send("You must enter a number1")

@bot.event
async def on_member_join(member): 
    channel = discord.utils.get(member.guild.channels,  name=910085494833053718)
    await channel.send(f"hi {member.mention}")




bot.run(TOKEN)
