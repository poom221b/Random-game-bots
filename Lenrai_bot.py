import discord
import random
from discord.ext import commands

# สร้าง Intents
intents = discord.Intents.all()
intents.messages = True
intents.guilds = True

# สร้าง Bot
bot = commands.Bot(command_prefix='!', intents=intents)

# เก็บข้อมูลคนใส่เกมกับเกมที่จะเล่น
player_games = {}


# เพิ่มเกมที่อยากเล่น
@bot.command()
async def add_game(ctx, game: str):
    user = ctx.author.name
    if user not in player_games:
        player_games[user] = []
    if game not in player_games[user]:
        player_games[user].append(game)
        await ctx.send(f"{user} เพิ่ม {game} เข้าไปในลิส")
    else:
        await ctx.send(f"{game} มันมีอยู่ในลิสแล้ว, {user}!")


# ดูเกมที่ทุกคนเล่นทเหมือนกัน
@bot.command()
async def show_games(ctx):
    user = ctx.author.name
    if user in player_games:
        await ctx.send(f"{user}'s games: {', '.join(player_games[user])}")
    else:
        await ctx.send(f"{user} ยังไม่ได้ใส่เกมเห้ย")


# สุ่มเกมที่ทุกคนจะเล่นด้วยกัน
@bot.command()
async def random_game(ctx):
    if not player_games:
        await ctx.send("ยังไม่มีใครใส่เกมที่จะเล่น")
        return

    if len(player_games) < 2:  # ตรวจสอบว่ามีผู้เล่นมากกว่า 1 คนไหม
        await ctx.send("ต้องมีผู้เล่นอย่างน้อย 2 คนเพื่อสุ่มเกม")
        return

    # หาเกมที่ทุกคนเล่นเหมือนกัน
    all_games = list(player_games.values())
    common_games = set(all_games[0]).intersection(*all_games)

    if common_games:
        chosen_game = random.choice(list(common_games))
        await ctx.send(f"เกมที่เราจะเล่นก็คืออออ : {chosen_game}")
    else:
        await ctx.send("แยกกันเล่นเถอะเพื่อน")



# เริ่มบอท
bot.run('Token')
